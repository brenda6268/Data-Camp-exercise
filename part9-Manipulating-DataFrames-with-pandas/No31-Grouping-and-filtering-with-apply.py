#Grouping and filtering with .apply()
'''
By using .apply(), you can write functions that filter rows within groups. The .apply() method will handle the iteration over individual groups and then re-combine them back into a Series or DataFrame.

In this exercise you'll take the Titanic data set and analyze survival rates from the 'C' deck, which contained the most passengers. To do this you'll group the dataset by 'sex' and then use the .apply() method on a provided user defined function which calculates the mean survival rates on the 'C' deck:

def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()
The DataFrame has been pre-loaded as titanic.

Instructions
100 XP
Instructions
100 XP
Group titanic by 'sex'. Save the result as by_sex.
Apply the provided c_deck_survival function on the by_sex DataFrame. Save the result as c_surv_by_sex.
Print c_surv_by_sex.
'''

# Code
# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)

'''
sex
female    0.913043
male      0.312500
dtype: float64

'''
'''
In [2]: titanic.head()
Out[2]: 
   pclass  survived                                             name     sex    age  ...    cabin  embarked boat   body                        home.dest
0       1         1                    Allen, Miss. Elisabeth Walton  female  29.00  ...       B5         S    2    NaN                     St Louis, MO
1       1         1                   Allison, Master. Hudson Trevor    male   0.92  ...  C22 C26         S   11    NaN  Montreal, PQ / Chesterville, ON
2       1         0                     Allison, Miss. Helen Loraine  female   2.00  ...  C22 C26         S  NaN    NaN  Montreal, PQ / Chesterville, ON
3       1         0             Allison, Mr. Hudson Joshua Creighton    male  30.00  ...  C22 C26         S  NaN  135.0  Montreal, PQ / Chesterville, ON
4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female  25.00  ...  C22 C26         S  NaN    NaN  Montreal, PQ / Chesterville, ON

[5 rows x 14 columns]


'''