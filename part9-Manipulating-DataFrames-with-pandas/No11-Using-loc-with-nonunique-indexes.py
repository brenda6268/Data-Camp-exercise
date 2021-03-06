#Using .loc[] with nonunique indexes
'''
As Dhavide mentioned in the video, it is always preferable to have a meaningful index that uniquely identifies each row. Even though pandas does not require unique index values in DataFrames, it works better if the index values are indeed unique. To see an example of this, you will index your sales data by 'state' in this exercise.

As always, begin by printing the sales DataFrame in the IPython Shell and inspecting it.

Instructions
100 XP
Instructions
100 XP
Set the index of sales to be the column 'state'.
Print the sales DataFrame to verify that indeed you have an index with state values.
Access the data from 'NY' and print it to verify that you obtain two rows.
'''

# Code
# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc[('NY')])

'''result

      month  eggs  salt  spam
state                         
CA         1    47  12.0    17
CA         2   110  50.0    31
NY         1   221  89.0    72
NY         2    77  87.0    20
TX         1   132   NaN    52
TX         2   205  60.0    55
       month  eggs  salt  spam
state                         
NY         1   221  89.0    72
NY         2    77  87.0    20

'''