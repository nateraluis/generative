import py5
import random
import time

colors = {'1': '#E84855',
          '2': '#F4777A',
          '3': '#FFA69E',
          '4': '#FEC775',
          '5': '#FDE74C',
          '6': '#D3D973',
          '7': '#A8CB9B',
          '8': '#F8C44E',
          '9': '#9EC8A5',
          '0': '#7EBDC2'}
text_color = '#231F20'
background = 255

width_canvas = 840
height_canvas = 950


def setup():
    """Setup the canvas"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.color_mode(py5.HSB)
    py5.no_fill()


def draw():
    """Make the drawing"""
    start_x = 0
    start_y = 0
    start_time = time.time()
    now = start_time
    for start_y in range(20, 820, 50):
        for start_x, i in zip(range(20, 820, 50), str(now)):
            if i != '.':
                color = colors.get(i)
                py5.fill(color, 255)
                py5.stroke_weight(5)
                py5.stroke(255, 255)
                py5.square(start_x, start_y, 50)
            else:
                py5.fill(text_color, 250)
                py5.no_stroke()
                py5.ellipse(start_x+25, start_y+25, 15, 15)
        time.sleep(random.randint(1, 10))
        now = time.time()
    my_font = py5.create_font("MesloLGS-NF-Regular", 32)
    py5.text_font(my_font)
    py5.text_size(33)
    py5.text_align(py5.LEFT, py5.BOTTOM)
    py5.fill(text_color)
    py5.text(int(now), 20, 900)
    py5.fill(text_color, 70)
    py5.text_size(12)
    py5.text("@natera", 20, 920)
    py5.save(f'20230718_time/time_{int(now)}.png')
    py5.no_loop()


py5.run_sketch()
