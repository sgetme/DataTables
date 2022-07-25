from re import sub
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import *
from kivy.uix.scrollview  import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout

import pandas as pd
import numpy as np
import random

Builder.load_string("""


<TableView>:
    id: parent_box
    orientation: 'vertical'
    BoxLayout:
        id: header_box
        size_hint: 1, None
        height: '60dp'
        canvas.before:
            Color: 
                rgba: (0.425, .425, .125, .5)
            Rectangle:
                size: self.size
                pos: self.pos

    ScrollView:
        # AnchorLayout:
        BoxLayout:
            id: table_box
            orientation: 'vertical'
            size_hint_y: None
            height: 1000
            do_scroll_y: True
            anchor_y: 'top'
            canvas.before:
                Color: 
                    rgba: (0.85, .75, .75, .5)
                Rectangle:
                    size: self.size
                    pos: self.pos
            
    BoxLayout:
        id:footer_box 
        size_hint: 1, None
        height: '60dp'
        TextInput:
            multiline: False
            # font_size: 20
            size_hint_x: .8
        Button:
            text: "Search Box"
            size_hint_x: .2

    """)





class TableView(BoxLayout):
    def __init__(self, header = True, row_index = True, search_box = True, search_button = True, **kwargs ):
        self.row_index = row_index
        self.search_box = search_box
        self.search_button = search_button
        self.header = header
        super().__init__(**kwargs)

        if not self.search_box:
            self.ids.footer_box.remove_widget(self.ids.search_box)

        if not self.search_button:
            self.ids.footer_box.remove_widget(self.ids.search_button)
        if not self.header:
            self.remove_widget(self.ids.header_box)

       
    def add_row(self, row):
        tg = GridLayout(cols =len(row), size_hint = (1, None), height = 60, pos_hint = {'top': 1})
        
        with tg.canvas.before:
            (Color((random.random()), (random.random()), random.random(), .24, mode = 'rgba'))
            tg.rect = Rectangle(pos = tg.pos, size = tg.size)

        
         # Listen to size and position changes
        tg.bind(pos=self.update_rect, size=self.update_rect)


        # pushing the table value into the grid widget
        for item in row:
            label = Label(text = str(item), color = (0, 1, 1, 1))
            tg.add_widget(label) 
        
        self.ids.table_box.add_widget(tg)


    def add_header(self, row):
        tg = GridLayout(cols =len(row), size_hint = (1, None), height = 60, pos_hint = {'top': 1})
        
        with tg.canvas.before:
            (Color((random.random()), (random.random()), random.random(), .24, mode = 'rgba'))
            tg.rect = Rectangle(pos = tg.pos, size = tg.size)

        
        # Listen to size and position changes
        tg.bind(pos=self.update_rect, size=self.update_rect)


        # pushing the table value into the grid widget
        for item in row:
            label = Label(text = str(item), color = (0, 1, 1, 1))
            tg.add_widget(label) 
        
        self.ids.header_box.add_widget(tg)

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size

    



