#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:01:39 2018

@author: hkmac
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
#%%
class firstapp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        self.btn1 = Button(text = 'Begin', font_size=32)
        self.btn1.bind(on_touch_move = self.on_touch_move) # bind Quit button to exit GUI
        self.btn2 = Button(text = 'Quit', font_size=32)
        self.btn2.bind(on_press = self.stop) # bind Quit button to exit GUI
        self.counter = 0
        layout.add_widget(self.btn1)
        layout.add_widget(self.btn2)
        return layout

    def on_touch_move(self,instance,touch):
        if touch.dx > 40:
            self.btn1.text = "Slide right"
        if touch.dx < -40:
            self.btn1.text = "Slide left"

            
#    def on_touch_move(self, touch):
#        self.counter += 1
#        if self.counter%2 == 0:
#            self.btn1.text = 'halp la'
#        else:
#            self.btn1.text = 'help pls'
        

#class Slide(BoxLayout):
#    def on_touch_move(self,touch):
#        if touch.dx > 40:
#            self.ids.slidestxt.text = "Slide right"
#            self.ids.slidestxt.text = "Slide left"

firstapp().run()