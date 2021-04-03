import pandas as pd
import numpy as np
from datetime import datetime

f_year = datetime.now().year

df = pd.read_excel('L:\SCM\SOP\AutoLoad\Sales4SOP\SalesLoad2SOP.xlsx',sheet_name='Sheet1')
df.columns = ['Sales Office','Sales Group','Customer','Customer desc','PM','Year/Month','KG']
df= df.drop(df.index[0])  # drop first line
ExepPM = ['OTHERS PVC','PROCESSED PVC','ROOFING ACCESSORIES','POLYPROPYLENE','OTHERS POLYCARBONAT','PROCESSED PC']
df = df[~df['PM'].isin(ExepPM)]
dfindx = pd.read_csv('L:\SCM\SOP\AutoLoad\Sales4SOP\INDEX.csv')

df.loc[df['Sales Office'] == 'North America' , ['Sales Office','Sales Group','Customer','Customer desc']]=['AMER','AMER','AMER','AMER']
df.loc[df['Sales Group'].str.contains('Australia') , ['Sales Group','Customer','Customer desc']]=['AUS_WHS','AUS_WHS','AUS_WHS']
df.loc[(df['Sales Group'] == 'Tovi Rotem') & (df['Customer'] != '13242')& (df['Customer'] != '166')& (df['Customer'] != '13924')& (df['Customer'] != '5580'),
       ['Sales Group','Customer','Customer desc']] = ['AUS_WHS','AUS_WHS','AUS_WHS']

df.loc[df['Customer'] == 'R7129' , ['Sales Office','Customer','Customer desc']]=['PLR4U','PLR4U','PLR4U']
df.loc[df['Sales Office'] == 'Israel' , ['Customer','Customer desc','Sales Group']]=['IL_Local','IL_Local','IL_Local']
df.loc[df['Sales Office'].str.contains('Central America') , ['Sales Office','Sales Group','Customer','Customer desc']]=['AMER','AMER','AMER','AMER']
#df.loc[df['Customer'] == 'PLR4U' , ['Sales Office','Sales Group',]]=['Israel','IL_Local']
df.loc[df['Customer'] == 'PLR4U' , ['Sales Office','Sales Group','Customer','Customer desc']]=['Israel','IL_Local','IL_Local','IL_Local']
df.loc[df['Customer desc'].str.contains('FORECAST') , ['Customer','Customer desc']]=['Forecast Customer','Forecast_Customer']
df.loc[df['Sales Office'] == 'Africa' , ['Sales Group','Customer','Customer desc']]=['S.A FORECAST','S.A FORECAST','S.A FORECAST']
#df.loc[df['Sales Office']=='UK' and ['Sales Group']=='Craig Walker ,CPL' |['Sales Group']=='Lisa Greenwood' , ['Sales Group','Customer','Customer desc']]=['CPL_SG','CPL_SG','CPL_SG']
df['Sales Group']= df['Sales Group'].replace(['Cash Sales','Craig Walker ,CPL','Daryll Croft','David Johnson','Igal Sunik','Igal Sunik-TPS','Laura Sharp','Lisa Greenwood','Stacey Maundrill,CPL','Vicky Cleary','Chris Elliott','Hayley Cresswell'], 'CPL_SG')
df.loc[df['Sales Group'] == 'CPL_SG' , ['Customer','Customer desc']]=['CPL_SG','CPL_SG']
df['Year'] = df['Year/Month'].str[3:]
df['Year'] = df['Year'].astype(int)
df['Year']= df['Year'].astype(str)
df['Year/Month']= df['Year/Month'].str[0:2]

                  # rename months
df['Year/Month']= df['Year/Month'].replace(['01','02','03','04','05','06','07','08','09','10','11','12'],
 ['Sales-Jan','Sales-Feb','Sales-Mar', 'Sales-Apr', 'Sales-May','Sales-Jun','Sales-Jul','Sales-Aug','Sales-Sep','Sales-Oct','Sales-Nov','Sales-Dec'])
                  # add months file
df0 = pd.read_excel('L:\SCM\SOP\AutoLoad\Sales4SOP\Base0.xlsx',sheet_name='Sheet2')
df0['Year'] = str(f_year)                 

frames = [df,df0]
df1=pd.concat(frames)
df1 = df1[['Sales Office','Sales Group','Customer','Customer desc','PM','Year','Year/Month','KG']]
df1['KG']= df1['KG'].astype(float)/1000

# =============================================================================
# Left join
# =============================================================================
df2= pd.merge(df1,dfindx,how='left',indicator=True) 

df2['Indx'] = df2['ID'].replace(np.nan, 0)
df2['Year']= df2['Year'].astype(str)
df2['Indx']= df2['Indx'].astype(int)
df2['ID'] = df2['ID'].replace(np.nan, 0)
df2['ID']= df2[ 'ID'].astype(int)
df2['ID'] = df2[ 'ID'].astype(str) +'-'+ df2[ 'Year']

a = df2.groupby(['Indx','ID','Sales Office','Sales Group','Customer','Customer desc','PM','Year','Year/Month']) ['KG'].sum().unstack()

#        Out to CSV - split cells
a.to_csv('L:\SCM\SOP\AutoLoad\Sales4SOP\SalesLoad2SOP_A.csv')
#        Rearrange columns
b = pd.read_csv('L:\SCM\SOP\AutoLoad\Sales4SOP\SalesLoad2SOP_A.csv')
b = b[["ID","Indx","Sales Office","Sales Group","Customer","Customer desc","PM","Year","Sales-Jan",
             "Sales-Feb","Sales-Mar","Sales-Apr","Sales-May","Sales-Jun","Sales-Jul",
             "Sales-Aug","Sales-Sep","Sales-Oct","Sales-Nov","Sales-Dec"]]
b.to_excel('L:\SCM\SOP\AutoLoad\Sales4SOP\SalesLoad2SOP_A.xlsx',sheet_name='ToLoad', index=False)
b.to_excel(r'\\PLRMCSRV\Palram_SNOP\SNOP Sales reference\SalesLoad2SOP_A.xlsx',sheet_name='ToLoad', index=False)
'''
del df
del a
del dfindx
del result
'''
for x in range(0, 3):
     print("DONE! " )
     

    
#print (df.iloc[100:102])
# https://www.youtube.com/watch?edufilter=NULL&v=vmEHCJofslg