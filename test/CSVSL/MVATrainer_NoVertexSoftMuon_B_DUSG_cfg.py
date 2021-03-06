import FWCore.ParameterSet.Config as cms

process = cms.Process("IPTrainer")

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.combinedSVTrainer = cms.EDAnalyzer("JetTagMVATreeTrainer",
	useCategories		= cms.bool(False),
	calibrationRecord	= cms.string("CombinedSVNoVertexSoftMuon"),
	ignoreFlavours		= cms.vint32(0, 4),
	signalFlavours		= cms.vint32(5, 7),
	minimumTransverseMomentum = cms.double(15.0),
	minimumPseudoRapidity	= cms.double(0),
	maximumPseudoRapidity	= cms.double(2.5),

	factor = cms.double(1),
	bound = cms.double(50),

	fileNames = cms.vstring(
		"/user/pvmulder/NewEraOfDataAnalysis/BTagServiceWork/DEVELOPMENT/SuperTaggerDev/CMSSW_5_3_14/src/RootFiles/SkimmedRootFiles/skimmed_max20k_eachptetabin_CombinedSVNoVertexSoftMuon_B.root",
		"/user/pvmulder/NewEraOfDataAnalysis/BTagServiceWork/DEVELOPMENT/SuperTaggerDev/CMSSW_5_3_14/src/RootFiles/SkimmedRootFiles/skimmed_max20k_eachptetabin_CombinedSVNoVertexSoftMuon_DUSG.root"
	),
	weightFile = cms.string("weights/CombinedSVNoVertexSoftMuon_BDUSG_histo.txt"),
	biasFiles = cms.vstring(
		"*",
		"-",
		"weights/CombinedSVNoVertexSoftMuon_B_DUSG_ratio.txt"
	)
)

process.looper = cms.Looper("JetTagMVATrainerLooper",
	trainers = cms.VPSet(
		cms.PSet(
			calibrationRecord = cms.string("CombinedSVNoVertexSoftMuon"),
			trainDescription = cms.untracked.string("Save_NoVertexSoftMuon_B_DUSG.xml"),
			loadState = cms.untracked.bool(False),
			saveState = cms.untracked.bool(False)
		)
	)
)

process.p = cms.Path(process.combinedSVTrainer)
