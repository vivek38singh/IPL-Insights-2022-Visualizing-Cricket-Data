#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


df=pd.read_csv("Book_ipl22_ver_33.csv")
# Print the shape of the DataFrame
print(df.shape)


# In[7]:


# Display the first 10 rows of the DataFrame
df.head(10)


# In[6]:


# Display the summary information of the DataFrame
df.info()


# In[5]:


# Display the last 5 rows of the DataFrame
df.tail(5)


# In[8]:


# Display the descriptive statistics of the DataFrame
df.describe()


# In[11]:


# Show the number of missing values in each column
df.isnull().sum()


# # So there is no null missing value,so that we no need to remove any columns.

# # Now we start Data Analysis and Visulizations

# In[14]:


# calculate the median of the "highscore" column in the DataFrame 'df' and then create a histogram using seaborn.
# Calculate the median of the 'highscore' column.
HighscoreRecords = df['highscore'].median()
print(HighscoreRecords)
sns.histplot(x='highscore',data=df)


# In[53]:


# Create a count plot using seaborn for the 'toss_decision' column
sns.countplot(x='toss_decision',data=df)


# In[82]:


#create a pie chart representing the distribution of "toss_decision" values.

# Count the number of matches for each toss decision
toss_decision_counts = df['toss_decision'].value_counts()

# Plot the pie chart
plt.figure(figsize=(5, 5))
plt.pie(toss_decision_counts, labels=toss_decision_counts.index, autopct="%1.1f%%")
plt.title('Toss Decision Distribution')
plt.show()


# In[52]:


#No of Matches at each Stadium.

venue = df["venue"].value_counts()
label = venue.index
counts = venue.values

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches at each Stadium')
fig.update_traces(hoverinfo='label+percent', 
                  textinfo='value', textfont_size=20)
fig.show()


# In[84]:


# Count the number of matches played by each team
matches_played = pd.concat([df['team1'], df['team2']]).value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
matches_played.plot(kind='bar')
plt.title('Number of Matches Played by Each Team')
plt.xlabel('Team')
plt.ylabel('Matches Played')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[101]:


# Create a box plot to compare first inning and second inning scores
plt.figure(figsize=(8, 6))
plt.boxplot([df['first_ings_score'], df['second_ings_score']])
plt.title('Comparison of First Inning and Second Inning Scores')
plt.xlabel('Inning')
plt.ylabel('Score')
plt.xticks([1, 2], ['First Inning', 'Second Inning'])
plt.show()


# In[20]:


#In which innings the players preformmed well.
ShowResults = go.Figure()

ShowResults.add_trace(go.Bar(
    x=df["venue"],y=df["first_ings_wkts"],
    name='First Innings Wickets', marker_color='red'
))

ShowResults.add_trace(go.Bar(
    x=df["venue"],y=df["second_ings_wkts"],
    name='Second Innings Wickets', marker_color='blue'
))

ShowResults.update_layout(barmode='group', xaxis_tickangle=-45)
ShowResults.show()


# In[26]:


#which team won most of the match in IPL 2022.
ShowResults = px.bar(df, x=df["match_winner"],
            title="Number of Matches Won in IPL 2022")
# Update the bar color to red
ShowResults.update_traces(marker_color='red')
ShowResults.show()


# In[43]:


figure = px.bar(df, x=df["match_winner"], color = "venue",
            title="Teams Performance at diffrent Venues in IPL 2022")
figure.show()


# In[27]:


#top scorers in IPL 2022 with compare to highscore.
ShowResults = px.bar(df, x=df["top_scorer"], y = df["highscore"], 
                color = df["highscore"],
            title="Top Scorers in IPL 2022")
ShowResults.show()


# In[80]:


# Create a scatter plot to compare first inning score and second inning score
plt.figure(figsize=(8, 6))
plt.scatter(df['first_ings_score'], df['second_ings_score'])
plt.xlabel('First Inning Score')
plt.ylabel('Second Inning Score')
plt.title('First Inning Score vs. Second Inning Score')
plt.show()


# In[28]:


#maximum scored match details of first innings
df.loc[df['first_ings_score'].idxmax()]


# In[29]:


#minimum scored match details of first inning
df.loc[df['first_ings_score'].idxmin()]


# In[30]:


#maximum scored match details of second innings
df.loc[df['second_ings_score'].idxmax()]


# In[31]:


#mininmum scored match details of second innings
df.loc[df['second_ings_score'].idxmin()]


# In[37]:


# first 5 players who had got the player of the match.
TOP_5_players=df['player_of_the_match'].value_counts().nlargest(5)
TOP_5_players


# In[38]:


# we have already defined DataFrame 'df' and 'TOP_5_players' contains the top 5 players
# obtained from the 'value_counts' and 'nlargest' operations

# Create the pie chart
PieChart = px.pie(names=TOP_5_players.index, values=TOP_5_players.values,
                  title="Top 5 Players with Most 'Player of the Match' Awards")

# Add player names as labels to the pie chart
PieChart.update_traces(textinfo='label+percent')

# Show the pie chart
PieChart.show()


# In[87]:


# Get the top 10 players with the most Player of the Match awards
top_10_players = df['player_of_the_match'].value_counts().nlargest(10)

# Plot the horizontal bar chart
plt.figure(figsize=(10, 6))
top_10_players.plot(kind='barh')
plt.title('Top 10 Players with Most Player of the Match Awards')
plt.xlabel('Number of Player of the Match Awards')
plt.ylabel('Player Name')
plt.gca().invert_yaxis()
plt.show()


# In[39]:


#top 5 best bowlers in IPL 2022.
top5_bowlers=df['best_bowling'].value_counts().nlargest(5)
top5_bowlers


# In[54]:


# Create a bar plot using seaborn for the top 5 best bowlers
plt.figure(figsize=(10, 6))
sns.barplot(x=top5_bowlers.index, y=top5_bowlers.values)

# Set labels and title
plt.title("Top 5 Best Bowlers in IPL 2022")
plt.xlabel("Player Name")
plt.ylabel("Number of Best Bowling Performances")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.show()


# In[113]:


final_match_details = df[df['stage'] == 'Final']

# Print the details of the final match
print(final_match_details)


# In[ ]:




