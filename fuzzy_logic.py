import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

temperature = ctrl.Antecedent(np.arange(0,41,1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0,101,1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0,5.01,0.01), 'fan_speed')

temperature['cold'] = fuzzy.trimf(temperature.universe, [0,0,10])
temperature['normal'] = fuzzy.trimf(temperature.universe, [10,20,30])
temperature['hot'] = fuzzy.trimf(temperature.universe, [30,40,40])

humidity['dry'] = fuzzy.trimf(humidity.universe, [0,0,40])
humidity['moderate'] = fuzzy.trimf(humidity.universe, [40,60,75])
humidity['humid'] = fuzzy.trimf(humidity.universe, [75,100,100])

fan_speed['low'] = fuzzy.trimf(fan_speed.universe, [0,0,1.78])
fan_speed['medium'] = fuzzy.trimf(fan_speed.universe, [1.78,2.5,3.5])
fan_speed['high'] = fuzzy.trimf(fan_speed.universe, [3.5,5,5])


rule1 = ctrl.Rule(temperature['low'], fan_speed['slow'])
rule2 = ctrl.Rule(temperature['moderate'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'], fan_speed['fast'])

fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)

fan_simulation.input['temperature'] = 40
fan_simulation.compute()

print("Optimal Fan Speed: ", fan_simulation.output['fan_speed'])