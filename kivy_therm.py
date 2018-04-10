# from Hui Kang and Wu Tong
# no guarantee, no warranty, no dragons 
# use at your own risk

# run this in python2
# your rpi should have kivy installed on python2

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from w1thermsensor import W1ThermSensor
import numpy as np
import time


Builder.load_string('''
<TemperatureReading>
    rows:2
    spacing:10
    padding:20
    BoxLayout:
        cols:4
        Label:
            font_size:20
            text:'Current Time:'
        Label:
            font_size:20
            id:ctime
            text:root.count_time
        Label:
            text:'Prediction Time:'
            font_size:20
        Label:
            id:ptime
            font_size:20
            text:root.pred_time
    BoxLayout:
        cols:4
        Label:
            font_size:20
            text:'Temperature Reading:'
        Label:
            id:temp_read
            font_size:20
            text:'-'
        Label:
            text:'Predicted Temperature:'
            font_size:20
        Label:
            id:temp_pred
            font_size:20
            text:'-'
''')

import time
import numpy as np

class TemperatureReading(GridLayout):
    count_time = StringProperty('0.00')
    pred_time = StringProperty('standby')
    def __init__(self,**kwargs):
        super(TemperatureReading,self).__init__(**kwargs)
        Clock.schedule_interval(self.tick,0)
        self.sensor = W1ThermSensor()
        self.start_time = time.time()
        self.temp_list = []
        self.time_list = []
        self.time_in = 30.
        self.inside = False  # changes to True if it is sensor is in water
        self.predicted = False  # changes to True if it prediction is made

    def tick(self,dt):
        # get time and temperature
        temp = self.sensor.get_temperature()
        current_time = time.time() - self.start_time
        
        # save time and temperature into resp. list
        self.time_list.append(time)
        self.temp_list.append(temp)
        
        # update time and temp on display
        self.count_time="{:.2f} s".format(current_time)
        self.ids.temp_read.text = "{:.3f} C".format(temp)
        
        # once it is inside the water, set inside as true 
        if np.abs(temp - np.mean(self.temp_list)) > 0.2  and not self.inside:
            self.time_in = current_time
            self.inside = True
        
        # once it has collected enough info
        # make prediction and display
        if current_time > self.time_in + 18. and not self.predicted:
            temp_pred = self.dummy_function(self.time_list, self.temp_list)
            self.ids.temp_pred.text = "{:.3f} C".format(temp_pred)
            pred_time = time.time() - self.start_time -  self.time_in
            self.pred_time = "{:.2f} s".format(pred_time)
            self.predicted = True
        
        # while it is collecting information update prediction time
        if self.inside and not self.predicted:
            self.pred_time = "{:.2f} s".format(current_time - self.time_in)

    
    # your prediction function
    def dummy_function(self, time_list, temp_list):
        # your are required to use a linear regression model
        return 40+10*np.random.randn()


# build app
class TemperatureReadingApp(App):
    def build(self):
        return TemperatureReading()

# run app
TemperatureReadingApp().run()
