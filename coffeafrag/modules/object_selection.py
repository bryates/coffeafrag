'''
 objects.py
 This script contains several functions that implement the object selection according to different object definitions.
 The functions are called with (jagged)arrays as imputs and return a boolean mask.
'''

import numpy as np
import awkward as ak

from topcoffea.modules.get_param_from_jsons import GetParam
from topcoffea.modules.paths import topcoffea_path
from coffeafrag.modules.paths import coffeafrag_path
get_tc_param = GetParam(topcoffea_path("params/params.json"))
get_b_param = GetParam(coffeafrag_path("params/params.json"))

### These functions have been synchronized with ttH ###

def isPresTau(pt, eta, dxy, dz, idDeepTau2017v2p1VSjet, minpt=20.0):
    return  (pt>minpt)&(abs(eta)<get_b_param("eta_t_cut"))&(abs(dxy)<get_b_param("dxy_tau_cut"))&(abs(dz)<get_b_param("dz_tau_cut"))&(idDeepTau2017v2p1VSjet>>1 & 1 ==1)

def isVLooseTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>2 & 1)

def isLooseTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>3 & 1)

def isMediumTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>4 & 1)

def isTightTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>5 & 1)

def isVTightTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>6 & 1)

def isVVTightTau(idDeepTau2017v2p1VSjet):
    return (idDeepTau2017v2p1VSjet>>7 & 1)

def is_tight_jet(pt, eta, jet_id, pt_cut, eta_cut, id_cut):
    mask = ((pt>pt_cut) & (abs(eta)<eta_cut) & (jet_id>id_cut))
    return mask

def ttH_idEmu_cuts_E3(hoe, eta, deltaEtaSC, eInvMinusPInv, sieie):
    return (hoe<(0.10-0.00*(abs(eta+deltaEtaSC)>1.479))) & (eInvMinusPInv>-0.04) & (sieie<(0.011+0.019*(abs(eta+deltaEtaSC)>1.479)))

def smoothBFlav(jetpt,ptmin,ptmax,year,scale_loose=1.0):

    # Get the btag wp for the year
    if (year == "2016"):
        wploose  = get_tc_param("btag_wp_loose_UL16")
        wpmedium = get_tc_param("btag_wp_medium_UL16")
    elif (year == "2016APV"):
        wploose  = get_tc_param("btag_wp_loose_UL16APV")
        wpmedium = get_tc_param("btag_wp_medium_UL16APV")
    elif (year == "2017"):
        wploose  = get_tc_param("btag_wp_loose_UL17")
        wpmedium = get_tc_param("btag_wp_medium_UL17")
    elif (year == "2018"):
        wploose  = get_tc_param("btag_wp_loose_UL18")
        wpmedium = get_tc_param("btag_wp_medium_UL18")
    else:
        raise Exception(f"Error: Unknown year \"{year}\". Exiting...")

    x = np.minimum(np.maximum(0, jetpt - ptmin)/(ptmax-ptmin), 1.0)
    return x*wploose*scale_loose + (1-x)*wpmedium

def coneptElec(pt, mvaTTHUL, jetRelIso):
    conePt = (0.90 * pt * (1 + jetRelIso))
    return ak.where((mvaTTHUL>get_tc_param("mva_TTH_e_cut")),pt,conePt)

def coneptMuon(pt, mvaTTHUL, jetRelIso, mediumId):
    conePt = (0.90 * pt * (1 + jetRelIso))
    return ak.where(((mvaTTHUL>get_tc_param("mva_TTH_m_cut"))&(mediumId>0)),pt,conePt)

def isPresElec(pt, eta, dxy, dz, miniIso, sip3D, eleId):
    pt_mask    = (pt       > get_b_param("pres_e_pt_cut"))
    eta_mask   = (abs(eta) < get_b_param("eta_e_cut"))
    dxy_mask   = (abs(dxy) < get_b_param("dxy_cut"))
    dz_mask    = (abs(dz)  < get_b_param("dz_cut"))
    iso_mask   = (miniIso  < get_b_param("iso_cut"))
    sip3d_mask = (sip3D    < get_b_param("sip3d_cut"))
    return (pt_mask & eta_mask & dxy_mask & dz_mask & iso_mask & sip3d_mask & eleId)

def isPresMuon(dxy, dz, sip3D, eta, pt, miniRelIso):
    pt_mask    = (pt         > get_b_param("pres_m_pt_cut"))
    eta_mask   = (abs(eta)   < get_b_param("eta_m_cut"))
    dxy_mask   = (abs(dxy)   < get_b_param("dxy_cut"))
    dz_mask    = (abs(dz)    < get_b_param("dz_cut"))
    iso_mask   = (miniRelIso < get_b_param("iso_cut"))
    sip3d_mask = (sip3D      < get_b_param("sip3d_cut"))
    return (pt_mask & eta_mask & dxy_mask & dz_mask & iso_mask & sip3d_mask)

