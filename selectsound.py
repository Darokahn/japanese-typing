def select_sound(angles, sets):
    sound = ""
    if len(angles) != len(sets):
        Exception("each angle must correspond to a set")
    if len(angles) > 2:
        Exception("len(angles) > 2: current implementation allows at most two joystick angles.")
    for i, angle in enumerate(angles):
        s = sets[i]
        index = get_angle_index(angle, len(s))
        sound += s[index]
        
    return sound

def get_angle_index(angle, length):
    if angle < 0:
        angle = 360 + angle
    print("angle:" + str(angle))
    arc_length = 360 / length
    for i in range(length):
        i = i * arc_length
        print(i)
        if i <= angle <= i + arc_length:
            return int(i / arc_length)
    return None