# to use ipython in terminal, use C:\Python\Scripts\ipython.exe
import pandas
# Can pass in values
df1 = pandas.DataFrame([[1,2,3],[10,20,30]])

# Can label columns
df1 = pandas.DataFrame([[1,2,3],[10,20,30]], columns=["Price", "Age", "Value"])

#And row names
df1 = pandas.DataFrame([[1,2,3],[10,20,30]], columns=["Price", "Age", "Value"], index=["First", "Second"])


# You can also pass dictionaries
df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])
df2=pandas.DataFrame([{"Name":"John","Surname":"Johns"},{"Name":"Jack"}])

# You can perform methods on these columns
#df1.mean()
# Or just get certain columns
#df1.Price
# and perform methods on just that column
#df1.Price.mean()

# Indexing and Slicing
#df1= df1.set_index("Price")
df1.loc[:]
print(df1.set_index("Value"))

#   Use for both index and column values
#   look in df_test for better example
#   loc gets sections of the matrix that you choose based on values in []
print(df1.loc[:,"Price"])

# convert from dataframe to list
list(df1.loc[:,"Price"])

# use iloc to access by indexes
df1.iloc[1,1]
df1.iloc[:,1:2]

# ix allows you access based on rows and indexes
# but you should stick with loc or iloc for more explicit usage of funtions
df1.ix[1,"Price"]

# Deleting Columns and Rows
#df1.drop(1,0)
df1.drop(df1.columns[:1],1)
df1.drop(df1.index[:1],0)

# Updating and Adding new columns and Rows
# values being added must be same length as current dataframe
df1["Other"] = [1,2]
print(df1)
print(df1.index)
print(df1.columns)
