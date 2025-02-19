# -*- coding: utf-8 -*-

"""

@author: 
    
    We are Group 9:
    
    Mátyás Varga
    mavar24@student.sdu.dk
    
    Mona Petersen Skriver
    moskr24@student.sdu.dk   
    
    Noemi Zurriaga Anglada
    nozur24@student.sdu.dk
    
    Ulrik Thue Rasmussen
    ulras24@student.sdu.dk
    
    
    
    
    
    
    
    
"""


# ---------------------------------------------- #
#                    DASHBOARD 
# ---------------------------------------------- #

# =============================================================================
#   Loading packages and dependencies
# =============================================================================

    


import pandas as pd 

import plotly.express as px
import plotly.graph_objs as go

from dash_holoniq_wordcloud import DashWordcloud 
from collections import Counter

from datetime import date

import dash
from dash import Dash, dcc, html, callback

from dash.dependencies import Input, Output 



# =============================================================================
#   Custom styling 
# =============================================================================


colors = {
    'background': '#0D0D0D', 
    'accent' : '#A6A6A6',  
    'bodytext': '#F2F2F2'}



markdown_text = ''' 
---
A Group 9 Presentation - From Webscraping to Dashboard
---
The visualizations are based on **available data** from this 
[list of doping cases in sport]
(https://en.wikipedia.org/wiki/List_of_doping_cases_in_sport) 
from Wikipedia, the free encyclopedia.
--- 

'''

# =============================================================================
#   Loading data for visualizations
# =============================================================================


    # =========================================================================
    #   Data - Timeline Visualization
    # =========================================================================
 

data = pd.read_csv("group_9_athletes_information.csv", sep=",").dropna()

filter_data = data.query('birthday != "N/A"')

histogram_1 = px.histogram(
  			data_frame= filter_data,             
           	x = "birthday", 
            color= "country",
            color_discrete_sequence=[
                "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
                "beige", "bisque", "black", "blanchedalmond", "blue",
                "blueviolet", "brown", "burlywood", "cadetblue",
                "chartreuse", "chocolate", "coral", "cornflowerblue",
                "cornsilk", "crimson", "cyan", "darkblue", "darkcyan",
                "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
                "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
                "darkorchid", "darkred", "darksalmon", "darkseagreen",
                "darkslateblue", "darkslategray", "darkslategrey",
                "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
                "dimgray", "dimgrey", "dodgerblue", "firebrick",
                "floralwhite", "forestgreen", "fuchsia", "gainsboro",
                "ghostwhite", "gold", "goldenrod", "gray", "grey", "green",
                "greenyellow", "honeydew", "hotpink", "indianred", "indigo",
                "ivory", "khaki", "lavender", "lavenderblush", "lawngreen",
                "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
                "lightgoldenrodyellow", "lightgray", "lightgrey",
                "lightgreen", "lightpink", "lightsalmon", "lightseagreen",
                "lightskyblue", "lightslategray", "lightslategrey",
                "lightsteelblue", "lightyellow", "lime", "limegreen",
                "linen", "magenta", "maroon", "mediumaquamarine",
                "mediumblue", "mediumorchid", "mediumpurple",
                "mediumseagreen", "mediumslateblue", "mediumspringgreen",
                "mediumturquoise", "mediumvioletred", "midnightblue",
                "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
                "oldlace", "olive", "olivedrab", "orange", "orangered",
                "orchid", "palegoldenrod", "palegreen", "paleturquoise",
                "palevioletred", "papayawhip", "peachpuff", "peru", "pink",
                "plum", "powderblue", "purple", "red", "rosybrown",
                "royalblue", "rebeccapurple", "saddlebrown", "salmon",
                "sandybrown", "seagreen", "seashell", "sienna", "silver",
                "skyblue", "slateblue", "slategray", "slategrey", "snow",
                "springgreen", "steelblue", "tan", "teal", "thistle",           
                "tomato",
                "turquoise", "violet", "wheat", "white", "whitesmoke",
                "yellow", "yellowgreen"
                ],
             
            nbins = 629,
            title= "Histogram",
            )

histogram_1.update_layout(

    xaxis_title="Year of birth",
    yaxis_title="Athletes"
    
)

    # =========================================================================
    #   Data - Wordclouds Visualization
    # =========================================================================


df = pd.read_csv("group_9_athletes_information.csv")  


df["sport"] = df["sport"].str.lower()
sport_count = Counter(df["sport"])
sport_data = pd.DataFrame.from_dict(sport_count, orient='index', columns=["count"]).reset_index()  
 

substances = df["substance"]
drug_list = []

