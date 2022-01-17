# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:26:59 2022

@author: sys
"""

import pandas as pd
df_Demogrph=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Demograph_Details")
df_Demogrph
df_Finance=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Financial_Details")
df_Finance
df_Transc=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="Transactions_Details")
df_Transc
df_T=pd.pivot_table(df_Transc,values='Transaction_amount',index='Customer_ID',aggfunc='count')
df_T
df_Demogrph_cl_f1=df_Demogrph[['Customer_ID', 'Customer_Name']]
df_Demogrph_cl_f1
df_Transc_cl_f2=df_Transc[['Customer_ID', 'Transaction_amount']]
df_Transc_cl_f2
df_Finance_cl_f3=df_Finance[['Customer_ID', 'Income']]
df_Finance_cl_f3
df1=df_Demogrph_cl_f1.merge(df_Finance_cl_f3,how='inner',on='Customer_ID')
df1
df2=df1.merge(df_T,how='inner',on='Customer_ID')
df2
df_offer=pd.read_excel(r"C:\Users\sys\Bhavani\Data_Engineering.xlsx",sheet_name="offer_Details")
df_offer
df_offer_cl_fl=df_offer[['Type_of_loan_Description','Type_of_Loan']]
df_offer_cl_fl
df_new_cc= df2[((df2['Income']  >=10000) & (df2['Income'] < 30000)  & (df2.Transaction_amount>2)) ]
df_new_cc
df_new_PL= df2[((df2['Income']  >=30000) & (df2['Income'] < 50000)  & (df2.Transaction_amount>1)) ]
df_new_PL
df_new_LI= df2[((df2['Income']  >=50000) & (df2['Income'] < 60000)  & (df2.Transaction_amount>1)) ]
df_new_LI        
df_new_HL= df2[((df2['Income']  >60000)  & (df2.Transaction_amount>2)) ]
df_new_HL 
df_final=pd.concat([df_new_cc,df_new_PL,df_new_LI,df_new_HL],axis=0)
df_final=pd.concat([df_new_cc,df_new_PL,df_new_LI,df_new_HL],axis=0,ignore_index = True)
df_final
df_final_cl_fl=df_final[['Customer_ID', 'Customer_Name']]
df_final_cl_fl
df_output=pd.concat([df_final_cl_fl,df_offer_cl_fl],axis=1)
df_output

