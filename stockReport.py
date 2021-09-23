import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px



df = pd.read_csv("crossover3.csv",index_col=False)
df =df.sort_values(by=['cross_over_date_strong'],ascending=False).head(10)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def genrate_table(dataFrame,max_rows=10):
        return html.Table([
                html.Thead(
                        html.Tr([html.Th(col) for col in dataFrame.columns])
                        ),
                html.Tbody([
                        html.Tr([
                                html.Td(dataFrame.iloc[i][col]) for col in dataFrame.columns
                                ])for i in range(min(len(dataFrame),max_rows))
                        ])
                ])
        
app = dash.Dash(__name__)
app.layout = html.Div(children=
	[html.H1(children="Techincal Indicator",style={
            'textAlign': 'center',
            'color': colors['text'],
            'backgroundColor': colors['background']
        }),
         genrate_table(df)



	]


	)


if __name__ == '__main__':
	app.run_server(debug=True)
