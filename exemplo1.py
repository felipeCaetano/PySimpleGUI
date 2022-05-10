from PySimpleGUI import Window, Button, Text


layout = [
    [Button("Botão 1")],
    [Button("Botão 2")],
    [Text("aperte o botão 3"), Button("Botão 3")],
]

window = Window(
    'janela da live de python',
    size=(400, 400),
    layout=layout
)
print(window.read())
window.close()
