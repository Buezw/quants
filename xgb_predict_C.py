def xgb_predict(features):
    score = 0.0

    # Tree 0
    def t0(features):
if features[19] < -1.8618742:
            if features[1] < 0.008460388:
                if features[13] < 113.36628:
                    return 9.4962146e-05
                else:
                    return 0.0011954226
            else:
                if features[18] < 47.415623:
                    return 0.00019176766
                else:
                    return -0.0010414862
        else:
            if features[1] < -0.01671769:
                if features[0] < 102.33519:
                    return 0.00029393015
                else:
                    return -0.0006175923
            else:
                if features[2] < -0.06625256:
                    return 0.0012174712
                else:
                    return 6.2325635e-06
        
    score += t0(features)

    # Tree 1
    def t1(features):
if features[20] < -2.3502882:
            if features[5] < 6.1726336:
                if features[16] < 0.9718254:
                    return 0.0010123982
                else:
                    return -0.0004532719
            else:
                return 0.0019549828
        else:
            if features[14] < 1.4365085:
                if features[21] < 0.6547846:
                    return 2.2748436e-05
                else:
                    return 0.00073172146
            else:
                if features[15] < 1.8650908:
                    return 0.0002514049
                else:
                    return -0.00027363037
        
    score += t1(features)

    # Tree 2
    def t2(features):
if features[21] < -0.75020987:
            if features[7] < 136.16093:
                if features[19] < -2.0442295:
                    return -0.00014524137
                else:
                    return -0.0010002264
            else:
                if features[7] < 139.05667:
                    return 0.0010829576
                else:
                    return -0.00021491633
        else:
            if features[19] < -2.8859918:
                if features[16] < 0.9718254:
                    return 0.0014592278
                else:
                    return -0.00048483154
            else:
                if features[10] < 188.00276:
                    return 1.925208e-05
                else:
                    return -0.0019711978
        
    score += t2(features)

    # Tree 3
    def t3(features):
if features[3] < -4.897208:
            if features[14] < 4.3378897:
                if features[18] < 37.83284:
                    return 2.2079732e-05
                else:
                    return -0.0013748746
            else:
                return 0.0010983817
        else:
            if features[17] < -1.5617101:
                if features[6] < -0.056526996:
                    return 0.00014787437
                else:
                    return -0.0018709687
            else:
                if features[19] < -1.8618742:
                    return 0.0003996126
                else:
                    return 7.6965825e-06
        
    score += t3(features)

    # Tree 4
    def t4(features):
if features[4] < 1.6370435:
            if features[21] < 0.46038336:
                if features[19] < -1.9097137:
                    return 0.00034312694
                else:
                    return -9.3096685e-05
            else:
                if features[20] < -1.1081516:
                    return -0.0016069998
                else:
                    return -0.0004649044
        else:
            if features[3] < 5.302454:
                if features[15] < 3.0103276:
                    return 8.044236e-05
                else:
                    return 0.00054314197
            else:
                if features[14] < 3.0399985:
                    return -0.0012924442
                else:
                    return 0.00017415633
        
    score += t4(features)

    # Tree 5
    def t5(features):
if features[17] < 0.94305867:
            if features[0] < 143.2167:
                if features[19] < 2.520104:
                    return 4.8299884e-05
                else:
                    return -0.0005177708
            else:
                if features[7] < 141.80888:
                    return 0.0017691031
                else:
                    return -0.00036632852
        else:
            if features[14] < 1.6088493:
                if features[17] < 1.6787297:
                    return 0.0010458723
                else:
                    return -0.00036005318
            else:
                if features[18] < 54.502678:
                    return -0.0010388352
                else:
                    return 0.00016707077
        
    score += t5(features)

    # Tree 6
    def t6(features):
if features[3] < 5.302454:
            if features[16] < 1.468351:
                if features[17] < -1.278247:
                    return -0.0006064742
                else:
                    return 3.6014902e-05
            else:
                if features[16] < 1.723698:
                    return 0.0014099751
                else:
                    return -0.00019481736
        else:
            if features[22] < 1.0678096:
                if features[2] < 0.07310474:
                    return -0.0011475163
                else:
                    return 0.00033032335
            else:
                if features[22] < 1.1240728:
                    return 0.0020461883
                else:
                    return -9.238752e-05
        
    score += t6(features)

    # Tree 7
    def t7(features):
