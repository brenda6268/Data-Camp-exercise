#Plotting time series, datetime indexing
'''
Pandas handles datetimes not only in your data, but also in your plotting.

In this exercise, some time series data has been pre-loaded. However, we have not parsed the date-like columns nor set the index, as we have done for you in the past!

The plot displayed is how pandas renders data with the default integer/positional index. Your job is to convert the 'Date' column from a collection of strings into a collection of datetime objects. Then, you will use this converted 'Date' column as your new index, and re-plot the data, noting the improved datetime awareness. After you are done, you can cycle between the two plots you generated by clicking on the 'Previous Plot' and 'Next Plot' buttons.

Before proceeding, look at the plot shown and observe how pandas handles data with the default integer index. Then, inspect the DataFrame df using the .head() method in the IPython Shell to get a feel for its structure.

Instructions
100 XP
Instructions
100 XP
Use pd.to_datetime() to convert the 'Date' column to a collection of datetime objects, and assign back to df.Date.
Set the index to this updated 'Date' column, using df.set_index() with the optional keyword argument inplace=True, so that you don't have to assign the result back to df.
Re-plot the DataFrame to see that the axis is now datetime aware. This code has been written for you.
'''

# Code
# Plot the raw data before setting the datetime index
df.plot()
plt.show()

# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date)

# Set the index to be the converted 'Date' column
df.set_index('Date',inplace=True)

# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()


'''note
Before proceeding:
In [1]: df.head()
Out[1]: 
   Temperature            Date
0         46.2  20100101 00:00
1         44.6  20100101 01:00
2         44.1  20100101 02:00
3         43.8  20100101 03:00
4         43.5  20100101 04:00


After proceeding:
In [3]: df.head()
Out[3]: 
                     Temperature
Date                            
2010-01-01 00:00:00         46.2
2010-01-01 01:00:00         44.6
2010-01-01 02:00:00         44.1
2010-01-01 03:00:00         43.8
2010-01-01 04:00:00         43.5



'''