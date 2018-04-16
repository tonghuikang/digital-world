#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 12:13:26 2018

@author: hkmac
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

#%%
class firstapp(App):
    def build(self):
#        layout = BoxLayout(orientation ='vertical')
#        top_buttons=BoxLayout()
#        layout.add_widget(top_buttons) # <--------
#        top_buttons.add_widget(save=Button(text='Save')
        
        self.label1 = Label(text='Investment Amount')
        self.label2 = Label(text='Years')
        self.label3 = Label(text='Annual Interest Rate')
        self.label4 = Label(text='Future Value')
        self.btn = Button(text = 'Begin', font_size=32)
        self.btn.bind(on_press = self.show_popup)
        
        self.textinput1 = TextInput(text='10000')
        self.textinput2 = TextInput(text='10')
        self.textinput3 = TextInput(text='5')
        self.label5 = Label(text='result')
        
        outsidelayout = BoxLayout(orientation = 'vertical')
        lane1 = BoxLayout(orientation = 'horizontal')
        lane2 = BoxLayout(orientation = 'horizontal')
        lane3 = BoxLayout(orientation = 'horizontal')
        lane4 = BoxLayout(orientation = 'horizontal')
        lane5 = BoxLayout(orientation = 'horizontal')
        
        lane1.add_widget(self.label1)
        lane2.add_widget(self.label2)
        lane3.add_widget(self.label3)
        lane4.add_widget(self.label4)
        lane5.add_widget(self.btn)
        
        lane1.add_widget(self.textinput1)
        lane2.add_widget(self.textinput2)
        lane3.add_widget(self.textinput3)
        lane4.add_widget(self.label5)
        
        outsidelayout.add_widget(lane1)
        outsidelayout.add_widget(lane2)
        outsidelayout.add_widget(lane3)
        outsidelayout.add_widget(lane4)
        outsidelayout.add_widget(lane5)
        
#        self.textinput = TextInput(text='Hello world')
#        self.btn1 = Button(text = 'Begin', font_size=32)
#        self.btn1.bind(on_touch_move = self.on_touch_move) # bind Quit button to exit GUI
#        self.btn2 = Button(text = 'Quit', font_size=32)
#        self.btn2.bind(on_press = self.on_stop) # bind Quit button to exit GUI
#        self.counter = 0
#        layout.add_widget(self.btn2)
        return outsidelayout
    
    def show_popup(self, b):
        inv_amt = float(self.textinput1.text)
        mth_int = float(self.textinput3.text)/1200.
        num_mth = float(self.textinput2.text)
        self.label5.text = "{:.2f}".format(inv_amt * ((1.+mth_int) ** (num_mth * 12)))

        
    
#        self.search=TextInput(multiline=False)
#        self.add_widget(self.search)
#        self.add_widget(Button(text="click",on_press=self.show_popup))

#    def on_touch_move(self,instance,touch):
#        if touch.dx > 40:
#            self.btn1.text = "Slide right"
#        if touch.dx < -40:
#            self.btn1.text = "Slide left"

            
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