if features[17] < 0.94305867:
            if features[7] < 68.34626:
                if features[3] < 1.0228416:
                    return 0.00060803833
                else:
                    return -0.0006029037
            else:
                if features[19] < -1.9097137:
                    return 0.00025661843
                else:
                    return -6.84222e-05
        else:
            if features[1] < 0.003010688:
                if features[21] < 0.848463:
                    return 0.0012670119
                else:
                    return 0.00016801711
            else:
                if features[19] < 5.856989:
                    return 0.00017865175
                else:
                    return -0.0009094045
        
    score += t7(features)

    # Tree 8
    def t8(features):
if features[19] < -2.6290972:
            if features[5] < -9.594737:
                if features[16] < -0.9410391:
                    return 0.00057695055
                else:
                    return -0.000707907
            else:
                if features[1] < 0.004706974:
                    return 0.0017549383
                else:
                    return 0.00033459582
        else:
            if features[17] < -1.5071751:
                if features[19] < -1.4018866:
                    return -0.0015193146
                else:
                    return -0.00019726001
            else:
                if features[14] < 0.28486788:
                    return -0.0005297924
                else:
                    return 3.1243024e-05
        
    score += t8(features)

    # Tree 9
    def t9(features):
if features[17] < -1.5617101:
            if features[2] < -0.06625256:
                if features[2] < -0.07117485:
                    return -5.3145555e-05
                else:
                    return -0.00033297602
            else:
                return -0.0015805569
        else:
            if features[3] < 5.302454:
                if features[16] < 1.3532116:
                    return 1.46412e-05
                else:
                    return 0.0007839485
            else:
                if features[3] < 6.692965:
                    return -0.00083508476
                else:
                    return 0.00016234936
        
    score += t9(features)

    # Tree 10
    def t10(features):
if features[17] < 0.94305867:
            if features[17] < 0.88934964:
                if features[10] < 147.06465:
                    return 3.5464935e-05
                else:
                    return -0.00030343697
            else:
                if features[2] < 0.07310474:
                    return -0.0011385333
                else:
                    return 0.0003622905
        else:
            if features[2] < 0.025397226:
                if features[18] < 65.5284:
                    return 0.0016616291
                else:
                    return 0.0005702655
            else:
                if features[5] < 9.917799:
                    return 0.00051315175
                else:
                    return -0.00021854237
        
    score += t10(features)

    # Tree 11
    def t11(features):
if features[14] < 1.4365085:
            if features[15] < 1.1833668:
                if features[5] < 1.970656:
                    return 8.085392e-06
                else:
                    return -0.0004697119
            else:
                if features[2] < 0.013568837:
                    return 9.5424686e-05
                else:
                    return 0.00048831245
        else:
            if features[15] < 1.8227913:
                if features[17] < -0.08449134:
                    return 0.0010825284
                else:
                    return -3.2040956e-05
            else:
                if features[18] < 33.96698:
                    return 0.00055222766
                else:
                    return -0.00023320728
        
    score += t11(features)

    # Tree 12
    def t12(features):
if features[3] < -2.7649167:
            if features[4] < -10.940355:
                return 0.0016495837
            else:
                if features[19] < -1.7430431:
                    return 0.00041533142
                else:
                    return -0.0004758339
        else:
            if features[17] < -1.2189687:
                if features[19] < -1.0625672:
                    return -0.0011044597
                else:
                    return 0.00017896848
            else:
                if features[2] < -0.044455513:
                    return 0.0011653024
                else:
                    return 5.765835e-05
        
    score += t12(features)

    # Tree 13
    def t13(features):
if features[15] < 3.472663:
            if features[16] < -1.3823837:
                if features[21] < -0.1435853:
                    return -0.0010412146
                else:
                    return 0.00067937834
            else:
                if features[1] < -0.015842654:
                    return -0.0003463195
                else:
                    return 8.126643e-06
        else:
            if features[17] < -1.2189687:
                if features[3] < -2.494241:
                    return 0.0002246283
                else:
                    return -0.00073848927
            else:
                if features[3] < 5.4135246:
                    return 0.0006313588
                else:
                    return -0.00030556865
        
    score += t13(features)

    # Tree 14
    def t14(features):
