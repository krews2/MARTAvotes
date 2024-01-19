import pandas as pd
import numpy as np
import plotly.express as px
import json
import dash
from dash import Dash, html, dash_table, callback
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from dash_bootstrap_templates import load_figure_template

iris = px.data.iris()
df=pd.read_excel("/home/krupesh/Documents/python scripts/MARTABiden.xlsx")
f = open('/home/krupesh/Documents/python scripts/Gwinnettvoting.geojson',) 
data = json.load(f) 
geojson = data
app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])


def my_scatter(dist="All"):
    if dist == "All":
        fig = px.scatter(df, x="Percent_Diff", y="Pres_Percentage", color="Can/Bal",size='Total_Diff_Abs',
                      hover_data={'Precinct':True,"Percent_Diff":True,'Pres_Percentage':':.2%'\
                                  ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False},
                               color_discrete_map={"Biden Wins/Marta Loses":"#ff7f0e","Biden Wins/Marta Wins":"green",
                                                  "Biden Loses/Marta Loses":"red"})

        fig.update_layout(
                width=1000,height=600,
                hoverlabel=dict(
                font_color="white",font_size=16,
                    font_family="Rockwell"),
                xaxis=dict(
                    tickformat='.2%'
                ),yaxis=dict(
                    tickformat='.2%'))
        return fig
    else:
        dfdis = df[df['District'].isin([dist])]
        fig = px.scatter(dfdis, x="Percent_Diff", y="Pres_Percentage", color="Can/Bal",size='Total_Diff_Abs',
                      hover_data={'Precinct':True,"Percent_Diff":True,'Pres_Percentage':':.2%'\
                                  ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False},
                               color_discrete_map={"Biden Wins/Marta Loses":"#ff7f0e","Biden Wins/Marta Wins":"green",
                                                  "Biden Loses/Marta Loses":"red"})

        fig.update_layout(
                width=1000,height=600,
                hoverlabel=dict(
                font_color="white",font_size=16,
                    font_family="Rockwell"),
                xaxis=dict(
                    tickformat='.2%'
                ),yaxis=dict(
                    tickformat='.2%'))
        return fig

