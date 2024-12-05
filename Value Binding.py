from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('Reprobaste?', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'Contabilidad', 2: 'Quimica', 3: 'Proramacion orientada a objetos'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()