# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 00:18:23 2020

@author: Romain

gecko-9 - ISO-ir-6
"""

import pandas as pd
import iso_ir_6_table

df = pd.DataFrame()
        
"""columns = {'1','2','3','4','5','6','7','8','9','10','11',
'12','13','14','15','16','17','18','19','20','21','22'})"""

df = pd.read_csv("E:/Users/Romain/Documents/The Gecko/9-ISO-ir-6/bite.csv")
df = df.fillna(0)

l = []


for i in range(0,159):
    for j in df.columns:
        l.append(int(df[j][i]))
    
bin_list = []

for i in l:
    bin_list.append("{:08b}".format(i))
    
    
PT = ""
clear = []

for i in bin_list:
    PT = PT + str(iso_ir_6_table.default_char(i))
    clear.append(iso_ir_6_table.default_char(i))
    

print(PT)

pt = ""

for i in range(len(clear)):
    if clear[i] == "SP" or clear[i] == "CR" or clear[i] == "LF":
        clear[i] = " "
        
    pt = pt + str(clear[i])






















