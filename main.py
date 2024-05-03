def on_button_pressed_a():
    music.set_volume(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

modifiedNote = 0
raw_acceleration = 0
music.set_volume(30)

def on_forever():
    global raw_acceleration, modifiedNote
    raw_acceleration = pins.map(input.acceleration(Dimension.X), -1023, 1023, 260, 440)
    modifiedNote = raw_acceleration
    led.plot_bar_graph(modifiedNote, 440)
    music.ring_tone(modifiedNote)
basic.forever(on_forever)
