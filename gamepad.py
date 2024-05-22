import pygame
pygame.init()
pygame.event.set_grab(True)
class Gamepad:
    def __init__(self, buttons = None):
        if not buttons:
            buttons = {}
        self.joystick = self.get_joystick()
        
        self.buttons = buttons
        
        self.button_binds = {}
        self.axis_binds = {}
        
    def add_buttons(self, buttons):
        self.buttons.update(buttons)
        
    def modify_button(self, button, index):
        self.buttons[button].change_func(index)
    
    def modify_buttons(self, buttons, indices):
        for count, button in enumerate(buttons):
            self.modify_button(button, indices[count])
        
    def tick(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button in self.buttons:
                    self.buttons[event.button].press()
                if event.button in self.button_binds:
                    func = self.button_binds[event.button]
                    func()
            elif event.type == pygame.JOYBUTTONUP:
                if event.button in self.buttons:
                    self.buttons[event.button].release()
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis in self.axis_binds:
                    func = self.axis_binds[event.axis]
                    func(event.value)
        
    def get_joystick(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYDEVICEADDED:
                    print("joystick added")
                    return pygame.joystick.Joystick(event.device_index)
    
    def bind_button(self, button, func):
        self.button_binds.update({button: func})
    
    def bind_axis(self, axis, func):
        self.axis_binds.update({axis: func})

class Button:
    def __init__(self, on_press_dict, on_release_dict):
        self.on_press_dict = on_press_dict
        self.on_release_dict = on_release_dict
        self.current_on_press = 0
        self.current_on_release = 0
    
    def change_func(self, index):
        self.current_func = index
        
    def press(self):
        funcs = list(self.on_press_dict.items())
        index = self.current_on_press
        func, args = funcs[index]
        func(*args)
        
    def release(self):
        funcs = list(self.on_release_dict.items())
        index = self.current_on_release
        func, args = funcs[index]
        func(*args)
        