"""Widgets de Layout"""
from PySimpleGUI import (Push, Window, Button, Text, Image, Input, Column,
    VSeparator)

left_layout = [[Image(filename='avatar.png')]]
right_layout = [
    [Text('e-mail:'), Input()],
    [Text('senha:'), Input(password_char='*')],
    [Push(),Push(), Button('login'), Push(), Push(), Button("Esqueci a senha"),
     Push(), Push()]
]
layout = [
    [Column(left_layout),
    VSeparator(),
    Column(right_layout)]
]
window = Window(
    'janela da live de python',
    layout=layout
)
print(window.read())
window.close()
