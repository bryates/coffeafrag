import awkward as ak


# The datasets we are using, and the triggers in them
dataset_dict_top22006 = {
    "2016" : {
        "SingleMuon" : [
            "IsoMu24",
            "IsoTkMu24",
            "IsoMu22_eta2p1",
            "IsoTkMu22_eta2p1",
            "IsoMu22",
            "IsoTkMu22",
            "IsoMu27",
        ],
        "SingleElectron" : [
            'Ele27_WPTight_Gsf',
            "Ele25_eta2p1_WPTight_Gsf",
            "Ele27_eta2p1_WPLoose_Gsf",
        ],
        "DoubleMuon" : [
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",
            "Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",
            "Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",
            "TripleMu_12_10_5",
        ],
        "DoubleEG" : [
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Ele16_Ele12_Ele8_CaloIdL_TrackIdL",
        ],
        "MuonEG" : [
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",
            "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",
            "Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_DiEle12_CaloIdL_TrackIdL",
            "DiMu9_Ele9_CaloIdL_TrackIdL",
        ]
    },

    "2017" : {
        "SingleMuon" : [
            "IsoMu24",
            "IsoMu27",
        ],
        "SingleElectron" : [
            "Ele32_WPTight_Gsf",
            "Ele35_WPTight_Gsf",
        ],
        "DoubleMuon" : [
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8",
            "TripleMu_12_10_5",
        ],
        "DoubleEG" : [
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Ele16_Ele12_Ele8_CaloIdL_TrackIdL",
        ],
        "MuonEG" : [
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_DiEle12_CaloIdL_TrackIdL",
            "Mu8_DiEle12_CaloIdL_TrackIdL_DZ", # Note: Listed in Andrew's thesis, but not TOP-19-001 AN
            "DiMu9_Ele9_CaloIdL_TrackIdL_DZ",
        ]
    },

    "2018" : {
        "SingleMuon" : [
            "IsoMu24",
            "IsoMu27",
        ],
        "EGamma" : [
            "Ele32_WPTight_Gsf",
            "Ele35_WPTight_Gsf",
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Ele16_Ele12_Ele8_CaloIdL_TrackIdL",
        ],
        "DoubleMuon" : [
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
            "Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8",
            "TripleMu_12_10_5",
        ],
        "MuonEG" : [
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",
            "Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",
            "Mu8_DiEle12_CaloIdL_TrackIdL",
            "Mu8_DiEle12_CaloIdL_TrackIdL_DZ",
            "DiMu9_Ele9_CaloIdL_TrackIdL_DZ",
        ]
    }
}

# Hard coded dictionary for figuring out overlap...
#   - No unique way to do this
#   - Note: In order for this to work properly, you should be processing all of the datastes to be used in the analysis
#   - Otherwise, you may be removing events that show up in other datasets you're not using
exclude_dict_top22006 = {
    "2016": {
        "DoubleMuon"     : [],
        "DoubleEG"       : dataset_dict_top22006["2016"]["DoubleMuon"],
        "MuonEG"         : dataset_dict_top22006["2016"]["DoubleMuon"] + dataset_dict_top22006["2016"]["DoubleEG"],
        "SingleMuon"     : dataset_dict_top22006["2016"]["DoubleMuon"] + dataset_dict_top22006["2016"]["DoubleEG"] + dataset_dict_top22006["2016"]["MuonEG"],
        "SingleElectron" : dataset_dict_top22006["2016"]["DoubleMuon"] + dataset_dict_top22006["2016"]["DoubleEG"] + dataset_dict_top22006["2016"]["MuonEG"] + dataset_dict_top22006["2016"]["SingleMuon"],
    },
    "2017": {
        "DoubleMuon"     : [],
        "DoubleEG"       : dataset_dict_top22006["2017"]["DoubleMuon"],
        "MuonEG"         : dataset_dict_top22006["2017"]["DoubleMuon"] + dataset_dict_top22006["2017"]["DoubleEG"],
        "SingleMuon"     : dataset_dict_top22006["2017"]["DoubleMuon"] + dataset_dict_top22006["2017"]["DoubleEG"] + dataset_dict_top22006["2017"]["MuonEG"],
        "SingleElectron" : dataset_dict_top22006["2017"]["DoubleMuon"] + dataset_dict_top22006["2017"]["DoubleEG"] + dataset_dict_top22006["2017"]["MuonEG"] + dataset_dict_top22006["2017"]["SingleMuon"],
    },
    "2018": {
        "DoubleMuon"     : [],
        "EGamma"         : dataset_dict_top22006["2018"]["DoubleMuon"],
        "MuonEG"         : dataset_dict_top22006["2018"]["DoubleMuon"] + dataset_dict_top22006["2018"]["EGamma"],
        "SingleMuon"     : dataset_dict_top22006["2018"]["DoubleMuon"] + dataset_dict_top22006["2018"]["EGamma"] + dataset_dict_top22006["2018"]["MuonEG"],
    },
}

