from os import system

names = ["Ram", "Krishna"]

for name in names:
    system(f'espeak Hello {name}')