if features[5] < 14.98618:
            if features[18] < 30.9627:
                if features[2] < -0.069616474:
                    return -0.00024163474
                else:
                    return 0.0007362689
            else:
                if features[17] < -1.5617101:
                    return -0.0010814433
                else:
                    return -1.15744415e-05
        else:
            if features[2] < 0.06127615:
                if features[17] < 1.0420717:
                    return 0.0002816057
                else:
                    return 0.0012041281
            else:
                if features[0] < 156.75044:
                    return 0.0006153787
                else:
                    return -0.0004076281
        
    score += t14(features)

    # Tree 15
    def t15(features):
if features[17] < 0.9682741:
            if features[0] < 143.2167:
                if features[9] < 139.93419:
                    return -2.207455e-05
                else:
                    return 0.00047252473
            else:
                if features[0] < 166.59955:
                    return -0.00039470987
                else:
                    return 0.0003735704
        else:
            if features[17] < 1.0080223:
                if features[1] < 0.0016684553:
                    return 0.0017707403
                else:
                    return 0.00047859453
            else:
                if features[21] < 0.9198338:
                    return 0.00049163116
                else:
                    return -0.00017339725
        
    score += t15(features)

    # Tree 16
    def t16(features):
if features[2] < -0.018705226:
            if features[16] < -2.4385195:
                if features[1] < -0.02198468:
                    return 8.659167e-05
                else:
                    return 0.0013418428
            else:
                if features[3] < -4.897208:
                    return -0.0007049266
                else:
                    return -0.00016699458
        else:
            if features[2] < -0.0083903335:
                if features[16] < 0.29738408:
                    return 0.00029112748
                else:
                    return 0.0015587247
            else:
                if features[16] < -0.8812417:
                    return -0.001356348
                else:
                    return -1.5836102e-05
        
    score += t16(features)

    # Tree 17
    def t17(features):
if features[18] < 85.162056:
            if features[6] < 0.025683863:
                if features[4] < 3.3466554:
                    return -3.6826237e-05
                else:
                    return -0.00084314786
            else:
                if features[17] < 0.08074977:
                    return 0.0009201405
                else:
                    return 0.000120659824
        else:
            if features[7] < 124.40748:
                return -0.00032839642
            else:
                return -0.0018294583
        
    score += t17(features)

    # Tree 18
    def t18(features):
if features[3] < 5.4135246:
            if features[3] < 5.2446837:
                if features[22] < 1.0513464:
                    return 2.9329127e-05
                else:
                    return -0.00042510522
            else:
                if features[20] < 2.1130915:
                    return 0.00019651453
                else:
                    return 0.0015941743
        else:
            if features[15] < 2.4027753:
                if features[4] < 6.4130316:
                    return -0.0014331964
                else:
                    return -2.6602473e-05
            else:
                if features[12] < 142.46315:
                    return -0.00081601087
                else:
                    return 9.653356e-05
        
    score += t18(features)

    # Tree 19
    def t19(features):
if features[17] < 0.9682741:
            if features[17] < 0.57530415:
                if features[4] < 3.9652104:
                    return -7.868351e-06
                else:
                    return 0.0004328217
            else:
                if features[1] < 0.012197236:
                    return -0.00012589832
                else:
                    return -0.0008414021
        else:
            if features[17] < 1.0080223:
                if features[1] < 0.0016684553:
                    return 0.0018115044
                else:
                    return 0.00040096696
            else:
                if features[17] < 1.5861769:
                    return 0.00028514012
                else:
                    return -0.00045667074
        
    score += t19(features)

    # Tree 20
    def t20(features):
if features[18] < 73.17508:
            if features[18] < 66.82742:
                if features[18] < 66.672035:
                    return -1.1963595e-05
                else:
                    return 0.0015111592
            else:
                if features[17] < 0.26950166:
                    return -0.0011148357
                else:
                    return -0.00023538391
        else:
            if features[2] < 0.06127615:
                if features[16] < 0.9337261:
                    return 8.714685e-05
                else:
                    return 0.000841469
            else:
                if features[18] < 75.4453:
                    return 0.00017380265
                else:
                    return -0.0006040074
        
    score += t20(features)

    # Tree 21
    def t21(features):
