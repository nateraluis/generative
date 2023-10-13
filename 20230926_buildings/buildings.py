"""
buildings by Luis Natera

Provide some description about the script
"""

import py5

width_canvas = 900
height_canvas = 950
background = 255


def setup():
    """Provides the setup for py5. It only runs once"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.frame_rate(7)


def draw_building(x_min, x_max, y_min, y_max):
    py5.stroke(255)
    py5.stroke_weight(1)
    py5.fill(0)
    rect_size = x_max - x_min
    py5.rect(x_min, y_min, rect_size, rect_size)
    x_center = (x_max + x_min) / 2
    tall = y_min + py5.random_int(2, 50)
    py5.line(x_center, tall, x_center, y_max)
    min_width = int((x_max - x_min) / 8)
    max_w = int((x_max - x_min) / 4)
    max_width = py5.random_int(min_width, max_w)
    for i in range(2, max_width, 3):
        py5.line(x_center + i, tall, x_center + i, y_max)
        py5.line(x_center - i, tall, x_center - i, y_max)

    tall = y_min + py5.random_int(50, 100)
    for i in range(i + 2, i + max_width, 3):
        py5.line(x_center + i, tall, x_center + i, y_max)
        py5.line(x_center - i, tall, x_center - i, y_max)

    # py5.line(x_min+0, 50, x_max-0, 150)


def draw():
    """
    Drawing block, the function is run once per frame.
    To make the function only runs once, use no_loop()
    """
    py5.background(background)
    x_min = y_min = 300
    x_max = y_max = 600
    for x_min, x_max in zip(range(50, 850, 100), range(150, 900, 100)):
        draw_building(x_min, x_max, y_min, y_max)
    #     for y_min, y_max in zip(range(50, 850, 100), range(150, 900, 100)):

    # py5.no_loop()
    py5.fill("#000000", 100)
    py5.text_size(20)
    py5.text("@natera", 50, 925)
    # py5.save_frame("20230926_buildings/images/buildings_####.png", use_thread=True)


py5.run_sketch()
