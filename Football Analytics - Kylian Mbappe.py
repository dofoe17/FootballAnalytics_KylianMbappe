#Aim is to rereate 

import pandas as pd 
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch
import understatapi
import matplotlib.font_manager as font_manager


#From Understatapi website 
'''
Endpoint 
UnderstatClient.league 
UnderstatClient.team 
UnderstatClient.player 
UnderstatClient.match 

'''

client = understatapi.UnderstatClient() 

#Lets extratc league data for La Liga in 2024 
league_data = client.league(league='La_Liga').get_match_data(season='2025')

#Run the above to find the ID for Real Madrid matches
shot_data = client.match(match='27324').get_shot_data() 
#print(shot_data['h'][0]) # first shot for the home team in the list

#Now we have the shot data for a Real Madrid match where we can identify Mbappe's player ID 
player_data_KM = client.player(player='3423').get_shot_data() #we now have all the shots for Mbappe

#Put this data into a dataframe
df = pd.DataFrame(player_data_KM)


#We now want to scale the X and Y column to be from 0-100 rather than 0-1 
df['X'] = pd.to_numeric(df['X']) * 100
df['Y'] = pd.to_numeric(df['Y']) * 100

#Statistics 
total_shots = df.shape[0] #shape gives us the number of rows and columns, [0] as we just want total rows
total_goals = df[df['result'] == 'Goal'].shape[0]
total_xG = round(pd.to_numeric(df['xG']).sum(), 0) 
xG_per_shot = round(total_xG / total_shots, 2)
points_average_distance = df['X'].mean() 
#assume length of pitch is 100 meters / 115 yards
actual_average_distance = 115 - (df['X'] * 1.15).mean() 
left_foot_goals = df[(df['result'] == 'Goal') & (df['shotType'] == 'LeftFoot')].shape[0]
right_foot_goals = df[(df['result'] == 'Goal') & (df['shotType'] == 'RightFoot')].shape[0] 
headed_goals = df[(df['result'] == 'Goal') & (df['shotType'] == 'Head')].shape[0] 
penalties = df[(df['result'] == 'Goal') & (df['situation'] == 'Penalty')].shape[0] 


#test = df.to_csv(r'C:\Users\Computer\OneDrive\Python\CSV Output\'Kylian_Mbappe_shots_2025')
#print(total_shots)
#print(total_goals)
#print(total_xG)
#print(xG_per_shot)
#print(points_average_distance)
#print(actual_average_distance)
#print(left_foot_goals)
#print(right_foot_goals)
#print(headed_goals)
#print(penalties)



#Visualisation
background_color = "#050505"

fig = plt.figure(figsize=(8, 12))
fig.patch.set_facecolor(background_color) #setting figure background colour

ax1 = fig.add_axes([0, #where the left corner of fig starts  
                    0.7, #where bottom left corner starts
                    1, #width 
                    0.2 #height
                    ]) 
ax1.set_facecolor(background_color)
ax1.set_xlim(0,1)
ax1.set_ylim(0,1)


#add text to our first figure section 
ax1.text(
    x = 0.5, #essentially the co-ordinates of the text
    y = 0.85, 
    s = 'Kylian Mbappe', 
    fontsize = 20, 
    fontweight = 'bold', 
    color = 'white', 
    ha = 'center'
)

ax1.text(
    x = 0.5, 
    y = 0.70, 
    s = 'Total shots in La Liga 2025', 
    fontsize = 14, 
    fontweight = 'bold', 
    color = 'white', 
    ha = 'center'
)

ax1.text(
    x = 0.25, 
    y = 0.5, 
    s = 'Low Quality Chance', 
    fontsize = 10, 
    fontweight = 'bold', 
    color = 'white', 
    ha = 'center'
)

#Create scatter point between our two pieces of text - repeat 4 times for each cirle on vis
ax1.scatter(
    x = 0.40,
    y = 0.53,
    s = 100, # size value here
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8
)

ax1.scatter(
    x = 0.45,
    y = 0.53,
    s = 200, # size value here
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8
)

ax1.scatter(
    x = 0.50,
    y = 0.53,
    s = 300, # size value here
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8
)

ax1.scatter(
    x = 0.55,
    y = 0.53,
    s = 400, # size value here
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8
)

ax1.scatter(
    x = 0.60,
    y = 0.53,
    s = 500, # size value here
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8
)

ax1.text(
    x = 0.75, 
    y = 0.5, 
    s = 'High Quality Chance', 
    fontsize = 10, 
    fontweight = 'bold', 
    color = 'white', 
    ha = 'center'
)