if features[14] < 1.4209665:
            if features[7] < 99.69595:
                if features[7] < 69.05771:
                    return 0.00036725015
                else:
                    return -0.00014419609
            else:
                if features[1] < -0.0094424:
                    return -0.0004351603
                else:
                    return 0.00031972548
        else:
            if features[14] < 2.4301841:
                if features[0] < 154.70668:
                    return -0.00015907054
                else:
                    return -0.00076963904
            else:
                if features[5] < 1.837702:
                    return -0.00022466372
                else:
                    return 0.00033809137
        
    score += t21(features)

    # Tree 22
    def t22(features):
if features[19] < -1.9362855:
            if features[0] < 130.32587:
                if features[14] < 1.1465296:
                    return 0.0006161003
                else:
                    return -7.310305e-05
            else:
                if features[21] < -0.98111266:
                    return -0.0006132913
                else:
                    return 0.0014946869
        else:
            if features[4] < -10.940355:
                return 0.0014059494
            else:
                if features[16] < -1.7395669:
                    return -0.00064525864
                else:
                    return -1.3281011e-05
        
    score += t22(features)

    # Tree 23
    def t23(features):
if features[19] < -2.8859918:
            if features[14] < 1.1394504:
                return 0.0016924419
            else:
                if features[19] < -3.3554604:
                    return -0.00024438012
                else:
                    return 0.0008458063
        else:
            if features[17] < -1.5617101:
                if features[0] < 110.36323:
                    return -8.2337785e-05
                else:
                    return -0.0013115031
            else:
                if features[17] < -0.8189923:
                    return 0.00033237576
                else:
                    return -1.0915987e-05
        
    score += t23(features)

    # Tree 24
    def t24(features):
if features[18] < 85.162056:
            if features[2] < -0.018705226:
                if features[22] < 0.08369433:
                    return -8.685604e-05
                else:
                    return -0.00082529674
            else:
                if features[2] < -0.0083903335:
                    return 0.00038393828
                else:
                    return 1.6757902e-05
        else:
            if features[7] < 124.40748:
                return -0.00031049814
            else:
                return -0.0016930978
        
    score += t24(features)

    # Tree 25
    def t25(features):
if features[3] < 5.302454:
            if features[16] < -2.2186184:
                if features[5] < -4.809034:
                    return 0.0009820138
                else:
                    return -0.00037086912
            else:
                if features[2] < 0.028730493:
                    return -4.12724e-05
                else:
                    return 0.00018680531
        else:
            if features[3] < 6.692965:
                if features[7] < 140.34889:
                    return -0.0001348354
                else:
                    return -0.0011756421
            else:
                if features[17] < -0.09527352:
                    return 0.0017695809
                else:
                    return 2.2308426e-05
        
    score += t25(features)

    # Tree 26
    def t26(features):
if features[21] < -0.75020987:
            if features[1] < 0.017020065:
                if features[21] < -1.6229664:
                    return 0.00045440617
                else:
                    return -0.00029945053
            else:
                if features[2] < -0.069616474:
                    return -0.00030100366
                else:
                    return -0.0018463185
        else:
            if features[1] < -0.029749539:
                if features[0] < 142.42253:
                    return 0.001669232
                else:
                    return -0.00012751078
            else:
                if features[20] < -2.3502882:
                    return 0.0006857013
                else:
                    return 1.9015748e-05
        
    score += t26(features)

    # Tree 27
    def t27(features):
if features[21] < -1.1737256:
            if features[3] < -1.6204301:
                if features[15] < 3.0103276:
                    return -0.0012045961
                else:
                    return 0.0002104231
            else:
                if features[5] < -4.6107483:
                    return -0.001330864
                else:
                    return -9.110955e-05
        else:
            if features[5] < -0.71565056:
                if features[22] < 0.24258949:
                    return 0.000111751164
                else:
                    return 0.0012281585
            else:
                if features[5] < -0.2367298:
                    return -0.00051111355
                else:
                    return -3.738002e-06
        
    score += t27(features)

    # Tree 28
    def t28(features):
