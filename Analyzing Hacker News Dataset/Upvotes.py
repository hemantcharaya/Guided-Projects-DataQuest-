# In this File we will analyze how the length of headlines and submission time impact the no. of upvotees on the post
import read 
import times
import pandas as pd 
data = read.load_data("hn_stories.csv")
data["len_head"] = data["headline"].str.len()
fig_1 = plt.figure(figsize =(15,20))

data_agg_len = data.groupby("len_head").upvotes.mean()
data_agg_len = pd.DataFrame({"word_count": data_agg_len.index, "upvotes": data_agg_len.values})
ax_1 = fig_1.add_subplot(2,1,1)
ax_1.plot(data_agg_len["word_count"],data_agg_len["upvotes"], color = "Red")
ax_1.set_xlabel("Word Count of Headline")
ax_1.set_ylabel("Upvotes Count")
ax_1.set_xlim(0,100)

ax_2 = fig_1.add_subplot(2,1,2)
data["hour"] = times.hr_ext(data)
data_agg_hr = data.groupby("hour").upvotes.mean()
print(data_agg_hr)
bar_heights = []
bar_position = []
bar_xticks =[]
for i in data_agg_hr:
    bar_heights.append(i)
for i in range(0,24):
    j = i+0.5
    bar_position.append(j)
for i in range(0,24):
    bar_xticks.append(i+.5)
ax_2.set_xticks(bar_xticks)
ax_2.bar(bar_position, bar_heights, 0.75, color = "black")
ax_2.set_xticklabels(range(0,24))
ax_2.set_xlabel("Hour of the Day")
ax_2.set_ylabel("Mean Upvotes Count")
fig_1.savefig("Figure_2.png")
plt.show()