def my_graph(graph_type="fig2",dis="All"):
    if graph_type is None:
        raise dash.exceptions.PreventUpdate()
    if graph_type == 'fig2':
        if dis == 'All':
            fig2 = px.choropleth(df, geojson=geojson, title="Biden Results and MARTA Results" , color="Can/Bal", 
            locations="Precinct",featureidkey="properties.PRECINCT_N",
                hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'\
                            ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False},
                color_discrete_map={"Biden Wins/Marta Loses":"#FFA836","Biden Wins/Marta Wins":"green",
                                        "Biden Loses/Marta Loses":"red"}
            )
            fig2.update_layout(width=1000,height=600, title_x=0.5)
            fig2.update_geos(fitbounds="locations", visible=True)
            
         
            return fig2
        else:
            dfdis = df[df['District'].isin([dis])]
            fig2 = px.choropleth(dfdis, geojson=geojson, title="Biden Results and MARTA Results" , color="Can/Bal", 
                        locations="Precinct",featureidkey="properties.PRECINCT_N",
                            hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'\
                                        ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False},
                            color_discrete_map={"Biden Wins/Marta Loses":"#FFA836","Biden Wins/Marta Wins":"green",
                                                    "Biden Loses/Marta Loses":"red"}
                        )
            fig2.update_layout(width=1000,height=600, title_x=0.5)
            fig2.update_geos(fitbounds="locations", visible=True)
           
            return fig2
    elif graph_type == 'fig3':
        if dis == 'All':
            fig3 = px.choropleth(df, geojson=geojson, title="% Diff in MARTA Votes vs Biden Votes" ,color="Percent_Diff", 
                        locations="Precinct",featureidkey="properties.PRECINCT_N",color_continuous_scale='Reds_r',
                            hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'
                                        ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False}
                        )
            fig3.update_layout(width=1000,height=600, title_x=0.5, coloraxis_colorbar=dict(
    tickformat=".2%"
        ))
            fig3.update_geos(fitbounds="locations", visible=True)
        
            return fig3
        else:
            dfdis = df[df['District'].isin([dis])]
            fig3 = px.choropleth(dfdis, geojson=geojson, title="% Diff in MARTA Votes vs Biden Votes" ,color="Percent_Diff", 
                        locations="Precinct",featureidkey="properties.PRECINCT_N",color_continuous_scale='Reds_r',
                            hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'
                                        ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False}
                        )
            fig3.update_layout(width=1000,height=600, title_x=0.5, coloraxis_colorbar=dict(
    tickformat=".2%"
        ))
            fig3.update_geos(fitbounds="locations", visible=True)
        
            return fig3
    elif graph_type == 'fig4':
        if dis == 'All':


            fig4 = px.choropleth(df, geojson=geojson, title="Diff in MARTA Votes vs Biden Votes" ,color="Total_Diff", 
                            locations="Precinct",featureidkey="properties.PRECINCT_N",color_continuous_scale='Reds_r',
                            hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'
                                        ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False}
                        )
            fig4.update_layout(width=1000,height=600,title_x=0.5)
            fig4.update_geos(fitbounds="locations", visible=True)
            return fig4
        else:
            dfdis = df[df['District'].isin([dis])]
            fig4 = px.choropleth(dfdis, geojson=geojson, title="Diff in MARTA Votes vs Biden Votes" ,color="Total_Diff", 
                            locations="Precinct",featureidkey="properties.PRECINCT_N",color_continuous_scale='Reds_r',
                            hover_data={'Precinct':True,"Percent_Diff":':.2%','Pres_Percentage':':.2%'
                                        ,'Marta_Percentage':':.2%','Total_Diff':True,"Total_Diff_Abs":False}
                        )
            fig4.update_layout(width=1000,height=600,title_x=0.5)
            fig4.update_geos(fitbounds="locations", visible=True)
            return fig4
    return None



dr1= dcc.Dropdown(id='my_dropdown',
            options=[
                     {'label': 'Can/Bal', 'value': 'fig2'},
                     {'label': 'Percent_Diff', 'value': 'fig3'},
                     {'label': 'Total_Diff', 'value': 'fig4'}
     ],value='fig2',style={'width': '25%','margin-left': '41%'})

dr2= dcc.Dropdown(id='my_df',
            options=[
                     {'label': 'District 1', 'value': 'District 1'},
                     {'label': 'All', 'value': 'All'}
     ],value='All',style={'width': '25%',  'margin-left': '41%'})



graphs= html.Div(
    [html.Div([

                dcc.Graph(id='scatter_graph', figure=my_scatter())],style={"display": "inline-block", "width": "48%"}),
    html.Div([
                dcc.Graph(id='our_graph',figure=my_graph())],style={"display": "inline-block", "width": "48%"})])
                
            
        






drops = html.Div(children=[dr1,dr2])
heading = html.H1("Dash Bootstrap Template Demo", className="bg-primary text-white p-2")

layout =html.Div(
        children=[
        html.H1("MARTA and Biden Votes", style={"text-align": "center"}),
        html.Br(),
        html.Div(graphs),
        
        html.Div(drops)],
        
        style={"padding": "50px","padding-left": "210px"})
       



app.layout = layout

@callback(Output(component_id='scatter_graph', component_property='figure'),
         [Input(component_id='my_df', component_property='value')])

def update_scatter_chart(dist):
    return my_scatter(dist)


@callback(Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')],
    [Input(component_id='my_df', component_property='value')]
)

def update_my_graph(graph_type,dis):
    return my_graph(graph_type,dis)




# Run the app
if __name__ == '__main__':
    app.run(debug=True)