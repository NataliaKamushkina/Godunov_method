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

app.layout = html.Div([
    html.H1("Построение точного решения задачи Римана", style={
        'textAlign': 'center',
        'color': 'blue'
    }),
    html.H3("Для данных на вход"),
    html.Div([
    "left_pressure: ",
    dcc.Input(id="text-input1", type="text", placeholder = left_pressure), 
    html.Br(),
    "left_density:  ",
    dcc.Input(id="text-input2", type="text", placeholder = left_density),
    html.Br(),
    "left_velocity: ",
    dcc.Input(id="text-input3", type="text", placeholder = left_velocity),
    html.Br(),
    "right_pressure: ",
    dcc.Input(id="text-input4", type="text", placeholder = right_pressure), 
    html.Br(),
    "right_density: ",
    dcc.Input(id="text-input5", type="text", placeholder = right_density),
    html.Br(),
    "right_velocity: ",
    dcc.Input(id="text-input6", type="text", placeholder = right_velocity),
    html.Br(),

    html.Div(id='PRINTOUTPUT'),
    html.Button('Ok', id='create_button')
], className="t3_fon",
    ),
    html.H3("Для графиков"),
    html.Div([
"График: ",
        ], className="t3_fon",
    ), 
])

@app.callback(Output('PRINTOUTPUT', 'children'),
              [Input('create_button', 'n_clicks'),
              Input('selection_tabs', 'value')],
              [State('text-input', 'value')])

def xyz(clicks, selected_tab, textinput):    

    changed_ids = [p['prop_id'].split('.')[0] for p in dash.callback_context.triggered]
    button_pressed = 'create_button' in changed_ids

    if not button_pressed:
        return ""

    if textinput == "":           
        return "No input"
    
    return "Successful"

#################################################

if __name__ == '__main__':
    app.run_server(debug=True)