if features[19] < -1.9362855:
            if features[7] < 128.12526:
                if features[19] < -2.1701863:
                    return -7.8719015e-05
                else:
                    return 0.0008794752
            else:
                if features[0] < 143.07297:
                    return 0.0012763597
                else:
                    return -0.0001063284
        else:
            if features[15] < 1.9504019:
                if features[19] < -1.761641:
                    return -0.0012831531
                else:
                    return 4.7907623e-05
            else:
                if features[7] < 135.55664:
                    return -0.00035476006
                else:
                    return -1.1853024e-05
        
    score += t28(features)

    # Tree 29
    def t29(features):
if features[22] < -0.5337389:
            if features[5] < -5.6155634:
                if features[3] < -0.38472548:
                    return 0.00016469111
                else:
                    return -0.001025732
            else:
                if features[16] < -1.0331678:
                    return -0.0011941222
                else:
                    return -0.00018417065
        else:
            if features[2] < -0.0083903335:
                if features[17] < -0.0824262:
                    return 0.0005656054
                else:
                    return 1.0049013e-05
            else:
                if features[5] < -4.6107483:
                    return -0.00072007114
                else:
                    return 4.2283147e-05
        
    score += t29(features)

    # Tree 30
    def t30(features):
if features[1] < -0.029749539:
            if features[2] < 0.0045234:
                if features[3] < -5.2921133:
                    return 2.1767895e-05
                else:
                    return 0.0015711355
            else:
                if features[1] < -0.031180533:
                    return -0.00012246984
                else:
                    return -0.0006566485
        else:
            if features[3] < -7.7122164:
                if features[15] < 3.183968:
                    return -0.0014616736
                else:
                    return -9.1585636e-05
            else:
                if features[3] < -4.366919:
                    return 0.000368972
                else:
                    return -4.3998866e-06
        
    score += t30(features)

    # Tree 31
    def t31(features):
if features[7] < 68.34626:
            if features[18] < 66.672035:
                if features[2] < 0.004176751:
                    return 0.00036376386
                else:
                    return 0.0010934909
            else:
                if features[1] < 0.009099994:
                    return -7.19385e-05
                else:
                    return -0.0008813414
        else:
            if features[15] < 0.84264493:
                if features[19] < 0.61754775:
                    return -8.166895e-05
                else:
                    return -0.0007185479
            else:
                if features[22] < -0.59010386:
                    return -0.00015944996
                else:
                    return 5.5458946e-05
        
    score += t31(features)

    # Tree 32
    def t32(features):
if features[21] < -1.6229664:
            if features[7] < 111.406845:
                if features[0] < 107.95296:
                    return -5.1765564e-05
                else:
                    return -0.0003188684
            else:
                if features[15] < 4.7804875:
                    return 0.0011648234
                else:
                    return 0.00028792067
        else:
            if features[21] < -1.1973152:
                if features[19] < 1.7088028:
                    return -0.00077108806
                else:
                    return 0.00040231683
            else:
                if features[5] < -0.71565056:
                    return 0.00010569696
                else:
                    return -6.118445e-05
        
    score += t32(features)

    # Tree 33
    def t33(features):
if features[16] < 1.1368798:
            if features[4] < 3.0483036:
                if features[4] < 2.5148482:
                    return 7.696128e-06
                else:
                    return -0.00062938186
            else:
                if features[17] < -0.032316715:
                    return 0.0016674607
                else:
                    return 0.00024466708
        else:
            if features[2] < 0.032798145:
                if features[2] < 0.016549623:
                    return -0.00018570623
                else:
                    return -0.001478881
            else:
                if features[1] < 0.0032520578:
                    return 0.0009854545
                else:
                    return -0.00033096396
        
    score += t33(features)

    # Tree 34
    def t34(features):
if features[3] < -4.897208:
            if features[18] < 37.83284:
                if features[17] < -0.96485347:
                    return -0.00027194156
                else:
                    return 0.00090439216
            else:
                if features[19] < 1.1850767:
                    return -0.0011787303
                else:
                    return 5.715192e-05
        else:
            if features[3] < -4.614019:
                if features[1] < -0.005042709:
                    return 0.0015015884
                else:
                    return -0.0006863403
            else:
                if features[1] < -0.01671769:
                    return -0.00031466663
                else:
                    return 1.6721997e-05
        
    score += t34(features)

    # Tree 35
    def t35(features):
