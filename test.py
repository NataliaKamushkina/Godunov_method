"""
Файл  запуском кода
"""
from solver import pressure_solve, InitialApproximationMean, solver
from perfect_gas_state import PerfectGasState
import numpy as np
import dash
import dash_table
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
gamma = 1.4
mol_mass = 0.029

left_pressure = 0.4
left_density = 1
left_velocity = 2

left_gas = PerfectGasState.build_from_pressure_density(left_pressure, left_density, gamma, mol_mass)

right_pressure = 0.4
right_density = 1
right_velocity = -2

right_gas = PerfectGasState.build_from_pressure_density(right_pressure, right_density, gamma, mol_mass)

print(pressure_solve(InitialApproximationMean, left_gas, right_gas, left_velocity, right_velocity))

x_mesh = np.linspace(-2, 2, 200)

times = np.linspace(0, 2, 80)

pressure, density, velocity = solver(
    x_mesh,
    times,
    InitialApproximationMean,
    left_gas,
    right_gas,
    left_velocity,
    right_velocity
)

"""
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20,10))

fig.suptitle('Две ударные волны', fontsize=28)
ax_1 = fig.add_subplot(311)
ax_2 = fig.add_subplot(312)
ax_3 = fig.add_subplot(313)

def plot(index):
    p_max = np.max(pressure)
    p_min = np.min(pressure)
    density_max = np.max(density)
    density_min = np.min(density)
    velocity_max = np.max(velocity)
    velocity_min = np.min(velocity)
    ax_1.clear()
    ax_2.clear()
    ax_3.clear()

    #ax_1.set_ylim(p_min, p_max)
    
    ax_1.set_ylabel("Давление", fontsize=24)
    #ax_2.set_ylim(density_min, density_max)
    ax_2.set_ylabel("Плотность", fontsize=24)
    #ax_3.set_ylim(velocity_min, velocity_max)
    ax_3.set_ylabel("Скорость", fontsize=24)

    ax_1.plot(x_mesh, pressure[index], linewidth=3.0)
    ax_2.plot(x_mesh, density[index], linewidth=3.0)
    ax_3.plot(x_mesh, velocity[index], linewidth=3.0)


from matplotlib import animation

anim = animation.FuncAnimation(fig, plot, interval=200, frames=len(times) - 1)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

anim.save("Две ударные волны.mp4", writer = writer)
"""
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
app.title='Построение точного решения задачи Римана'
"""
app.layout = html.Div(className="tbanner",
    children=[
       html.H1(children='Построение точного решения задачи Римана', style={
        'textAlign': 'center',
        'color': 'white'
    }),
"""

dcc.Tabs(id="tabs", value='tab-0', children=[
        dcc.Tab(label='Для данных на вход', value='tab-0')      
    ], className="mainMenu"),
        #html.Div(id='tabs-content'),   
#])

"""
tab_div = html.Div(
    dcc.Tabs(id='selection_tabs', value='tab-1', children=[
        dcc.Tab(label='Tab one', value='tab-1'),
        dcc.Tab(label='Tab two', value='tab-2'),
]))
"""
app.layout = html.Div(children=[
    html.H1(children='Test app'),
   # tab_div,
    dcc.Input(id="text-input", type="text", placeholder=""),
    html.Div(id='PRINTOUTPUT'),
    html.Button('Click me', id='create_button')
])

@app.callback(Output('PRINTOUTPUT', 'children'),
              [Input('create_button', 'n_clicks'),
              Input('selection_tabs', 'value')],
              [State('text-input', 'value')])

def xyz(clicks, selected_tab, textinput):    

    #To determine if n_clicks is changed. 
    changed_ids = [p['prop_id'].split('.')[0] for p in dash.callback_context.triggered]
    button_pressed = 'create_button' in changed_ids

    if not button_pressed:
        return ""

    if textinput == "":           
        return "No input"
    
    return "Successful"

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-0':
        return html.Div([ dcc.Textarea(placeholder='Введите Ваш текст...',value='Здесь можно оставить заметки',style={'width': '20%', 'height': '30%', 'display': 'block','margin': '0 auto'}),  
            
    html.H1(children=[
            dcc.Markdown('''
 # Для данных на вход
'''), 
#dcc.Textarea(placeholder='Введите Ваш текст...',value='...',style={'width': '20%', 'height': '30%', 'display': 'block','margin': '0 auto'})
  ], className="t3_fon"),
        html.H1(children=[
            dcc.Markdown('''
 # Для картинок/ Нарисовать график
'''), 
#dcc.Textarea(placeholder='Введите Ваш текст...',value='...',style={'width': '20%', 'height': '30%', 'display': 'block','margin': '0 auto'})
  ], className="t3_fon"),
html.Ul(id='imglist',children=[
        #html.Li([html.A(href="", children=[html.Img(src='https://roomester.ru/wp-content/uploads/2019/02/kak-ukrasit-stol-2-18.jpg')])]),            
    ], #className = "tr_fon"
    )

        ]),
@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('btn-nclicks-1', 'n_clicks'),
    Input('btn-nclicks-2', 'n_clicks'),
    Input('btn-nclicks-3', 'n_clicks')
)
def displayClick(btn1, btn2, btn3):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if 'btn-nclicks-1' in changed_id:
        msg = 'Button 1 was most recently clicked'
    elif 'btn-nclicks-2' in changed_id:
        msg = 'Button 2 was most recently clicked'
    elif 'btn-nclicks-3' in changed_id:
        msg = 'Button 3 was most recently clicked'
    else:
        msg = 'None of the buttons have been clicked yet'
    return html.Div(msg)
#################################################

if __name__ == '__main__':
    app.run_server(debug=True)