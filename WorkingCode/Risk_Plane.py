import Risk_Curve as RC
import pickle 
def Risk_Plane(repeats, nus_para,nus_trans):
    for k in nus_para:
        print(k)
        data = RC.RiskCurve(repeats,nus_trans)
        #pickle.dump(data,open( "risk_plane_v_para_v_trans.p", "wb" ) )
        pickle.dump(data,open( "risk_plane_0.04_0-0.3.p", "wb" ) )


nus_para = [0.04] #[0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22,0.24,0.26,
           # 0.28,0.3,0.32,0.34,0.36,0.38,0.4,0.42,0.44,0.46,0.48,0.5,0.52,0.54,
           # 0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.,76,0.78,0.8,0.82,
           # 0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,1]
#1
#repeats = 10
#nus_trans = [0,0.2,0.4]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.42,0.44,0.46]
#nus_trans = [0.48,0.50,0.52]
#nus_trans = [0.54,0.56,0.58] 
#nus_trans = [0.60,0.62,0.64] 
#nus_trans = [0.66,0.68,0.70]  
 #2
repeats = 10
nus_trans = [0,0.2,0.3]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.34,0.36,0.38]
#nus_trans = [0.4,0.42,0.44]
#nus_trans = [0.46,0.48,0.50]
#nus_trans = [0.52,0.54,0.56] 
#nus_trans = [0.58,0.60,0.62] 
#nus_trans = [0.64,0.66,0.68]  
##3
#repeats = 10
#nus_trans = [0,0.2,0.3]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.32,0.34,0.36]
#nus_trans = [0.38,0.40,0.42]
#nus_trans = [0.44,0.46,0.48]
#nus_trans = [0.50,0.52,0.54] 
#nus_trans = [0.56,0.58,0.60] 
#nus_trans = [0.62,0.64,0.66]  
##4
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.30,0.32,0.34]
#nus_trans = [0.36,0.38,0.40]
#nus_trans = [0.42,0.44,0.46]
#nus_trans = [0.48,0.50,0.52] 
#nus_trans = [0.54,0.56,0.58] 
#nus_trans = [0.60,0.62,0.64]  
##5
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38]
#nus_trans = [0.40,0.42,0.44]
#nus_trans = [0.46,0.48,0.50] 
#nus_trans = [0.52,0.54,0.56] 
#nus_trans = [0.58,0.60,0.62] 
##6
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.26,0.28,0.30]
#nus_trans = [0.32,0.34,0.36]
#nus_trans = [0.38,0.40,0.42]
#nus_trans = [0.44,0.46,0.48] 
#nus_trans = [0.50,0.52,0.54] 
#nus_trans = [0.56,0.58,0.60]
##7
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.24,0.26,0.28]
#nus_trans = [0.30,0.32,0.34]
#nus_trans = [0.36,0.38,0.40]
#nus_trans = [0.42,0.44,0.46] 
#nus_trans = [0.48,0.50,0.52] 
#nus_trans = [0.54,0.56,0.58]  
##8   
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.8,1.0]  
#repeats = 50
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38] 
#nus_trans = [0.40,0.42,0.44] 
#nus_trans = [0.46,0.48,0.50]
#nus_trans = [0.52,0.54,0.56] 
##9
#repeats = 10
#nus_trans = [0]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.20,0.22,0.24]
#nus_trans = [0.26,0.28,0.30]
#nus_trans = [0.32,0.34,0.36] 
#nus_trans = [0.38,0.40,0.42] 
#nus_trans = [0.44,0.46,0.48]
#nus_trans = [0.50,0.52,0.54] 
##10
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.24,0.26,0.28]
#nus_trans = [0.30,0.32,0.34] 
#nus_trans = [0.36,0.38,0.40] 
#nus_trans = [0.42,0.44,0.46]
#nus_trans = [0.48,0.50,0.52] 
##11
#repeats = 10
#nus_trans = [0]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32] 
#nus_trans = [0.34,0.36,0.38] 
#nus_trans = [0.40,0.42,0.44]
#nus_trans = [0.46,0.48,0.50]
##12
#repeats = 10
#nus_trans = [0]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.20,0.22,0.24]
#nus_trans = [0.26,0.28,0.30] 
#nus_trans = [0.32,0.34,0.36] 
#nus_trans = [0.38,0.40,0.42]
#nus_trans = [0.44,0.46,0.48]
##13
#repeats = 10
#nus_trans = [0,0.2,0.22]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.24,0.26,0.28] 
#nus_trans = [0.30,0.32,0.34] 
#nus_trans = [0.36,0.38,0.40]
#nus_trans = [0.42,0.44,0.46]
##14
#repeats = 10
#nus_trans = [0,0.2]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.22,0.24,0.26] 
#nus_trans = [0.28,0.30,0.32] 
#nus_trans = [0.34,0.36,0.38]
#nus_trans = [0.40,0.42,0.44]
##15
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.5,1.0]  
#repeats = 50
#nus_trans = [0.20,0.22,0.24] 
#nus_trans = [0.26,0.28,0.30] 
#nus_trans = [0.32,0.34,0.36]
#nus_trans = [0.38,0.40,0.42]
##16
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.5,1.0]  
#repeats = 50
#nus_trans = [0.18,0.20,0.22] 
#nus_trans = [0.24,0.26,0.28] 
#nus_trans = [0.30,0.32,0.34]
#nus_trans = [0.36,0.38,0.40]
##17
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26] 
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##18
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.14,0.16,0.18] 
#nus_trans = [0.20,0.22,0.24] 
#nus_trans = [0.26,0.28,0.30]
#nus_trans = [0.32,0.34,0.36]
#nus_trans = [0.38,0.4]
##18
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.12,0.14,0.16] 
#nus_trans = [0.18,0.20,0.22] 
#nus_trans = [0.24,0.26,0.28]
#nus_trans = [0.30,0.32,0.34]
#nus_trans = [0.36,0.38,0.4]
##19
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##20
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##21
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##22
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##23
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##24
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##25
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##26
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
##27
#repeats = 10
#nus_trans = [0,]
#nus_trans = [0.7,1.0]  
#repeats = 50
#nus_trans = [0.1,0.12,0.14] 
#nus_trans = [0.16,0.18,0.20] 
#nus_trans = [0.22,0.24,0.26]
#nus_trans = [0.28,0.30,0.32]
#nus_trans = [0.34,0.36,0.38,0.4]
Risk_Plane(repeats,nus_para,nus_trans)