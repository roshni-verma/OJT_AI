import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'MonsoonIntensity': [1, 2, 3, 4, 5],
    'Deforestation': [5, 3, 4, 2, 1],
    'ClimateChange': [2, 4, 1, 3, 5],
    'Siltation': [4, 2, 5, 1, 3],
    'AgriculturalPractices': [3, 5, 2, 4, 1],
    'DrainageSystems': [5, 1, 3, 2, 4],
    'CoastalVulnerability': [1, 3, 2, 5, 4],
    'Landslides': [2, 5, 1, 4, 3],
    'PopulationScore': [3, 4, 5, 1, 2],
    'InadequatePlanning': [4, 2, 3, 5, 1]
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define custom CSS styles
styles = {
    'container': {
        'display': 'flex',
        'flex-direction': 'row',
        'justify-content': 'space-between',
        'width': '80%',
        'margin': '0 auto',
        'font-family': 'Arial, sans-serif'
    },
    'header': {
        'textAlign': 'center',
        'padding': '10px',
        'background-color': '#4CAF50',
        'color': 'white',
        'font-size': '18px',  # Font size for the header
        'border-radius': '5px',
        'margin-bottom': '20px',
        'width': '50%',  # Reduced width for the header
        'margin': '0 auto'  # Center the header horizontally
    },
    'controls': {
        'width': '30%',
        'padding': '10px',
        'border': '1px solid #ddd',
        'border-radius': '5px',
        'margin-right': '20px',
        'background-color': '#f9f9f9'
    },
    'graph': {
        'width': '65%',  # Smaller width for the graph
        'border': '1px solid #ddd',
        'border-radius': '5px',
        'padding': '10px',
        'background-color': '#ffffff'
    }
}

app.layout = html.Div([
    html.Div("Weather Forecast Analysis Dashboard", style=styles['header']),
    html.Div(style=styles['container'], children=[
        # Controls for X-axis, Y-axis, and Chart Type
        html.Div(style=styles['controls'], children=[
            html.Label("Select X-axis:"),
            dcc.Dropdown(
                id='x-axis-dropdown',
                options=[{'label': col, 'value': col} for col in df.columns],
                value='MonsoonIntensity',  # Default value
                clearable=False
            ),
            html.Label("Select Y-axis:"),
            dcc.Dropdown(
                id='y-axis-dropdown',
                options=[{'label': col, 'value': col} for col in df.columns],
                value='Deforestation',  # Default value
                clearable=False
            ),
            html.Label("Select Chart Type:"),
            dcc.Dropdown(
                id='chart-type-dropdown',
                options=[
                    {'label': 'Line Chart', 'value': 'line'},
                    {'label': 'Bar Chart', 'value': 'bar'},
                    {'label': 'Scatter Plot', 'value': 'scatter'}
                ],
                value='line',  # Default value
                clearable=False
            )
        ]),

        # Graph
        html.Div(dcc.Graph(id='chart'), style=styles['graph'])
    ])
])

# Callback to update graph based on dropdown selections
@app.callback(
    Output('chart', 'figure'),
    [Input('x-axis-dropdown', 'value'),
     Input('y-axis-dropdown', 'value'),
     Input('chart-type-dropdown', 'value')]
)
def update_graph(x_axis, y_axis, chart_type):
    if chart_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis,
                      labels={'x': x_axis, 'y': y_axis},
                      title=f'Line Chart of {x_axis} vs {y_axis}')
    elif chart_type == 'bar':
        fig = px.bar(df, x=x_axis, y=y_axis,
                     labels={'x': x_axis, 'y': y_axis},
                     title=f'Bar Chart of {x_axis} vs {y_axis}')
    elif chart_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis,
                         labels={'x': x_axis, 'y': y_axis},
                         title=f'Scatter Plot of {x_axis} vs {y_axis}')
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
