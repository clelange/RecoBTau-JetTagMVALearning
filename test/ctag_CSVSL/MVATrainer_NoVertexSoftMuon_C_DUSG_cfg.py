import FWCore.ParameterSet.Config as cms

process = cms.Process("IPTrainer")

process.source = cms.Source("EmptySource")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.combinedSVTrainer = cms.EDAnalyzer("JetTagMVATreeTrainer",
	useCategories		= cms.bool(False),
	calibrationRecord	= cms.string("CombinedSVNoVertexSoftMuon"),
	ignoreFlavours		= cms.vint32(0, 5, 7),
	signalFlavours		= cms.vint32(4),
	minimumTransverseMomentum = cms.double(15.0),
	minimumPseudoRapidity	= cms.double(0),
	maximumPseudoRapidity	= cms.double(2.5),

	factor = cms.double(1),
	bound = cms.double(50),

	fileNames = cms.vstring(
		"/user/pvmulder/NewEraOfDataAnalysis/BTagServiceWork/DEVELOPMENT/RootFiles_CSVSLIVF_JetFlavourPUjetIDcleanIVF/QCD_training/skimmed_20k_eachptetabin_CombinedSVNoVertexSoftMuon_C.root",
		"/user/pvmulder/NewEraOfDataAnalysis/BTagServiceWork/DEVELOPMENT/RootFiles_CSVSLIVF_JetFlavourPUjetIDcleanIVF/QCD_training/skimmed_20k_eachptetabin_CombinedSVNoVertexSoftMuon_DUSG.root"
	),
	weightFile = cms.string("weights/CombinedSVNoVertexSoftMuon_CDUSG_histo.txt"),
	biasFiles = cms.vstring(
		"*",
		"-",
		"weights/CombinedSVNoVertexSoftMuon_C_DUSG_ratio.txt"
	)
)

process.looper = cms.Looper("JetTagMVATrainerLooper",
	trainers = cms.VPSet(
		cms.PSet(
			calibrationRecord = cms.string("CombinedSVNoVertexSoftMuon"),
			trainDescription = cms.untracked.string("Save_NoVertexSoftMuon_C_DUSG.xml"),
			loadState = cms.untracked.bool(False),
			saveState = cms.untracked.bool(False)
		)
	)
)

process.p = cms.Path(process.combinedSVTrainer)
