import gamepad
from gamepad import Button

class Test:
    def __init__(self):
        self.message = "hello"
    def test(self):
        print(self.message)

g = gamepad.Gamepad()

a = Button({print: ("hello",)},
           {print: ("world",)})

b = Button({print: ("world",)},
           {print: ("hello",)})

buttons = {0: a, 1: b}

t = Test()
g.add_buttons(buttons)
g.bind_button(0, t.test) 

while True:
    g.tick()