import read 
import pandas as pd
df = read.load_data("hn_stories.csv")
long_string = ""
space = " "
for idx, row in df.iterrows():
    if idx == 0:
        long_string = str(row["headline"])
    else:
        long_string = long_string + str(row["headline"]) + space

list_str = long_string.split(" ")
dict_str = {}
for P in list_str:
    if P in dict_str:
        dict_str[P] = dict_str[P] +1
    else:
        dict_str[P] =1 

ser_word = pd.Series(dict_str, name = "count")
ser_word.index.name = "word"
ser_word.reset_index()
ser_word.sort_values(ascending = False, inplace = True)

print(ser_word.head(10))




