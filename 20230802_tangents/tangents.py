import py5
import random

# background = '#292F36'
background = '#FBFBF2'
stroke_circles = '#000000'
stroke_lines = '#848FA5'

width_canvas = 900
height_canvas = 900


def setup():
    """Setup the canvas"""
    py5.size(width_canvas, height_canvas)
    # py5.begin_record(py5.SVG, '20230802_tangents/tangents.svg')
    py5.frame_rate(3)
    py5.background(background)
    py5.color_mode(py5.HSB)
    py5.no_fill()


def draw():
    """Make the drawing"""
    py5.background(background)
    x = random.randint(100, 800)
    x_ = 75
    for y in range(75, 900, 50):
        # py5.no_fill()
        R = (255 - 10) / (800 - 100)
        alpha = (x - 100) * R + 10
        py5.fill(stroke_circles, alpha)
        py5.stroke(stroke_circles)
        if y != 875:
            py5.ellipse(x, y, 50, 50)
            py5.line(x_, y-25, x, y-25)
        elif y == 875:
            py5.line(x_, y-25, 800, y-25)
        x_ = x
        x = random.randint(100, 800)
    # py5.no_loop()
    # py5.end_record()
    # py5.save('20230802_tangents/tangents.png')


py5.run_sketch()
