import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing CSV file for each year
csv_15 = pd.read_csv('VS15MORT.csv')
csv_16 = pd.read_csv('VS16MORT.csv')
csv_17 = pd.read_csv('VS17MORT.csv')

#selecting all drug overdose deaths only using ICD 10 MCOD cause of death codes

csv_meth =  csv.loc[csv['  ICD10'].str.contains("T436", case = false)] 
X40-X44, X60-X64, X85, Y10-Y14

#create list of all accidental drug overdose death codes
drug_codes = ['X40', 'X41', 'X42', 'X43', 'X44', 'X60', 'X61', 'X62', 'X63', 'X64', 'X85', 'Y10', 'Y11', 'Y12', 'Y13', 'Y14']
#create accidental_OD regex
drug_dat = '|'.join(drug_codes)

#strip spaces from columns of each dataframe
csv_15.columns = csv_15.columns.str.strip()
csv_16.columns = csv_16.columns.str.strip()
csv_17.columns = csv_17.columns.str.strip()

#find all overdose deaths using accidnetal OD regex

#VERSION A

csv_15_OD =  csv_15.loc[csv_15['  ICD10'].str.contains(drug_dat, case = False)]
csv_16_OD =  csv_16.loc[csv_16['  ICD10'].str.contains(drug_dat, case = False)]
csv_17_OD =  csv_17.loc[csv_17['  ICD10'].str.contains(drug_dat, case = False)]

#VERSION B, using is in 
CSV_15_OD = csv_15.loc[csv_15['  ICD10'].str.contains('|'.join(drug_codes), case = False)]


#list all causes of death by count by year
COD_15 = csv_15['  ICD10'].value_counts().reset_index().rename(columns={'index': '  ICD10', 0: 'count'})
COD_16 = csv_16['  ICD10'].value_counts().reset_index().rename(columns={'index': '  ICD10', 0: 'count'})
COD_17 = csv_17['  ICD10'].value_counts().reset_index().rename(columns={'index': '  ICD10', 0: 'count'})