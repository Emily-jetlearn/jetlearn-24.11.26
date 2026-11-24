import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly # same as matplotlib but with higher graphical standards
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

covid_dataset = 'data science folder\\covid_data.csv'
data = pd.read_csv(covid_dataset)
print(f'\n Covid Data columns: \n {data.columns} \n')

# selecting specific sets of columns from the original dataset
data = data[["Province_State", "Country_Region", 'Last_Update', 
             'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths',
       'Active']]

#renaming columns

data.columns = ('state','Country','lastUpdate', 'Lat','Long', 'Confirmed',
                'Recovered','Deaths', 'Active')

print(f'covid dataset after renaming columns: \n')
print(f'\n{data.head} \n')

data['state'].fillna(value = '',inplace = True) #makes changes to the actual dataset
'''fillna (value) - will fill any missing value (NaN)
in this "State" column with an empty string ('')
'''

#top ten most effected countries
top10_confirmed = pd.DataFrame(data.groupby("Country")['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
print(f'\ntop 10 confirmed most affected countries: \n {top10_confirmed}\n countries \n')

print(f'\n top ten countries:\n {top10_confirmed.index} \n')

#creating plotly, express scatter plot
figure1 = px.scatter(top10_confirmed,x=top10_confirmed.index,
                     y="Confirmed",size="Confirmed",size_max = 120,
                     color = top10_confirmed.index,
                     title= "Top 10 countries by confirmed cases")
figure1.write_html("Fig1.html",auto_open=True)

#top 10 countries with the highest number of deaths

top10_deaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest().sort_values(ascending=False))
print(f'\n top 10 countries with highest death toll: \n {top10_deaths}\n')

'''fig = px.bar(top10_deaths,x = "Deaths" , y = top10_deaths.index, 
             height = 600, color = "Deaths", orientation = 'h',
             color_continuous_scale = ['deepskyblue','yellow'], title = 'Top 10 Deaths Cases worldwide')

fig.write_html("fig.html", auto_open = True)'''


# top 10 recovered countries

top10_recovered = pd.DataFrame(data.groupby("Country")["Recovered"].sum()
                               .nlargest(10).sort_values(ascending = False))
print(f'\n\ntop 10 countries with the most recovered cases: \n {top10_recovered} \n')

fig3 = px.scatter(top10_recovered, x= top10_recovered.index, 
                       y = "Recovered",size_max = 120,  
                       color = top10_recovered.index,
                       title = 'top 10 countries with the most recovered cases')
fig3.write_html("fig3.html", auto_open = True)


# bar graph of recovered cases

figbar = px.bar(top10_recovered, x = top10_recovered.index, y =  "Recovered", 
                height = 600, color = "Recovered",  
                color_continuous_scale = px.colors.sequential.Viridis,
            title = "top 10 countries with the most recovered")

figbar.write_html("figbar.html", auto_open = True)


#USA top 5 states affected

top_states_US = data["Country"] == "US"
top_states_US = data[top_states_US].nlargest(5, "Confirmed")
print(f'\n Top US states confirmed cases: \n {top_states_US} \n')

# Brazil top 10 states affected

top_Brazil_states = data["Country"] =="Brazil"
top_Brazil_states = data[top_Brazil_states].nlargest(5, "Confirmed")
print(f'\n top 5 states with confirmed cases in Brazil: \n {top_Brazil_states} \n') 


# top confirmed 10 states in India

top_India_states = data["Country"] == "India"
top_India_states = data[top_India_states].nlargest(5, "Confirmed")
print(f'\n top 5 states in India with the most confirmed cases: \n {top_India_states}\n')

#graph 5 states for confirmed and death cases in US
fig4 = go.Figure(data = [go.Bar(name = "Confirmed cases", 
                        y = top_states_US["state"],
                        x = top_states_US["Confirmed"],
                        orientation = 'h'),
        go.Bar(name = "death cases", y = top_states_US["state"],
                    x = top_states_US["Deaths"], 
                    orientation = "h" ) ])
                    
fig4.update_layout(title = "most affected states in US")
fig4.write_html('Fig4.html', auto_open = True )




#top 5 states in Russia with most confirmed cases