def isLooseElec(miniPFRelIso_all,sip3d,lostHits):
    return (miniPFRelIso_all<get_b_param("iso_cut")) & (sip3d<get_b_param("sip3d_cut")) & (lostHits<=1)

def isLooseMuon(miniPFRelIso_all,sip3d,looseId):
    return (miniPFRelIso_all<get_b_param("iso_cut")) & (sip3d<get_b_param("sip3d_cut")) & (looseId)

def isVetoMuon(mu):
    return mu.looseId & (mu.pt > get_b_param("loose_m_pt_cut")) & (abs(mu.eta) < get_b_param("eta_m_cut")) & (mu.jetRelIso < get_b_param("m_veto_iso_cut"))

def isVetoElec(ele):
    return (ele.cutBased == (1<<get_b_param("loose_e")))

def isTightMuon(mu):
    return mu.tightId & (mu.pt > get_b_param("tight_m_pt_cut")) & (abs(mu.eta) < get_b_param("eta_m_cut")) & (mu.jetRelIso < get_b_param("iso_cut"))

def isTightElec(ele):
    return (ele.cutBased >= (1<<get_b_param("tight_e")))  & (ele.pt > get_b_param("tight_e_pt_cut")) & (abs(ele.eta) < get_b_param("eta_e_cut")) & (ele.jetRelIso < get_b_param("iso_cut"))

def isFOElec(pt, conept, jetBTagDeepFlav, ttH_idEmu_cuts_E3, convVeto, lostHits, mvaTTHUL, jetRelIso, mvaFall17V2noIso_WP90, year):

    # Get the btag cut for the year
    if (year == "2016"):
        bTagCut = get_tc_param("btag_wp_medium_UL16")
    elif (year == "2016APV"):
        bTagCut = get_tc_param("btag_wp_medium_UL16APV")
    elif (year == "2017"):
        bTagCut = get_tc_param("btag_wp_medium_UL17")
    elif (year == "2018"):
        bTagCut = get_tc_param("btag_wp_medium_UL18")
    else:
        raise Exception(f"Error: Unknown year \"{year}\". Exiting...")

    btabReq    = (jetBTagDeepFlav<bTagCut)
    ptReq      = (conept>get_b_param("fo_pt_cut"))
    qualityReq = (ttH_idEmu_cuts_E3 & convVeto & (lostHits==0))
    mvaReq     = ((mvaTTHUL>get_tc_param("mva_TTH_e_cut")) | ((mvaFall17V2noIso_WP90) & (jetBTagDeepFlav<smoothBFlav(0.9*pt*(1+jetRelIso),20,45,year)) & (jetRelIso < get_b_param("fo_e_jetRelIso_cut"))))

    return ptReq & btabReq & qualityReq & mvaReq

def isFOMuon(pt, conept, jetBTagDeepFlav, mvaTTHUL, jetRelIso, year):

    # Get the btag cut for the year
    if (year == "2016"):
        bTagCut = get_tc_param("btag_wp_medium_UL16")
    elif (year == "2016APV"):
        bTagCut = get_tc_param("btag_wp_medium_UL16APV")
    elif (year == "2017"):
        bTagCut = get_tc_param("btag_wp_medium_UL17")
    elif (year == "2018"):
        bTagCut = get_tc_param("btag_wp_medium_UL18")
    else:
        raise Exception(f"Error: Unknown year \"{year}\". Exiting...")

    btagReq = (jetBTagDeepFlav<bTagCut)
    ptReq   = (conept>get_b_param("fo_pt_cut"))
    mvaReq  = ((mvaTTHUL>get_tc_param("mva_TTH_m_cut")) | ((jetBTagDeepFlav<smoothBFlav(0.9*pt*(1+jetRelIso),20,45,year)) & (jetRelIso < get_b_param("fo_m_jetRelIso_cut"))))
    return ptReq & btagReq & mvaReq

def tightSelElec(clean_and_FO_selection_TTH, mvaTTHUL):
    return (clean_and_FO_selection_TTH) & (mvaTTHUL > get_tc_param("mva_TTH_e_cut"))

def tightSelMuon(clean_and_FO_selection_TTH, mediumId, mvaTTHUL):
    return (clean_and_FO_selection_TTH) & (mediumId>0) & (mvaTTHUL > get_tc_param("mva_TTH_m_cut"))

def isClean(obj_A, obj_B, drmin=0.4):
    objB_near, objB_DR = obj_A.nearest(obj_B, return_metric=True)
    mask = ak.fill_none(objB_DR > drmin, True)
    return (mask)
