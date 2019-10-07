#importations
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from matplotlib.pyplot import figure

df_cleaned = pd.read_csv('Deats_coded.csv')
df_cleaned.head()
#list all ICD 10 codes
df_cleaned


#create list of ICD 10 codes associated with suicide
suicide_guns = ['X74', 'X73', 'X72']
#create an expression that has each ICD10 as a possible condition
suicide_guns_regex = '|' .join(suicide_guns)


df_suicide = df_cleaned[df_cleaned['ICD10'].str.contains(suicide_guns_regex)]
#visualize our value counts to show that the data worked
df_suicide['ICD10'].value_counts()
df_suicide.columns

#create a simplified race category
df_suicide["Race-Simplified"] = df_suicide["Race"]
#replace values as needed
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Vietnamese' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Filipino' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Asian Indian' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Chinese' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Korean' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Japanese' : 'Asian'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Hawaiian' : 'Asian or Pacific Islander'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Samoan' : 'Asian or Pacific Islander'})
df_suicide["Race-Simplified"]= df_suicide["Race-Simplified"].replace({'Guamanian' : 'Asian or Pacific Islander'})
df_suicide["Race-Simplified"].value_counts()
df_suicide["Hispanic_Origin"].value_counts()
#check hispanic origin and replace relevant Race-Simplified Value

#df_suicide['Race-Simplified'] = df_suicide['Hispanic_Origin'].apply(lambda x: 'Hispanic' if x == 'Mexican' else print("nochanges"))
for indx, row in df_suicide.iterrows():
    if df_suicide.loc[indx, 'Hispanic_Origin' ]               == 'Mexican' :
        df_suicide.loc[indx, 'Race-Simplified'] = 'Hispanic'
    elif df_suicide.loc[indx, 'Hispanic_Origin' ]  == 'Puerto Rican' :
        df_suicide.loc[indx, 'Race-Simplified'] = 'Hispanic'
    elif df_suicide.loc[indx, 'Hispanic_Origin' ]  == 'Central or South American' :
        df_suicide.loc[indx, 'Race-Simplified'] = 'Hispanic'
    elif df_suicide.loc[indx, 'Hispanic_Origin' ]  == 'Cuban' :
        df_suicide.loc[indx, 'Race-Simplified'] = 'Hispanic'
    elif df_suicide.loc[indx, 'Hispanic_Origin' ]  == 'Hispanic origin unknown' :
        df_suicide.loc[indx, 'Race-Simplified'] = 'Hispanic'
    else:
        print("Nothing to change")
    

#df_suicide['Race-Simplified']

df_suicide["Race-Simplified"].value_counts()

df_suicide.columns
#group by year and Race, resetting index to keep column names available
suicide_year_cat = df_suicide.groupby(['Data_Year', 'Race']).count().reset_index()
#rename column
suicide_year_cat = suicide_year_cat.rename(columns={"Unnamed: 0": "Number of Deaths"})

#visualize data
suicide_year_cat

df_suicide_total = df_suicide.groupby(['Data_Year']).count().reset_index()
df_suicide_total = df_suicide_total.rename(columns = {'Unnamed: 0' : 'Number of Deaths'})

#visualize dataframe without grouping
df_suicide_total.columns
df

#create axis

x_axis = df_suicide_total['Data_Year']
y_axis = df_suicide_total['Number of Deaths']
colors = np.array(["blue"])




fig, ax = plt.subplots()
def autolabel(rects):
   
   for rect in rects:
       height = rect.get_height()
       ax.annotate('{}'.format(height),
                   xy=(rect.get_x() + rect.get_width() / 2, height),
                   xytext=(0, 2),  # 3 points vertical offset
                   textcoords="offset points",
                   ha='center', va='bottom')
rect=ax.bar(x_axis, y_axis, color='r', width=0.35 , align="center")
autolabel(rect)


# Plot
plt.bar(x_axis, y_axis)
plt.title('Number of Gun Deaths By Suicide By Year')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.ylim(bottom = 0, top = 50000)
fig = plt.gcf()
fig.set_size_inches(6, 4, forward=True)

#conduct Chi-Square with the years of the biggest difference
# Observed data in a (hypothetical) year where deaths are the same for each year
total = df_suicide_total["Number of Deaths"].sum()
deaths_by_year = df_suicide_total["Number of Deaths"]
print (total)
observed = pd.Series([deaths_by_year[0], deaths_by_year[1], deaths_by_year[2]], index=["2015", "2016", "2017"])
df = pd.DataFrame([observed]).T
df[1] = total/3
df.columns = ["observed", "expected"]
critical_value = stats.chi2.ppf(q = 0.95, df = 2)
df

