"""exemplo 2 da live."""
from PySimpleGUI import Window, Button, Text, Image, Input

layout = [
    [Image(filename='avatar.png')],
    [Text('e-mail:'), Input()],
    [Text('senha:'), Input()],
    [Button('login'), Button("Esqueci a senha")]
]
window = Window(
    'janela da live de python',
    layout=layout,
    element_justification='c'
)
print(window.read())
window.close()