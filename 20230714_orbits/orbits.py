import py5
import math
import time
import random

width_canvas = 900
height_canvas = 1200
width_circle = 900/5
height_circle = 900/5

circle_x = 20
circle_y = 20

background = 255
orbit_color = '#231F20'

colors = ['#7EBDC2', '#FFA69E', '#FDE74C', '#E84855']


def calculate_points(width_circle,
                     height_circle,
                     x_origin,
                     y_origin,
                     num_points):
    """Calculate x points in a cirncunference"""

    radius = min(width_circle, height_circle) / 2
    angle_increment = 2 * math.pi / num_points
    start_angle = random.uniform(0, 2 * math.pi)

    points = []
    for i in range(num_points):
        angle = start_angle + i * angle_increment
        x = x_origin + radius * math.cos(angle)
        y = y_origin + radius * math.sin(angle)
        points.append((x, y))
    return points


def setup():
    """Setup the canvas"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.color_mode(py5.HSB)
    py5.no_fill()


def draw():
    """Make the drawing"""
    py5.background(background)
    for x_origin in range(225, 900, 225):
        for y_origin in range(225, 1000, 225):
            color = random.choice(colors)
            py5.fill(color)
            py5.stroke(color)
            py5.ellipse(x_origin, y_origin, circle_x, circle_y)
            for width_circle in range(100, 250, 50):
                height_circle = width_circle
                num_points = random.randint(1, 3)
                py5.no_fill()
                py5.stroke(orbit_color, 80)
                py5.ellipse(x_origin, y_origin, width_circle, width_circle)
                color = random.choice(colors)
                for x, y in calculate_points(width_circle,
                                             height_circle,
                                             x_origin,
                                             y_origin,
                                             num_points):
                    py5.fill(color)
                    py5.stroke(color)
                    py5.ellipse(x, y, circle_x, circle_y)
                    num_points = random.randint(1, 3)
                    for x, y in calculate_points(circle_x+15,
                                                 circle_y+15,
                                                 x,
                                                 y,
                                                 num_points):
                        color = random.choice(colors)
                        py5.fill(color)
                        py5.stroke(250, 50)
                        py5.ellipse(x, y, circle_x/3, circle_y/3)
    time_sec = int(time.time())
    py5.no_loop()
    my_font = py5.create_font("MesloLGS-NF-Regular", 32)
    py5.text_font(my_font)
    py5.text_size(33)
    py5.text_align(py5.CENTER, py5.BOTTOM)
    py5.fill(orbit_color)
    py5.text("ORBITS", 450, 1100)
    py5.fill(orbit_color, 100)
    py5.text_size(18)
    py5.text(f"{time_sec}", 450, 1120)
    py5.fill(orbit_color, 70)
    py5.text_size(12)
    py5.text("@natera", 450, 1140)
    py5.save(f'orbits_{time_sec}.png')


py5.run_sketch()