if features[21] < -1.8185312:
            return 0.0010236623
        else:
            if features[3] < -4.897208:
                if features[14] < 2.2469232:
                    return 0.0005757468
                else:
                    return -0.0005978301
            else:
                if features[3] < -4.366919:
                    return 0.0007491848
                else:
                    return -2.513545e-05
        
    score += t35(features)

    # Tree 36
    def t36(features):
if features[3] < 5.302454:
            if features[18] < 73.70747:
                if features[1] < 0.021666324:
                    return -6.6422166e-05
                else:
                    return 0.00037643572
            else:
                if features[14] < 2.5109985:
                    return 0.00014309298
                else:
                    return 0.0012393234
        else:
            if features[17] < 0.5399378:
                if features[21] < 0.41108778:
                    return -0.001260629
                else:
                    return -0.00020364216
            else:
                if features[17] < 1.0745221:
                    return 0.00046250035
                else:
                    return -0.0005378998
        
    score += t36(features)

    # Tree 37
    def t37(features):
if features[18] < 85.162056:
            if features[18] < 73.70747:
                if features[18] < 66.82742:
                    return 2.1543878e-05
                else:
                    return -0.00030245067
            else:
                if features[1] < 0.0040621883:
                    return 0.0008229875
                else:
                    return 8.654131e-05
        else:
            if features[7] < 124.40748:
                return -0.00025153087
            else:
                return -0.0015216075
        
    score += t37(features)

    # Tree 38
    def t38(features):
if features[4] < -10.940355:
            return 0.0011242771
        else:
            if features[3] < -6.7628055:
                if features[18] < 35.355717:
                    return 0.0003176786
                else:
                    return -0.0012668675
            else:
                if features[16] < -0.66755503:
                    return 0.00019776149
                else:
                    return -2.679457e-05
        
    score += t38(features)

    # Tree 39
    def t39(features):
if features[15] < 1.9504019:
            if features[12] < 98.721825:
                if features[0] < 98.80212:
                    return 6.748401e-06
                else:
                    return -0.00059400423
            else:
                if features[5] < 2.0329716:
                    return 0.00042250412
                else:
                    return -2.3835286e-05
        else:
            if features[20] < 3.1726298:
                if features[14] < 1.370738:
                    return 0.00015589068
                else:
                    return -0.0002526391
            else:
                if features[20] < 5.5392566:
                    return 0.00036997057
                else:
                    return -0.00040664856
        
    score += t39(features)

    # Tree 40
    def t40(features):
if features[22] < 0.89847267:
            if features[22] < 0.84997344:
                if features[9] < 110.12416:
                    return -4.6909827e-05
                else:
                    return 0.00011223741
            else:
                if features[8] < 71.94027:
                    return -0.000285852
                else:
                    return 0.0009455122
        else:
            if features[21] < 0.9198338:
                if features[18] < 73.17508:
                    return -0.00025675588
                else:
                    return 0.00057505537
            else:
                if features[9] < 145.46736:
                    return -0.00084462186
                else:
                    return 0.00013339918
        
    score += t40(features)

    # Tree 41
    def t41(features):
if features[20] < -1.5578581:
            if features[20] < -2.4148476:
                if features[5] < 6.1726336:
                    return -1.3004773e-05
                else:
                    return 0.0012924223
            else:
                if features[22] < -0.099247746:
                    return -0.0001041258
                else:
                    return -0.0010612619
        else:
            if features[3] < 6.5396614:
                if features[14] < 0.28486788:
                    return -0.00046285483
                else:
                    return 3.8548766e-05
            else:
                if features[17] < 0.34021264:
                    return 0.0019264128
                else:
                    return 0.00027996473
        
    score += t41(features)

    # Tree 42
    def t42(features):
if features[13] < 152.65271:
            if features[13] < 152.17982:
                if features[1] < -0.029749539:
                    return 0.0006976099
                else:
                    return -4.209014e-06
            else:
                if features[5] < 4.353577:
                    return 0.0015512229
                else:
                    return -0.00037020276
        else:
            if features[8] < 156.83247:
                if features[16] < -1.0331678:
                    return -2.993182e-05
                else:
                    return -0.0017137275
            else:
                if features[1] < 0.0056643733:
                    return 0.00039113016
                else:
                    return -0.0003584745
        
    score += t42(features)

    # Tree 43
    def t43(features):