#now want the add the vis circles for goal/no goal 
ax1.text(
    x = 0.45,
    y = 0.27,
    s = 'Goal',
    fontsize = 10,
    color = 'white',
    ha = 'right'
)
ax1.scatter(
    x = 0.47,
    y = 0.3,
    s = 100, 
    color = 'green',
    edgecolor = 'white',
    linewidth = 0.8,
    alpha = 0.7 # provides a bit of transparency 
)

ax1.scatter(
    x = 0.53,
    y = 0.3,
    s = 100, 
    color = background_color,
    edgecolor = 'white',
    linewidth = 0.8,
)
ax1.text(
    x = 0.55,
    y = 0.27,
    s = 'No Goal',
    fontsize = 10,
    color = 'white',
    ha = 'left'
)


#Plotting the pitch on our visualisation
ax2 = fig.add_axes([0.05, #where the left corner of fig starts  
                    0.25, #where bottom left corner starts
                    0.7, #width 
                    0.5 #height
                    ]) 
ax2.set_facecolor(background_color)


pitch = VerticalPitch(
    pitch_type='opta',
    half=True,
    pitch_color=background_color,
    pad_bottom=0.5, 
    line_color='white', 
    linewidth=0.9,
    axis=True, 
    label=True
)
pitch.draw(ax=ax2) #this adds the pitch to othe second section of the vis

#add the average distance to our vis 
ax2.scatter(
    x = 90,
    y = points_average_distance,
    s = 100,
    color = 'white', 
    linewidth = 0.8
) #this gives us the scatter spot

ax2.plot([90, 90], [100, points_average_distance], color = 'white', linewidth = 2) #this gives us the line
ax2.text(
    x = 90,
    y = points_average_distance - 5,
    s = f'Average Distance:\n{actual_average_distance:.1f} yards',
    fontsize = 10, 
    color = 'white', 
    ha = 'center'
)


for x in df.to_dict(orient='records'):
    pitch.scatter(
        x['X'],
        x['Y'],
        s=300 * pd.to_numeric(x['xG']), 
        color='green' if x['result'] == 'Goal' else background_color,
        ax=ax2,
        alpha=0.7,
        linewidth=0.8,
        edgecolor='white'
    )


ax3 = fig.add_axes([0, #where the left corner of fig starts  
                    0.2, #where bottom left corner starts
                    1, #width 
                    0.05 #height
                    ]) 
ax3.set_facecolor(background_color)

ax3.text(x=0.25, y=0.5, s='Shots', fontsize=16, fontweight='bold', color='white', ha='center')
ax3.text(x=0.25, y=0, s=f'{total_shots}', fontsize=12, fontweight='bold', color='green', ha='center')


ax3.text(x=0.38, y=0.5, s='Goals', fontsize=16, fontweight='bold', color='white', ha='center')
ax3.text(x=0.38, y=0, s=f'{total_goals}', fontsize=12, fontweight='bold', color='green', ha='center')


ax3.text(x=0.53, y=0.5, s='xG', fontsize=16, fontweight='bold', color='white', ha='center')
ax3.text(x=0.53, y=0, s=f'{total_xG:.2f}', fontsize=12, fontweight='bold', color='green', ha='center')

ax3.text(x=0.68, y=0.5, s='xG per Shot ', fontsize=16, fontweight='bold', color='white', ha='center')
ax3.text(x=0.68, y=0, s=f'{xG_per_shot:.2f}', fontsize=12, fontweight='bold', color='green', ha='center')


#Add stats to the right side of the grid
ax4 = fig.add_axes([0.8, #where the left corner of fig starts  
                    0.25, #where bottom starts
                    0.1, #width 
                    0.45 #height
                    ]) 
ax4.set_facecolor(background_color)

ax4.text(x=0.85, y=0.8, s='Right Foot', fontsize=16, fontweight='bold', color='white', ha='center')
ax4.text(x=0.85, y=0.75, s=f'{right_foot_goals}', fontsize=12, fontweight='bold', color='green', ha='center')

ax4.text(x=0.85, y=0.65, s='Left Foot', fontsize=16, fontweight='bold', color='white', ha='center')
ax4.text(x=0.85, y=0.6, s=f'{left_foot_goals}', fontsize=12, fontweight='bold', color='green', ha='center')

ax4.text(x=0.85, y=0.4, s='Penalties', fontsize=16, fontweight='bold', color='white', ha='center')
ax4.text(x=0.85, y=0.35, s=f'{penalties}', fontsize=12, fontweight='bold', color='green', ha='center')

ax4.text(x=0.85, y=0.25, s='Headers', fontsize=16, fontweight='bold', color='white', ha='center')
ax4.text(x=0.85, y=0.2, s=f'{headed_goals}', fontsize=12, fontweight='bold', color='green', ha='center')


plt.show() 