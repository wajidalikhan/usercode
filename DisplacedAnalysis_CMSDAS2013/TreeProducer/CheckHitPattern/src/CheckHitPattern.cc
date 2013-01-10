#include "TreeProducer/CheckHitPattern/interface/CheckHitPattern.h"

// To get Tracker Geometry
#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

// To convert detId to subdet/layer number.
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
//#include "DataFormats/SiStripDetId/interface/SiStripDetId.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"

#include "Utilities/General/interface/CMSexception.h"

// For a given subdetector & layer number, this static map stores the minimum and maximum
// r (or z) values if it is barrel (or endcap) respectively.
CheckHitPattern::RZrangeMap CheckHitPattern::rangeRorZ_;

CheckHitPattern::CheckHitPattern(const edm::EventSetup& iSetup) {

  //
  // Note min/max radius (z) of each barrel layer (endcap disk).
  //

  // Get Tracker geometry
  edm::ESHandle<TrackerGeometry> trackerGeometry;
  iSetup.get<TrackerDigiGeometryRecord>().get(trackerGeometry);
  const TrackingGeometry::DetContainer& dets = trackerGeometry->dets();

  // Loop over all modules in the Tracker.
  for (unsigned int i = 0; i < dets.size(); i++) {    

    // Get subdet and layer of this module
    DetInfo detInfo = this->interpretDetId(dets[i]->geographicalId());
    uint32_t subDet = detInfo.first;

    // Note r (or z) of module if barrel (or endcap).
    double r_or_z;
    if (this->barrel(subDet)) {
      r_or_z = dets[i]->position().perp();
    } else {
      r_or_z = fabs(dets[i]->position().z());
    }

    // Recover min/max r/z value of this layer/disk found so far.
    double minRZ = 999.;
    double maxRZ = 0.;
    if (rangeRorZ_.find(detInfo) != rangeRorZ_.end()) {
      minRZ = rangeRorZ_[detInfo].first;
      maxRZ = rangeRorZ_[detInfo].second;
    }

    // Update with those of this module if it exceeds them.
    if (minRZ > r_or_z) minRZ = r_or_z; 
    if (maxRZ < r_or_z) maxRZ = r_or_z;     
    rangeRorZ_[detInfo] = std::pair<double, double>(minRZ, maxRZ);
  }

#ifdef DEBUG_CHECKHITPATTERN
  RZrangeMap::const_iterator d;
  for (d = rangeRorZ_.begin(); d != rangeRorZ_.end(); d++) {
    DetInfo detInfo = d->first;
    std::pair<double, double> rangeRZ = d->second;
    std::cout<<"CHECKHITPATTERN: Tracker subdetector type="<<detInfo.first<<" layer="<<detInfo.second
	     <<" has min r (or z) ="<<rangeRZ.first<<" and max r (or z) = "<<rangeRZ.second<<std::endl; 
  }
#endif
}

CheckHitPattern::DetInfo CheckHitPattern::interpretDetId(DetId detId) {
  // Convert detId to a pair<uint32, uint32> consisting of the numbers used by HitPattern 
  // to identify subdetector and layer number respectively.
  if (detId.subdetId() == StripSubdetector::TIB) {
    return DetInfo( detId.subdetId() , TIBDetId(detId).layer() );
  } else if (detId.subdetId() == StripSubdetector::TOB) {
    return DetInfo( detId.subdetId() , TOBDetId(detId).layer() );
  } else if (detId.subdetId() == StripSubdetector::TID) {
    return DetInfo( detId.subdetId() , TIDDetId(detId).wheel() );
  } else if (detId.subdetId() == StripSubdetector::TEC) {
    return DetInfo( detId.subdetId() , TECDetId(detId).wheel() );
  } else if (detId.subdetId() == PixelSubdetector::PixelBarrel) {
    return DetInfo( detId.subdetId() , PXBDetId(detId).layer() );
  } else if (detId.subdetId() == PixelSubdetector::PixelEndcap) {
    return DetInfo( detId.subdetId() , PXFDetId(detId).disk() );
  } else {
    throw Genexception("Found DetId that is not in Tracker");
  }   
}

bool CheckHitPattern::barrel(uint32_t subDet) {
  // Determines if given sub-detector is in the barrel.
  return (subDet == StripSubdetector::TIB || subDet == StripSubdetector::TOB ||
          subDet == PixelSubdetector::PixelBarrel); 
}


std::pair<unsigned int, unsigned int> 
CheckHitPattern::analyze(const reco::Track& track, const TransientVertex& vert) 
{
  // Check if hit pattern of this track is consistent with it being produced
  // at given vertex. Pair.first gives number of hits on track in front of vertex.
  // Pair.second gives number of missing hits between vertex and innermost hit
  // on track.

  // Get hit patterns of this track
  const reco::HitPattern& hp = track.hitPattern(); 
  const reco::HitPattern& ip = track.trackerExpectedHitsInner(); 

  // Count number of valid hits on track definately in front of the vertex,
  // taking into account finite depth of each layer.
  unsigned int nHitBefore = 0;
  for (int i = 0; i < hp.numberOfHits(); i++) {
    uint32_t hit = hp.getHitPattern(i);
    if (hp.trackerHitFilter(hit) && hp.validHitFilter(hit)) {
      uint32_t subDet = hp.getSubStructure(hit);
      uint32_t layer = hp.getLayer(hit);
      DetInfo detInfo(subDet, layer);
      double maxRZ = rangeRorZ_[detInfo].second;

      if (this->barrel(subDet)) {
        if (vert.position().perp() > maxRZ) nHitBefore++;
      } else {
        if (fabs(vert.position().z()) > maxRZ) nHitBefore++;
      } 
    }
  }

  // Count number of missing hits before the innermost hit on the track,
  // taking into account finite depth of each layer.
  unsigned int nMissHitAfter = 0;
  for (int i = 0; i < ip.numberOfHits(); i++) {
    uint32_t hit = ip.getHitPattern(i);
    if (ip.trackerHitFilter(hit)) {
      uint32_t subDet = ip.getSubStructure(hit);
      uint32_t layer = ip.getLayer(hit);
      DetInfo detInfo(subDet, layer);
      double minRZ = rangeRorZ_[detInfo].first;

      if (this->barrel(subDet)) {
	if (vert.position().perp() < minRZ) nMissHitAfter++;
      } else {
	if (fabs(vert.position().z()) < minRZ) nMissHitAfter++;
      } 
    }
  }
 
  return std::pair<unsigned int, unsigned int>(nHitBefore, nMissHitAfter);
}

void CheckHitPattern::print(const reco::Track& track) const {
  // Get hit patterns of this track
  const reco::HitPattern& hp = track.hitPattern(); 
  const reco::HitPattern& ip = track.trackerExpectedHitsInner(); 

  std::cout<<"=== Hits on Track ==="<<std::endl;
  this->print(hp);
  std::cout<<"=== Hits before track ==="<<std::endl;
  this->print(ip);
}

void CheckHitPattern::print(const reco::HitPattern& hp) const {
  for (int i = 0; i < hp.numberOfHits(); i++) {
    uint32_t hit = hp.getHitPattern(i);
    if (hp.trackerHitFilter(hit)) {
      uint32_t subdet = hp.getSubStructure(hit);
      uint32_t layer = hp.getLayer(hit);
      std::cout<<"hit "<<i<<" subdet="<<subdet<<" layer="<<layer<<" type "<<hp.getHitType(hit)<<std::endl;
    }
  } 
}
