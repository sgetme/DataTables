
import math
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout



Builder.laod_string(""" 
<DataTables>:
  Widget:
    canvas.before:
      Color: 
        rgba: (1, 1, 1, 1)
       Rectangle:
        pos: self.pos
        size: self.size
        
 


""")