for drugs in substances:
    drugs = str(drugs)
    drugs = drugs.lower()
    drugs = drugs.split()
        
    for drug in drugs:        
        drug_list.append(drug.strip("[](){}<>,.-_!@#$%^&*|\\/?;:'\"~`+= "))
        
drug_list_count = Counter(drug_list)  
drug_dataframe = pd.DataFrame.from_dict(drug_list_count, orient='index', columns=["count"]).reset_index()   


substance_data = [
    ["Cannabis", 130],
    ["Cocaine", 88],
    ["Stanozolol", 88],
    ["Steroids", 80],
    ["Nandrolone", 77],
    ["Epo", 75],
    ["Metandienone", 66],
    ["Methylhexaneamine", 60],
    ["Erythropoietin", 56],
    ["Testosterone", 53],
    ["Clenbuterol", 47],
    ["Anabolic", 45],
    ["Furosemide", 38],
    ["Methandienone", 35],
    ["Doping", 33],
    ["Ephedrine", 28],
    ["Boldenone", 25],
    ["Norandrosterone", 21],
    ["Cannabinoids", 20],
    ["Growth Hormone", 38],
    ["Blood", 17],
    ["Methylhexanamine", 17],
    ["Hydroxystanozolol", 14],
    ["hydrochlorothiazide", 12],
    ["methyltrienolone", 12],
    ["prednisone", 12],
    ["drostanolone", 11],
    ["methyltestosterone", 11],
    ["pseudoephedrine", 11],
    ["steroid", 11],
    ["buprenorphine", 10],
    ["prednisolone", 10],
    ["thc", 10],
    ["amphetamine", 9],
    ["amphetamines", 9],
    ["cortisone", 9],
    ["metabolite", 9],
    ["dehydrochlormethyltestosterone", 8],
    ["finasteride", 8],
    ["sibutramine", 8],
    ["benzoylecgonine", 7],
    ["metenolone", 7],
    ["methamphetamine", 7],
    ["clostebol", 6]   
]    
    

sport_data = [
    ["weightlifting", 360],
    ["swimming", 267],
    ["cycling", 174],
    ["football (soccer)", 100],
    ["water polo", 75],
    ["baseball", 61],
    ["wrestling", 47],
    ["tennis", 43],
    ["cricket", 40],
    ["boxing", 36],
    ["mixed martial arts", 32],
    ["cross-country skiing", 26],
    ["volleyball", 24],
    ["ice hockey", 22],
    ["rugby union", 19],
    ["basketball", 17],
    ["kickboxing", 16],
    ["american football", 16],
    ["rugby", 12],
    ["gymnastics", 12],
    ["australian rules football", 12],
    ["rowing", 11],
    ["bodybuilding", 11],
    ["canadian football", 10],
    ["auto racing", 10],
    ["rugby league", 9],
    ["biathlon", 9],
    ["athletics", 9],
    ["bobsleigh", 8],
    ["triathlon", 7],
    ["powerlifting", 7],
    ["motorcycle racing", 6],
    ["diving", 6],
    ["speed skating", 5],
    ["judo", 5],
    ["curling", 4],
    ["canoeing", 4],
    ["ski jumping", 3],
    ["shot put", 3],
    ["shooting", 3],
    ["horse racing", 3],
    ["bobsledding", 3],
    ["beach volleyball", 3],
    ["ten-pin bowling", 2],
    ["sumo wrestling", 2],
    ["strongmen", 2],
    ["sprinting", 2],
    ["snowboarding", 2],
    ["snooker", 2],
    ["rhythmic gymnastics", 2],
    ["modern pentathlon", 2],
    ["hockey", 2],
    ["figure skating", 2],
    ["field hockey", 2],
    ["darts", 2],
    ["association football", 2],
    ["wheelchair rugby", 1],
    ["wheelchair curling", 1],
    ["wheelchair basketball", 1],
    ["track and field athletics", 1],
    ["track and field", 1],
    ["taekwondo", 1],
    ["surfing", 1],
    ["squash", 1],
    ["sport wrestling", 1],
    ["speed skating, long track", 1],
    ["skeleton", 1],
    ["silat", 1],
    ["rugby union (former bodybuilder)", 1],
    ["rugby (nrl)", 1],
    ["pole vaulting", 1],
    ["nordic combined", 1],
    ["muay thai", 1],
    ["mountain biking", 1],
    ["motorcycling", 1],
    ["mma and kickboxing", 1],
    ["lifesaving", 1],
    ["lawn tennis", 1],
    ["kickboxing, muay thai", 1],
    ["kayaking", 1],
    ["jockey", 1],
    ["highland games", 1],
    ["handball", 1],
    ["hammer throwing", 1],
    ["hammer throw", 1],
    ["greco-roman wrestling", 1],
    ["golf", 1],
    ["football", 1],
    ["fencing", 1],
    ["equestrian", 1],
    ["drag racing", 1],
    ["cycling (track)", 1],
    ["canoe sprint", 1],
    ["boccia", 1],
    ["badminton", 1],
    ["athletics (hept)", 1],
    ["alpine skiing", 1]
]    
    


   
    # =========================================================================
    #   Data - Map Visualization
    # =========================================================================
 

