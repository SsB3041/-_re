import pandas as pd
import numpy as np 


print("규격을 입력하세용")
d_name= input()
data=pd.read_csv("{}_New.csv".format(d_name))


data=data.fillna(0)

data_row = data.shape[0]
data_coloum =data.shape[1]



####
##    n= Step의 갯수 Step이 너무 커질 시 Total 통합에서 Txt 파일 까지 담을 수 없는 크기가 존재
####

n=3


total_list = []
total_df = pd.DataFrame()
for i in range(0,data_row):
    test_df= pd.DataFrame()
    f1 = data.iloc[i,0]
    f2_min, f2_max = data.iloc[i,1], data.iloc[i,3] 
    f3_min, f3_max = data.iloc[i,3], data.iloc[i,4] 
    f4_min, f4_max = data.iloc[i,5], data.iloc[i,6]
    f5_min, f5_max = data.iloc[i,7], data.iloc[i,8]
    f6_min, f6_max = data.iloc[i,9], data.iloc[i,10]
    f7_min, f7_max = data.iloc[i,11], data.iloc[i,12]
    f8_min, f8_max = data.iloc[i,13], data.iloc[i,14]
    f9_min, f9_max = data.iloc[i,15], data.iloc[i,16]
    f10_min, f10_max = data.iloc[i,17], data.iloc[i,18]
    f11_min, f11_max = data.iloc[i,19], data.iloc[i,20]    
    f12_min, f12_max = data.iloc[i,21], data.iloc[i,22]
    f13_min, f13_max = data.iloc[i,23], data.iloc[i,24]
    f14_min, f14_max = data.iloc[i,25], data.iloc[i,26]
    f15_min, f15_max = data.iloc[i,27], data.iloc[i,28]
    f16_min, f16_max = data.iloc[i,29], data.iloc[i,30]
    f17_min, f17_max = data.iloc[i,31], data.iloc[i,32]
    f18_min, f18_max = data.iloc[i,33], data.iloc[i,34]    
    
    ####
    ##    Round와 Float을 건 이유 특정 화학 조성의 경우 Step을 구할 경우 10^-6까지 작은 값으로 존재, 위 존재 범위는 csv파일로 치환 시 사라지는 문제가 발생하여
    ##    특정 조성에는 round를 걸었음, 또한 자릿수 제한이 없을경우, 커널트릭을 적용 시(소수의 역수를 곱할 시 혹은 소수 소수 곱할 시) 너무 값이 커지는 문제가 존재
    ####
    
    f2_step = (f2_max-f2_min)/(n-1)
    f3_step = round(float(f3_max-f3_min)/(n-1),3)
    f4_step = (f4_max-f4_min)/(n-1)
    f5_step = (f5_max-f5_min)/(n-1)
    f6_step = round(float(f6_max-f6_min)/(n-1),3)
    f7_step = round(float(f7_max-f7_min)/(n-1),3)
    f8_step = round(float(f8_max-f8_min)/(n-1),3)
    f9_step = round(float(f9_max-f9_min)/(n-1),3)
    f10_step = (f10_max-f10_min)/(n-1)#B까지
    f11_step = round(float(f11_max-f11_min)/(n-1),3)#CU
    f12_step = round(float(f12_max-f12_min)/(n-1),3)
    f13_step = (f13_max-f13_min)/(n-1)
    f14_step = float(f14_max-f14_min)/(n-1)
    f15_step = float(f15_max-f15_min)/(n-1)
    f16_step = float(f16_max-f16_min)/(n-1)
    f17_step = float(f17_max-f17_min)/(n-1)
    f18_step = float(f18_max-f18_min)/(n-1)
    
     
    ####
    ##     Step == 최솟값에서 최댓값까지 뛰어넘는 간격, So 들어가지 않는다 (함유가 없다)라면 Step을 100으로 만들어 Pass하는 형식
    ####
    if f2_step == 0 :
        f2_step = 100      
    if f2_max == 0 or f2_min == f2_max:
        f2_step = 100
    if f3_step == 0 :
        f3_step == 100
    if f3_max==0 or f3_min==f3_max :
        f3_step = 100        
    if f4_step == 0 :
        f4_step = 100
    if f4_max ==0 or f4_min == f4_max :
        f4_step= 100
    if f5_step == 0 :
        f5_step = 100
    if f5_max ==0 or f5_min == f5_max :
        f5_step= 100
    if f6_step == 0 :
        f6_step = 100
    if f6_max ==0 or f6_min == f6_max :
        f6_step= 100
    if f7_step == 0 :
        f7_step = 100
    if f7_max ==0 or f7_min == f7_max :
        f7_step= 100
    if f8_step == 0 :
        f8_step = 100
    if f8_max ==0 or f8_min == f8_max :
        f8_step= 100
    if f9_step == 0 :
        f9_step = 100
    if f9_max ==0 or f9_min == f9_max :
        f9_step= 100
    if f10_step == 0 :
        f10_step = 100
    if f10_max ==0 or f10_min == f10_max :
        f10_step= 100
    if f11_step == 0 :
        f11_step = 100
    if f11_max ==0 or f11_min == f11_max :
        f11_step= 100
    if f12_step == 0 :
        f12_step = 100
    if f12_max ==0 or f12_min == f12_max :
        f12_step= 100
    if f13_step == 0 :
        f13_step = 100
    if f13_max ==0 or f13_min == f13_max :
        f13_step= 100
    if f14_step == 0 :
        f14_step = 100
    if f14_max ==0 or f14_min == f14_max :
        f14_step= 100
    if f15_step == 0 :
        f15_step = 100
    if f15_max ==0 or f15_min == f15_max :
        f15_step= 100
    if f16_step == 0 :
        f16_step = 100
    if f16_max ==0 or f16_min == f16_max :
        f16_step= 100 
    if f17_step == 0 :
        f17_step = 100
    if f17_max ==0 or f17_min == f17_max :
        f17_step= 100
    if f18_step == 0 :
        f18_step = 100
    if f18_max ==0 or f18_min == f18_max :
        f18_step= 100   
               
    ####
    ##    강종의 이름, 군집군을 불러옴
    ####
    name = data.loc[i,"Name"]
    SteelClass = data.loc[i,"SteelClass"]
    ####
    ##    탄소는 고정 (이름으로 판별 했을 시) 함유 조성의 갯수(m)의 따라 데이터의 갯수가 m^n승으로 범주를 만들어 증강하는 증강코드,
    ##    Range의 경우 () : 이상 미만 이므로 f2_max를 그대로 들어올 시 f2_max를 포함하지 않음
    ##    따라서 f2_max에서 Total 규격의 Max - Min을 해서 규격의 혼동을 야기하지 않고, f2_max를 포함할 수 있는 미솟값을 더함 ex)보론은 피코의 단위이기에 작은수를 추가
    ####
    for b in np.arange(f2_min,f2_max+0.001,f2_step):
        for c in np.arange(f3_min,f3_max+0.01,f3_step):                    
            for d in np.arange(f4_min,f4_max+0.01,f4_step):                    
                for e in np.arange(f5_min,f5_max+0.01,f5_step):                        
                    for f in np.arange(f6_min,f6_max+0.01,f6_step):                             
                        for g in np.arange(f7_min,f7_max+0.01,f7_step):
                            for h in np.arange(f8_min,f8_max+0.01,f8_step):
                                for i in np.arange(f9_min,f9_max+0.01,f9_step):                                        
                                    for j in np.arange(f10_min,f10_max+0.0001,f10_step):                                          
                                        for k in np.arange(f11_min,f11_max+0.01,f11_step) :
                                            for l in np.arange(f12_min,f12_max+0.01,f12_step) :
                                                for m in np.arange(f13_min,f13_max+0.0001,f13_step):
                                                    for Ti in np.arange(f14_min,f14_max+f14_step+0.001,f14_step):   
                                                        for Nb in np.arange(f15_min,f15_max+0.0001,f15_step):
                                                            for Wo in np.arange(f16_min,f16_max+0.0001,f16_step):
                                                                for Pb in np.arange(f17_min,f17_max+0.0001,f17_step):
                                                                    for Ne in np.arange(f18_min,f18_max+0.0001,f18_step):
                                                                        df_1=pd.DataFrame([{'Name': name, "SteelClass" :SteelClass, 'C':f1, 'Si':b, 'Mn':c ,'P':d,"S":e,"Cr":f,"Mo":g,"Ni":h,"V":i,"B":j,"Sn":k,"Cu":l,"Al":m,"Ti":Ti,"Nb":Nb,"W":Wo,"Pb":Pb,"N":Ne}])
                                                                        test_df = test_df.append(df_1, ignore_index=True)
                                                                        print(name)
    total_df = total_df.append(test_df, ignore_index=True)
total_df=pd.DataFrame(total_df)
# total_df.to_csv("SAE_Test.csv", index=False)
# total_df.to_csv("SAE_Test.txt",sep="\t",index=False)
# total_df.to_csv("JASO_Test.txt",sep="\t",index=False)
# total_df.to_csv("JIS_Test.txt",sep="\t",index=False)
# total_df.to_csv("GB_Test.txt",sep="\t",index=False)
# total_df.to_csv("ISO_Test.txt",sep="\t",index=False)

total_df.to_csv("{}_Test.txt".format(d_name),sep="\t",index=False)
