
from DataTables import TableView

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout 

table = {"names":['first', 'second', 'third'], 
    'data':  [["mengist", "Getie", "Messele"],
            ['ayele','mamo', 'bekele'],
            ['abebaw', 'molla', 'endalew']]}


Builder.load_string("""




<TableApp>:
	TableView:

	""")




class TableApp(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		row = [1, "hh", 3, 4, 5]

		dt = TableView(row_index=True)
		cols = ["No", "F. Name", "L. Name", "Score", "Grade","Heigt","Age"]
		table = [[1, "Meng", "Gat", 95, "A+",],
				[2, "Kalkida", "Belete", 85, "A"],
				[3, "Leilete", "Aemiro", 83, "A-"],
				[4, "Deere", "Akila", 72, "B"],
				[5, "Ambesaw", "Agesa", 72, "B"],
				[5, "Bigg", "Agesa", 72, "B"],
				[5, "End", "Agesa", 72, "B"],
				
				[6, "Haile", "GEta", 83, "A-"]]

		dt.add_header(cols)
		for row in table:
			row[0] = table.index(row)
			if table[0] != table[table.index(row)]:
				print("Number of Columns do not match")
			dt.add_row(row)

		# dt.add_row(row)
		self.add_widget(dt)

class MyApp(App):
	def build(self):
		return TableApp()

MyApp().run()
