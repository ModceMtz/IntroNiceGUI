from nicegui import ui

ui.icon('thumb_up', color='#ca6dd1').classes('text-7xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('ModceMtz').style('color: #ca6dd1; font-family: Georiga; font-size: 12px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()