if features[5] < 0.9840165:
            if features[21] < 0.14053917:
                if features[19] < 1.9098394:
                    return -3.8332087e-06
                else:
                    return 0.0004727175
            else:
                if features[15] < 0.9634678:
                    return 0.0010577855
                else:
                    return 0.00016294674
        else:
            if features[4] < 1.2522593:
                if features[21] < -0.30675545:
                    return -0.0013345366
                else:
                    return -0.00025286977
            else:
                if features[1] < -0.01671769:
                    return -0.0013285636
                else:
                    return 7.6543205e-05
        
    score += t43(features)

    # Tree 44
    def t44(features):
if features[3] < 6.5396614:
            if features[3] < 5.4135246:
                if features[22] < -0.43278152:
                    return -0.00011108369
                else:
                    return 3.7233833e-05
            else:
                if features[7] < 165.65164:
                    return -0.0006445074
                else:
                    return 0.00016187209
        else:
            if features[15] < 2.3316216:
                return 0.0026369586
            else:
                if features[22] < 1.0513464:
                    return -0.00012394371
                else:
                    return 0.0006019229
        
    score += t44(features)

    # Tree 45
    def t45(features):
if features[15] < 1.8650908:
            if features[15] < 1.4948084:
                if features[21] < 0.40077758:
                    return 2.8285367e-05
                else:
                    return -0.0007013906
            else:
                if features[9] < 155.75403:
                    return 0.0004981399
                else:
                    return -0.0005497901
        else:
            if features[19] < 2.0254157:
                if features[13] < 140.08417:
                    return -0.0003930359
                else:
                    return -2.5494692e-05
            else:
                if features[19] < 2.520104:
                    return 0.00066521537
                else:
                    return -4.1323525e-05
        
    score += t45(features)

    # Tree 46
    def t46(features):
if features[18] < 34.47917:
            if features[16] < -0.5316557:
                if features[17] < -1.5071751:
                    return -5.549224e-05
                else:
                    return 0.000855531
            else:
                if features[7] < 68.34626:
                    return 0.0005064715
                else:
                    return -0.00045259434
        else:
            if features[22] < -0.8238561:
                if features[19] < 1.1850767:
                    return -0.0005054829
                else:
                    return 0.0010257863
            else:
                if features[19] < -2.8859918:
                    return 0.0007998002
                else:
                    return -2.7042788e-05
        
    score += t46(features)

    # Tree 47
    def t47(features):
if features[15] < 3.0103276:
            if features[15] < 2.7417614:
                if features[0] < 142.7882:
                    return 4.9224927e-05
                else:
                    return -0.00020359266
            else:
                if features[20] < 2.1130915:
                    return -0.00023095081
                else:
                    return -0.0014989459
        else:
            if features[7] < 128.85828:
                if features[12] < 119.80313:
                    return 9.66255e-05
                else:
                    return -0.000603836
            else:
                if features[16] < 0.9511192:
                    return 0.00045234305
                else:
                    return -4.3564538e-05
        
    score += t47(features)

    # Tree 48
    def t48(features):
if features[14] < 0.28486788:
            if features[18] < 34.47917:
                if features[3] < -0.085894704:
                    return 0.00061194965
                else:
                    return -2.2458291e-06
            else:
                if features[15] < 0.48353973:
                    return -0.0010239439
                else:
                    return -0.00017367279
        else:
            if features[7] < 188.23566:
                if features[9] < 168.77014:
                    return 2.565587e-05
                else:
                    return 0.00052125956
            else:
                if features[1] < -4.538677e-05:
                    return -0.00018198657
                else:
                    return -0.0013455735
        
    score += t48(features)

    # Tree 49
    def t49(features):
if features[3] < -0.32675582:
            if features[18] < 69.11555:
                if features[5] < -8.970885:
                    return 0.0003032502
                else:
                    return -0.00011315338
            else:
                if features[1] < 0.003010688:
                    return -0.0005639004
                else:
                    return -0.0020445965
        else:
            if features[1] < 0.018033022:
                if features[2] < 0.032798145:
                    return 5.485072e-05
                else:
                    return 0.00030575326
            else:
                if features[18] < 47.415623:
                    return 0.0006419228
                else:
                    return -0.00035406367
        
    score += t49(features)

    return score
