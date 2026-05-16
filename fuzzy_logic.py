import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0,41,1), 'temperature')
fan_speed = ctrl.Consequent(np.arange(0,5.01,0.01), 'fan_speed')

temperature['cold'] = fuzzy.trimf(temperature.universe, [0,0,10])
temperature['normal'] = fuzzy.trimf(temperature.universe, [10,20,30])
temperature['hot'] = fuzzy.trimf(temperature.universe, [30,40,40])

fan_speed['slow'] = fuzzy.trimf(fan_speed.universe, [0,0,1.78])
fan_speed['medium'] = fuzzy.trimf(fan_speed.universe, [1.78,2.5,3.5])
fan_speed['fast'] = fuzzy.trimf(fan_speed.universe, [3.5,5,5])

rule1 = ctrl.Rule(temperature['cold'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['normal'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['hot'], fan_speed['fast'])

fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)

fan_simulation.input['temperature'] = 40
fan_simulation.compute()

print("Optimal Fan Speed: ", fan_simulation.output['fan_speed'])