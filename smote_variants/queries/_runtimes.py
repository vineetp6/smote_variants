"""
This module contains some estimated runtimes for average imbalanced
datasets used for testing and evaluation.
"""

__all__ = ['runtimes']

runtimes = {
'NoSMOTE': 0.0001575469970703125,
'polynom_fit_SMOTE_bus': 0.00033428668975830076,
'polynom_fit_SMOTE_star': 0.00044138431549072265,
'ROSE': 0.00048253536224365237,
'Gazzah': 0.0009819984436035157,
'SPY': 0.0010293960571289063,
'MSMOTE': 0.0010655879974365234,
'AHC': 0.0011803627014160157,
'RWO_sampling': 0.0012227773666381836,
'polynom_fit_SMOTE_mesh': 0.0012503862380981445,
'polynom_fit_SMOTE_poly': 0.0013056278228759765,
'SMOTE': 0.0014549016952514649,
'Selected_SMOTE': 0.001479768753051758,
'NT_SMOTE': 0.0015209674835205077,
'G_SMOTE': 0.001589655876159668,
'Random_SMOTE': 0.0016499996185302735,
'Safe_Level_SMOTE': 0.00169680118560791,
'Gaussian_SMOTE': 0.0018160581588745118,
'MCT': 0.001826310157775879,
'Borderline_SMOTE1': 0.0020763397216796873,
'CURE_SMOTE': 0.002085232734680176,
'Borderline_SMOTE2': 0.0021561145782470702,
'Edge_Det_SMOTE': 0.002244853973388672,
'SMOTE_OUT': 0.0023625850677490234,
'CCR': 0.002711176872253418,
'SMOTE_Cosine': 0.0028854131698608397,
'SL_graph_SMOTE': 0.0030184030532836915,
'SMMO': 0.003188467025756836,
'distance_SMOTE': 0.003262615203857422,
'CBSO': 0.0035253286361694334,
'Lee': 0.0036804676055908203,
'SMOTE_TomekLinks': 0.0037401437759399412,
'SMOTE_D': 0.0038565874099731447,
'SMOTE_RSB': 0.004146575927734375,
'Assembled_SMOTE': 0.0043058633804321286,
'NDO_sampling': 0.004311156272888183,
'PDFOS': 0.004357147216796875,
'OUPS': 0.004824352264404297,
'NRAS': 0.0050504207611083984,
'ISMOTE': 0.005362510681152344,
'SMOBD': 0.00565187931060791,
'Stefanowski': 0.005956506729125977,
'ANS': 0.00623626708984375,
'LN_SMOTE': 0.006256961822509765,
'SN_SMOTE': 0.0065546751022338865,
'AND_SMOTE': 0.007062482833862305,
'TRIM_SMOTE': 0.00791945457458496,
'MDO': 0.009374117851257325,
'SYMPROD': 0.009868478775024414,
'cluster_SMOTE': 0.011855554580688477,
'SOI_CJ': 0.012188553810119629,
'SMOTE_ENN': 0.012231278419494628,
'SOMO': 0.012856888771057128,
'SUNDO': 0.013146662712097168,
'SMOTE_FRST_2T': 0.014063835144042969,
'ASMOBD': 0.01421060562133789,
'VIS_RST': 0.016105914115905763,
'DBSMOTE': 0.016603636741638183,
'ADASYN': 0.023564982414245605,
'V_SYNTH': 0.025472474098205567,
'SMOTE_IPF': 0.029655957221984865,
'MWMOTE': 0.0335747241973877,
'kmeans_SMOTE': 0.034969449043273926,
'ProWSyn': 0.03614718914031982,
'MSYN': 0.03970990180969238,
'NEATER': 0.04637973308563233,
'LLE_SMOTE': 0.04672214984893799,
'SVM_balance': 0.049683642387390134,
'NRSBoundary_SMOTE': 0.05426912307739258,
'SDSMOTE': 0.06174941062927246,
'DE_oversampling': 0.07008554935455322,
'Supervised_SMOTE': 0.07257795333862305,
'ISOMAP_Hybrid': 0.0780186653137207,
'LVQ_SMOTE': 0.09743821620941162,
'ADOMS': 0.0985065221786499,
'KernelADASYN': 0.1399752378463745,
'SSO': 0.1672980308532715,
'CE_SMOTE': 0.1770571231842041,
'E_SMOTE': 0.17706725597381592,
'MOT2LD': 0.23347222805023193,
'A_SUWO': 0.35372257232666016,
'DSMOTE': 0.5619288682937622,
'GASMOTE': 0.7379563808441162,
'SMOTE_PSOBAT': 0.83712158203125,
'IPADE_ID': 2.19421124458313,
'DEAGO': 2.9683846950531008,
'SMOTE_PSO': 3.2347741603851317,
'ADG': 4.425517630577088,
'AMSCO': 18.11877920627594,
'DSRBF': 24.86799850463867
}
