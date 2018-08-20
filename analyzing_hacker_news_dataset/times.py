import read 
import matplotlib.pyplot as plt
import pandas as pd 
def hr_ext(df_func):
    df_func["submission_time"] = pd.to_datetime(df_func["submission_time"])
    df_func["hour"] = df_func["submission_time"].dt.hour
    return df_func["hour"]

def month_ext(df_func):
    df_func["submission_time"] = pd.to_datetime(df_func["submission_time"])
    df_func["month"] = df_func["submission_time"].dt.month
    return df_func["month"]


df = read.load_data("hn_stories.csv")
ser_hr = hr_ext(df)
ser_month = month_ext(df)
# Articles published in every hour of the day
print(ser_hr.value_counts().sort_values(ascending = False))
# Articles published in every month of the year
print(ser_month.value_counts().sort_values(ascending = False))

no_phr = ser_hr.value_counts().sort_index()
no_pmonth = ser_month.value_counts().sort_index()

fig_1 = plt.figure(figsize=(15,20))
ax_1 = fig_1.add_subplot(2,1,1) 
ax_2 = fig_1.add_subplot(2,1,2) 

bar_heights_1 = []
bar_position_1 = []
bar_xticks_1 =[]
for i in no_pmonth:
    bar_heights_1.append(i)
for i in range(0,12):
    j = i+0.5
    bar_position_1.append(j)
for i in range(0,12):
    bar_xticks_1.append(i+.5)
ax_1.set_xticks(bar_xticks_1)
ax_1.set_xticklabels(["Jan", "Feb","Mar", "Apr", "May","Jun", "Jul", "Aug","Sep", "Oct", "Nov","Dec"], rotation =90)
ax_1.bar(bar_position_1, bar_heights_1, 0.75, color = "red")
ax_1.set_xlabel("Month")
ax_1.set_ylabel("Articles per Month")

bar_heights_2 = []
bar_position_2 = []
bar_xticks_2 =[]
for i in no_phr:
    bar_heights_2.append(i)
for i in range(0,24):
    j = i+0.5
    bar_position_2.append(j)
for i in range(0,24):
    bar_xticks_2.append(i+.5)
ax_2.set_xticks(bar_xticks_2)
ax_2.bar(bar_position_2, bar_heights_2, 0.75, color = "black")
ax_2.set_xticklabels(range(0,24))
ax_2.set_xlabel("Hour")
ax_2.set_ylabel("Articles per hour")

plt.show()
fig_1.savefig("Figure_1.png")