# Run the chi square test with stats.chisquare()
stats.chisquare(df['observed'], df['expected'])
#we can conlcude based on a chi-square test that the number of deaths by suicide has increased and is
#statistically significant

#pivot table for breakdown by ICD10 code
suicide_year_cat = df_suicide.groupby(['Data_Year', 'Race']).count().reset_index()
suicide_year_cat.columns
#drop unnecessary frames
suicide_year_cat = suicide_year_cat.drop(['Month_Of_Death', 'Resident_Status', 'Sex', 'Age', 'Age_Group', 'Place_Of_Death', 
                                          'Marital_Status', 'DOW_of_Death', 'Injured_At_Work', 'Manner_Of_Death' ,'Activity_Code',  'Place_Of_Causal_Injury' ,'Hispanic_Origin', 'Causes_of_Death', 'ICD10'], axis=1)
suicide_year_cat
race_pivot = suicide_year_cat.pivot(index = "Data_Year", columns="Race").reset_index()
race_pivot = race_pivot.rename(columns={"Unnamed: 0": "Number of Deaths"})
suicide_year_cat["Race"].value_counts()

#plot line graph for total number of deaths, then broken down by ICD10

# Generate the Plot (with Error Bars)
fig, ax = plt.subplots()

#create timepoints list 
timepoints = [2015, 2016, 2017]


#create list of standard error of the means for each drug by time 
#create list of each mean for each drug by time 

codes = ['X73',
         'X94',
         'W33',
         'Y23',]

colors = ['#000000', 
          '#0000FF',
          '#8A2BE2',
          '#A52A2A',]

descriptions = ['Intentional self-harm',
             'Homicide',
             'Accident',
             'Undetermined']


#set figure size, limits, and labels
ax.set_xlabel("Year of Death")
ax.set_ylabel("Number of Deaths")
ax.set_xlim(2015, 2018)
ax.set_ylim(0, 3000)
fig.set_size_inches(18.5, 10.5, forward=True)



#loop through list of each drugs and plot with corresponding color using zip function
for code, color, description in zip(codes, colors, descriptions):

    #get number of deaths for each code
    death_code = by_death_pivot['Number of Deaths'][code].tolist()
    #generate legend description 
    description = "Number of Deaths Due to " + str(description) 
    #ax.errorbar(timepoints, means, yerr=sem, fmt='o', color = color, marker='s', label=description)
    #create actual plot
    plt.plot(timepoints, death_code, linewidth=1, color = color, label=description, marker='o')
    
    

plt.legend(loc="best", fontsize="small", fancybox=True)
figure(num=None, figsize=(160, 80), dpi=100, facecolor='w', edgecolor='k')

plt.show()


# Save the Figure







# Generate the Plot (Accounting for percentages)

# Save the Figure

# Show the Figure
plt.show()

#conduct Chi-Square for the two largest categories, suicide and homicide
# Observed data in a (hypothetical) year where deaths are the same for each year
total_suicide = by_death_pivot["Number of Deaths"]['X73'].sum()
deaths_by_year = by_death_pivot["Number of Deaths"]['X73']
print (total_suicide)
deaths_by_year
observed = pd.Series([deaths_by_year[0], deaths_by_year[1], deaths_by_year[2]], index=["2015", "2016", "2017"])
df = pd.DataFrame([observed]).T
df[1] = total_suicide/3
df.columns = ["observed", "expected"]
critical_value = stats.chi2.ppf(q = 0.95, df = 2)
print(df)
stats.chisquare(df['observed'], df['expected'])

#conduct Chi-Square for the two largest categories, suicide and homicide
# Observed data in a (hypothetical) year where deaths are the same for each year
total_homicide = by_death_pivot["Number of Deaths"]['X94'].sum()
deaths_by_year = by_death_pivot["Number of Deaths"]['X94']
print (total_homicide)
deaths_by_year
observed = pd.Series([deaths_by_year[0], deaths_by_year[1], deaths_by_year[2]], index=["2015", "2016", "2017"])
df = pd.DataFrame([observed]).T
df[1] = total_homicide/3
df.columns = ["observed", "expected"]
critical_value = stats.chi2.ppf(q = 0.95, df = 2)
print(df)
stats.chisquare(df['observed'], df['expected'])