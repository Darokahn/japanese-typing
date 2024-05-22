import hiraganadata
from gamepad import Gamepad
from gamepad import Button
import selectsound

import math
from pynput import keyboard

DEADZONE = 0.2

class Typer:
    def __init__(self, gamepad):
        hiragana_data = hiraganadata.get_hiragana_data()
        self.consonants, self.vowels = hiragana_data["phonemes"].values()
        self.table = hiragana_data["table"]
        self.axes_0 = [0, 0]
        self.axes_1 = [0, 0]
        gamepad.bind_axis(0, self.axis_0_0)
        gamepad.bind_axis(1, self.axis_0_1)
        gamepad.bind_axis(2, self.axis_1_0)
        gamepad.bind_axis(3, self.axis_1_1)
        gamepad.bind_button(10, self.type_char)
        
    def axis_0_0(self, val):
        self.axes_0[0] = val
    def axis_0_1(self, val):
        self.axes_0[1] = val
    def axis_1_0(self, val):
        self.axes_1[0] = val
    def axis_1_1(self, val):
        self.axes_1[1] = val
        
    def type_char(self):
        x, y = self.axes_0
        mag1 = math.sqrt(x**2 + y**2)
        angle1 = math.degrees(math.atan2(y, x))
        x, y = self.axes_1
        mag2 = math.sqrt(x**2 + y**2)
        angle2 = math.degrees(math.atan2(y, x))
        angles = [angle1, angle2]
        sets = [self.consonants, self.vowels]
        mags = [mag1, mag2]
        i = 0
        while i < len(mags):
            if mags[i] < DEADZONE:
                del mags[i]
                del angles[i]
                del sets[i]
            else:
                i += 1
            
        sound = selectsound.select_sound(angles, sets)
        if sound not in self.table:
            return
        character = self.table[sound]
        type_char(character)

def type_char(char, controller = keyboard.Controller()):
    controller.press(char)
    controller.release(char)
    
z = Button({type_char: [keyboard.Key.backspace]}, {})

g = Gamepad({9: z}) 
t = Typer(g)

while True:
    g.tick()
        