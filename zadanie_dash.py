
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
df = pd.read_csv('https://raw.githubusercontent.com/malinowskadominika/PAD/main/winequelity.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H2(children='Zadanie PAD 06 DASH'),
    html.H4(children='Tabela z danymi wina'),
    generate_table(df),
    html.H4(children='Wybierz rodzaj wykresu, który chcesz wyświetlić'),
    html.Div([
        dcc.RadioItems(
                ['Regression', 'Classification'],
                'Regression',
                id='selected_model',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            ) 
    ]),
    html.Div([
        html.H4(id='text1'),
        dcc.Dropdown(
            df.columns,
            'quality',
            id = 'selected_column'
        ),
        dcc.Graph(id="graph")
    ]),


])

@app.callback(
    Output(component_id='text1', component_property='children'),
    Input(component_id='selected_model', component_property='value')
)
def update_tex1(input_value):
    if (input_value == 'Regression'):
        return "Wykres zależności pH od:"
    else:
        return "Wykres zależności zmiennej target od:"


@app.callback(
    Output("graph", "figure"), 
    Input(component_id='selected_column', component_property='value'),
    Input(component_id='selected_model', component_property='value'))    
def update_chart(selected_column, selected_model):
    if selected_model == 'Regression':
        fig = px.scatter(df, x= selected_column, y='pH')
    else:
        fig = px.scatter(df, x = selected_column, y='target')
        
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


 