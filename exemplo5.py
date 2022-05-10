"""temas"""
import PySimpleGUI
from PySimpleGUI import (Push, Window, Button, Text, Image, Input, Column,
                         VSeparator, popup, theme, theme_previewer)

left_layout = [[Image(filename='avatar.png')]]
right_layout = [
    [Text('e-mail:'), Input(key='-email-')],
    [Text('senha:'), Input(key='-senha-', password_char='*')],
    [Push(), Button('login'), Push(), Push(), Button("Esqueci a senha"),
     Push()]
]
layout = [
    [Column(left_layout),
    VSeparator(),
    Column(right_layout)]
]

theme('DarkPurple4')

window = Window(
    'janela da live de python',
    layout=layout
)
while True:
    event, values = window.read()
    print(event, values)
    match(event):
        case 'login':
            popup("Login realizado com sucesso!")
        case 'esqueci a senha':
            popup(f"seu email é {values['-email-']}")
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()