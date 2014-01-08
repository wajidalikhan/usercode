import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
           '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/0EE2182F-FC9D-E011-898F-0024E876827F.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/2655E983-FB9D-E011-8B04-0024E876807F.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/3658C54B-F49D-E011-9285-00266CF9BED8.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/3C69C714-F49D-E011-B965-00A0D1EEF69C.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/204436D7-F99D-E011-93AD-0026B94E27FD.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/4C2A7DEE-FC9D-E011-9F2C-0026B94E2831.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/2ACE1AF1-F39D-E011-A404-00A0D1EE8D6C.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/62CB78DA-FE9D-E011-9466-0024E8768819.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/38CDD282-F79D-E011-9928-001D096B0F99.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/707F5AAB-FD9D-E011-9277-0015178C4A78.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/769084E1-EF9D-E011-8B1E-00266CFAE8D0.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/48FC3230-F19D-E011-9FF3-00266CFAE838.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/7A63A9DB-FE9D-E011-9CB3-0024E876A83B.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/5408C1EA-F99D-E011-96D2-0024E86E8D80.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/7C4EFDBA-FC9D-E011-BBF8-0024E8768D1A.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/6A2FC00C-F19D-E011-B18B-00A0D1EE26D0.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/90961476-F69D-E011-8A5C-00151796D45C.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/726172E6-F39D-E011-9BC0-0015178C1990.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/9AD97A96-FA9D-E011-AB5D-0024E86E8D25.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/78D6DFF6-F59D-E011-AFEE-0015178C4934.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/A43DC6A6-FE9D-E011-808A-0024E8768101.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/7A86E7E8-F49D-E011-BB7E-00A0D1EE8E94.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/A6EF9E1B-F39D-E011-8719-00266CF9B970.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/8A590AB9-F19D-E011-88D7-00A0D1EEA838.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/B6A3940F-F59D-E011-BA70-00A0D1EEF5B4.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/96B3F1B8-F49D-E011-91B2-00A0D1EE8ECC.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/C6436A46-F29D-E011-854A-00266CF2580C.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/A0B95F1F-ED9D-E011-ABA0-00A0D1EE25D0.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/C87D6C54-F19D-E011-BF7E-00266CF9BEF8.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/A480A569-F19D-E011-AEB2-00151796D874.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/D26DDCC1-F69D-E011-9EA0-0015178C4948.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/ACA21A89-F19D-E011-A7BA-00266CFAE1EC.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/DAA5854E-F49D-E011-ABC2-00A0D1EE8DFC.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/B89ECE90-FB9D-E011-A07B-0026B94E2899.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/E0B96C59-F29D-E011-BF2D-00266CF9AEA4.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/C6DE628F-F29D-E011-821C-00266CF27130.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/EAFE3FFF-F29D-E011-8925-00A0D1EE95AC.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/CC38CE35-F49D-E011-86C8-00A0D1EE8EE0.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/F8D9CB5C-F89D-E011-ADC1-00151796D8A0.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/D88C4EFA-FE9D-E011-9A2D-0024E876A83B.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/DE9A4FEC-F29D-E011-BA3E-00A0D1EE29B8.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/E40BB6AB-F19D-E011-B0FB-00266CF24EEC.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/F4513F7B-F29D-E011-AC5F-00266CF9B04C.root',
                  '/store/mc/Summer11/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau-100_7TeV-pythia6/GEN-SIM-RECODEBUG/PU_S4_START42_V11-v2/0000/FC36FCD8-FE9D-E011-8051-0024E8768446.root' ] );


secFiles.extend( [
                   ] )
