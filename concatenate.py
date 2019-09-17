import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import array as arr

#importing CSV file for each year
csv_12 = pd.read_csv('VS12MORT.csv')
csv_13 = pd.read_csv('VS13MORT.csv')
csv_14 = pd.read_csv('VS14MORT.csv')
csv_15 = pd.read_csv('VS15MORT.csv')
csv_16 = pd.read_csv('VS16MORT.csv')
csv_17 = pd.read_csv('VS17MORT.csv')



#deaths array creation
deaths = [csv_12, csv_13, csv_14, csv_15, csv_16, csv_17]

#strip column names for each mortality file
first_year = 2012
for i, death in enumerate(deaths):
	death.columns = death.columns.str.strip()
	for j, col in enumerate(death.columns):
		print("In " ,first_year+i ,"the column name is" ,col)



#concatenate column names for each mortality file
first_year = 2012
for i, death in enumerate(deaths):
	death['all_MCOD'] = death['RA1'].str.cat(death[['RA1','RA2','RA3','RA4','RA5','RA6','RA7','RA8','RA9','RA10','RA11','RA12','RA13','RA14','RA15','RA16','RA17','RA18','RA19', 'RA20']], sep=' - ')
	print("next--year", first_year+i)
	for j, col in enumerate(death.columns):
		print("In " ,first_year+i ,"the column name is" ,col)
	

#write each file to CSV
first_year = 2012
for i, death in enumerate(deaths):
	current_year = first_year + i 
	title = "{}_all_mortality_concat.csv".format(current_year)
	death.to_csv(title)
	print("next--year", first_year+i)
	
#Find number of overdose deaths using CDC-Case definition 
drug_codes = ['X40', 'X41', 'X42', 'X43', 'X44', 'X60', 'X61', 'X62', 'X63', 'X64', 'X85', 'Y10', 'Y11', 'Y12', 'Y13', 'Y14']
#create accidental_OD regex
drug_dat = '|'.join(drug_codes)

#create subsets for each year based on overdose death case definition
OD_2012 =  csv_12.loc[csv_12['ICD10'].str.contains(drug_dat, case = False)]
OD_2013 =  csv_13.loc[csv_13['ICD10'].str.contains(drug_dat, case = False)]
OD_2014 =  csv_14.loc[csv_14['ICD10'].str.contains(drug_dat, case = False)]
OD_2015 =  csv_15.loc[csv_15['ICD10'].str.contains(drug_dat, case = False)]
OD_2016 =  csv_16.loc[csv_16['ICD10'].str.contains(drug_dat, case = False)]
OD_2017 =  csv_17.loc[csv_17['ICD10'].str.contains(drug_dat, case = False)]

OD_deaths = [OD_2012, OD_2013, OD_2014, OD_2015, OD_2016, OD_2017]


#write each overdose-death year to CSV
first_year = 2012
for i, OD_death in enumerate(OD_deaths):
	current_year = first_year + i 
	title = "{}_all_overdose_deaths_concat.csv".format(current_year)
	OD_death.to_csv(title)
	print("next--year", first_year+i)













#List Columns
for col in csv_12.columns: 
    print(col) 
#Strip the columns of leading blank spaces
csv_12.columns = csv_15.columns.str.strip()

#list columns after stripping
for col in csv_12.columns: 
    print(col) 

#create new dataframe with 20 contributing causes of death using RA1:RA20 names
csv_12["all_MCOD"] = csv_15["RA1"].str.cat(csv_15[['RA1','RA2','RA3' ,'RA4','RA5' ,'RA6' ,'RA7' ,'RA8' ,'RA9' ,'RA10' ,'RA11' ,'RA12' ,'RA13' ,'RA14' ,'RA15' ,'RA16' ,'RA17' ,'RA18' ,'RA19' ,'RA20']], sep=' - ')

#Drug overdose deaths were identified using the International Classification of Diseases, Tenth Revision (ICD10) , based on the ICD-10 underlying cause-of-death codes X40–44 (unintentional), X60–64 (suicide), X85
#(homicide), or Y10–Y14 (undetermined intent). 


psychostim_codes = ['T436']

#create subframe for any drug_codes

#csv_15_OD =  csv_15.loc[csv_15['all_MCOD'].str.contains(drug_dat, case = False)]

#csv_15_meth =  csv_15.loc[csv_15['all_MCOD'].str.contains(psychostim_codes, case = False)]

#create subframe for any firearm assault/gun homicide
firearm_deaths = ['W32', 'W33', 'W34', 'X72', 'X73', 'X74', 'X93', 'X94', 'X95', 'Y22', 'Y23', 'Y24', 'Y35']
firearm_dat = '|'.join(firearm_deaths)
#create array for all deaths involving guns from 2012 to 2017
csv_12_guns = csv_12.loc[csv_12['ICD10'].str.contains(firearm_dat, case = False)]
csv_13_guns = csv_13.loc[csv_13['ICD10'].str.contains(firearm_dat, case = False)]
csv_14_guns = csv_14.loc[csv_14['ICD10'].str.contains(firearm_dat, case = False)]
csv_15_guns = csv_15.loc[csv_15['ICD10'].str.contains(firearm_dat, case = False)]
csv_16_guns = csv_16.loc[csv_16['ICD10'].str.contains(firearm_dat, case = False)]
csv_17_guns = csv_17.loc[csv_17['ICD10'].str.contains(firearm_dat, case = False)]


#find any cases involving any opioid and any cocaine or psychostimulant with abuse potential. 
#denominator: All overdose deaths(i.e. contains "drug_dat", then from that subset, any polydrug combo, which means contains
#First, we find the CDC case definition for an overdose  using the International Classification of Diseases, Tenth Revision (ICD10) , based on the ICD-10 underlying cause-of-dea
RA_15_OD = RA_15.loc[RA_15['ICD10'].str.contains(drug_dat, case = False)]


gun_deaths = [csv_12_guns, csv_13_guns, csv_14_guns, csv_15_guns, csv_16_guns, csv_17_guns]




#write deaths to CSV
first_year = 2012
for i, gun_death in enumerate(gun_deaths):
	current_year = first_year + i 
	title = "{}_all_gun_deaths.csv".format(current_year)
	gun_death.to_csv(title)
	print("next--year", first_year+i)