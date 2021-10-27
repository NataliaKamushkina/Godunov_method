import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Markdown('''
        #### Ввод данных
        аааа       
    '''),
#  №1
'''
        dcc.Slider(
            id="slider-circular", min=0, max=20, 
            marks={i: str(i) for i in range(21)}, 
            value=3
        ),
        dcc.Input(
            id="input-circular", type="number", min=0, max=20, value=3
        ),
'''
# Кнопка для ввода даных
        html.Div(dcc.Input(id='input-box', type='text')),
        html.Button('Submit', id='button2'),
        html.Div(id='output-container-button2',
             children='Enter a value and press submit'),
    
#Диапазон для ввода даных
    dcc.RangeSlider(
        count=1,
        min=-5,
        max=10,
        step=0.5,
        value=[-3, 7]
    ),
    dcc.Markdown('''
        #### График
        аааа       
    '''),

# Кнопка для графика
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Показать график', id='button'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    ),
    
# Для  №1
"""
@app.callback(
    Output("input-circular", "value"),
    Output("slider-circular", "value"),
    Input("input-circular", "value"),
    Input("slider-circular", "value"),
)
def callback(input_value, slider_value):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-circular" else slider_value
    return value, value
"""
#########################################
if __name__ == '__main__':
    app.run_server(debug=True)