df = pd.read_csv("cases_in_countries.csv")

def draw_map(map_df):
    fig = go.Figure(go.Scattermap(
       mode = "markers+text",
       lon = map_df["longitude"].to_list(),
       lat = map_df["latitude"].to_list(),
       marker = {'size': (map_df["case"]*1.2).to_list() },
       text = map_df["country"]))
    return fig


default_fig = draw_map(df)

     









# =============================================================================
#   Initialise app
# =============================================================================

app = dash.Dash(__name__)

# =============================================================================
#   Layout
# =============================================================================

app.layout = html.Div(
     style={'backgroundColor': colors['background']}, children=[ 
                                                               
    # =========================================================================
    #   Content
    # =========================================================================
       
    html.Div(
        'DSK801: Programming for Data Science', 
        style={'textAlign': 'left','color': colors['bodytext'], 
        'fontSize': 13, 'fontFamily': 'sans-serif',
        'padding': '5px'}
        ), 
     
    html.Div(
        [html.Img(src='assets/img_SDU_WHITE_RGB.png',           
        style={'height':'10%', 
               'width':'10%', 
               'padding': '5px'})]
        ), 

    html.H1(
        'Doping in Sports',
        style={'textAlign': 'left', 
               'color': colors['bodytext'],
               'fontSize': 40, 
               'fontFamily': 'monospace', 
               'padding': '5px', 
               'fontWeight': 'bold'}
        ), 
 
    html.Div(
        [dcc.Markdown(children= markdown_text, 
        style={'textAlign': 'left',
               'color': colors['bodytext'],
                'fontSize': 13, 
                'fontFamily': 'sans-serif', 
                'padding': '5px'})]
        ), 
 
    
    
    # =========================================================================
    #   Tab 1 - Timeline
    # =========================================================================   
    dcc.Tabs(id='tabs', value='tab1', children=[
        
        dcc.Tab(label='Timeline', value='tab1', children =[
            
            (html.Div([dcc.Graph(id= "timeline", figure =histogram_1)])), 
            html.Div([dcc.Dropdown(list(set(filter_data["country"])), id= "slider1")]), 
                        dcc.DatePickerRange(
                                           month_format='MMMM Y',
                                           end_date_placeholder_text='MMMM Y',
                                           start_date=date(1930, 1, 1), id="slider2") 
        ]),
        
    # =========================================================================
    #   Tab 2 - Wordcloud for substances
    # =========================================================================
        
        dcc.Tab(label='Wordcloud for Substances', value='tab2', children=[
            
            html.Div([
                
                html.Div([
                    DashWordcloud(
                        id='wordcloud_substance',
                        list=substance_data,
                        width=900, height=600,
                        gridSize=18,
                        color='#9C27B0',
                        backgroundColor='#1B1B1B',
                        shuffle=True,
                        rotateRatio=0.5,
                        shrinkToFit=True,
                        shape='circle',
                        hover=True
                        )
                    ])
                ])
            
            ]),
        
    # =========================================================================
    #   Tab 3 - Wordcloud for sports
    # =========================================================================
    
    
        dcc.Tab(label='Wordcloud for Sports', value='tab3', children=[
            
            html.Div([

                DashWordcloud(
                    id='wordcloud_sport',
                    list=sport_data,
                    width=900, height=600,
                    gridSize=18,
                    color='#f0f0c0',
                    backgroundColor='#001f00',
                    shuffle=True,
                    rotateRatio=0.5,
                    shrinkToFit=True,
                    shape='circle',
                    hover=True
                    )
                ])
            
            ]),

    
    # =========================================================================
    #   Tab 4 - Map
    # =========================================================================

        dcc.Tab(label='Map', value='tab4', children=[ 
            
            html.Div([
            
            dcc.Graph(id='graph1', figure=default_fig), 
            dcc.Slider(df['case'].min(),
            df['case'].max(),
            step=None,
            value=df['case'].min(),
            id='case-slider' ),
                ])
            ])
        ])
    
    ])



# =============================================================================
#   Adding interactivity
# =============================================================================


@callback(
    Output('graph1', 'figure'),
    Input('case-slider', 'value'),
)
def update_map(cases):
    filterd_df = df[df['case'] >= cases]
    return draw_map(filterd_df)


# =============================================================================
#   Run app
# =============================================================================


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)