def add1lMaskAndSFs(events, year, isData, sampleType):

    # lep and padded lep
    lep = events.leptons
    padded_lep = ak.pad_none(lep,1)

    # Filters and cleanups
    filter_flags = events.Flag
    filters = filter_flags.goodVertices & filter_flags.globalSuperTightHalo2016Filter & filter_flags.HBHENoiseFilter & filter_flags.HBHENoiseIsoFilter & filter_flags.EcalDeadCellTriggerPrimitiveFilter & filter_flags.BadPFMuonFilter & (((year == "2016")|(year == "2016APV")) | filter_flags.ecalBadCalibFilter) & (isData | filter_flags.eeBadScFilter)
    mask = filters
    #cleanup = events.minMllAFAS > 12
    #muTightCharge = ((abs(padded_lep[:,0].pdgId)!=13) | (padded_lep[:,0].tightCharge>=1))

    ## IDs
    #eleID1 = (abs(padded_lep[:,0].pdgId)!=11)

    ## 1l requirements:
    #exclusive = ak.num( lep,axis=-1)<2
    #semilep = (ak.num(lep)) >= 1
    #pt25 = (ak.any(ak.firsts(lep.pt) > 25.0, axis=1))
    #mask = (filters & cleanup & semilep & pt25 & exclusive & eleID1 & muTightCharge)

    ## MC matching requirement (already passed for data)
    #if sampleType == "data":
    #    pass
    #else:
    #    lep1_match_prompt = ((padded_lep[:,0].genPartFlav==1) | (padded_lep[:,0].genPartFlav == 15))
    #    lep1_charge       = ((padded_lep[:,0].gen_pdgId*padded_lep[:,0].pdgId) > 0)
    #    lep1_match_conv   = (padded_lep[:,0].genPartFlav==22)
    #    prompt_mask = ( lep1_match_prompt & lep1_charge)
    #    conv_mask   = ( lep1_match_conv)
    #    if sampleType == 'prompt':
    #        mask = (mask & prompt_mask)
    #    elif sampleType =='conversions':
    #        mask = (mask & conv_mask)
    #    elif sampleType =='prompt_and_conversions':
    #        # Samples that we use for both prompt and conv contributions (i.e. just DY)
    #        mask = (mask & (prompt_mask | conv_mask))
    #    else:
    #        raise Exception(f"Error: Unknown sampleType {sampleType}.")

    #mask_nozeeveto = mask
    events['is1l'] = ak.fill_none(mask,False)
    #events['is1l_nozeeveto'] = ak.fill_none(mask_nozeeveto,False)

    # SFs
    events['sf_1l_muon'] = padded_lep[:,0].sf_nom_1l_muon
    events['sf_1l_elec'] = padded_lep[:,0].sf_nom_2l_elec
    events['sf_1l_hi_muon'] = padded_lep[:,0].sf_hi_1l_muon
    events['sf_1l_hi_elec'] = padded_lep[:,0].sf_hi_2l_elec
