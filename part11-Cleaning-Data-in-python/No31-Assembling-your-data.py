#Assembling your data
'''
Here, three DataFrames have been pre-loaded: g1800s, g1900s, and g2000s. These contain the Gapminder life expectancy data for, respectively, the 19th century, the 20th century, and the 21st century.

Your task in this exercise is to concatenate them into a single DataFrame called gapminder. This is a row-wise concatenation, similar to how you concatenated the monthly Uber datasets in Chapter 3.

Instructions
100 XP
Use pd.concat() to concatenate g1800s, g1900s, and g2000s into one DataFrame called gapminder. Make sure you pass DataFrames to pd.concat() in the form of a list.
Print the shape and the head of the concatenated DataFrame.
'''

# Code
# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s,g1900s, g2000s])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())


'''result
(780, 218)
    1800   1801   1802   1803   1804          ...            2013  2014  2015  2016        Life expectancy
0    NaN    NaN    NaN    NaN    NaN          ...             NaN   NaN   NaN   NaN               Abkhazia
1  28.21  28.20  28.19  28.18  28.17          ...             NaN   NaN   NaN   NaN            Afghanistan
2    NaN    NaN    NaN    NaN    NaN          ...             NaN   NaN   NaN   NaN  Akrotiri and Dhekelia
3  35.40  35.40  35.40  35.40  35.40          ...             NaN   NaN   NaN   NaN                Albania
4  28.82  28.82  28.82  28.82  28.82          ...             NaN   NaN   NaN   NaN                Algeria

[5 rows x 218 columns]

'''