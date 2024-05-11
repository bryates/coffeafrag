import awkward as ak

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
