"""
lattice by Luis Natera
"""

import py5

width_canvas = 900
height_canvas = 950
background = 255


def setup():
    """Provides the setup for py5. It only runs once"""
    # py5.full_screen()
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.frame_rate(3)


def _draw_edges(x_min, x_max, y_min, y_max):
    # Edges
    py5.stroke(0)
    py5.stroke_weight(3)
    if py5.random_int(0, 1):
        py5.line((x_max+x_min)/2, y_min, (x_max+x_min)/2, y_max)
    if py5.random_int(0, 1):
        py5.line((x_max+x_min)/2, y_min, x_min, (y_max+y_min)/2)
    if py5.random_int(0, 1):
        py5.line(x_min, (y_max+y_min)/2, (x_max+x_min)/2, y_max)
    if py5.random_int(0, 1):
        py5.line((x_max+x_min)/2, y_max, x_max, (y_max+y_min)/2)
    if py5.random_int(0, 1):
        py5.line(x_max, (y_max+y_min)/2, (x_max+x_min)/2, y_min)
    if py5.random_int(0, 1):
        py5.line(x_min, (y_max+y_min)/2, x_max, (y_max+y_min)/2)


def _draw_nodes(x_min, x_max, y_min, y_max):
    # Nodes
    py5.fill(255)
    py5.stroke_weight(3)
    py5.ellipse((x_max+x_min)/2, y_min, 20, 20)
    py5.ellipse((x_max+x_min)/2, y_max, 20, 20)
    py5.ellipse(x_min, (y_max+y_min)/2, 20, 20)
    py5.ellipse(x_max, (y_max+y_min)/2, 20, 20)


def draw_single_motif():
    x_min = 400
    x_max = 500
    y_min = 400
    y_max = 500
    _draw_edges(x_min, x_max, y_min, y_max)
    _draw_nodes(x_min, x_max, y_min, y_max)


def draw():
    """
    Drawing block, the function is run once per frame.
    To make the function only runs once, use no_loop()
    """
    py5.background(background)
    # draw_single_motif()
    for x_min, x_max in zip(range(50, 850, 100), range(150, 900, 100)):
        for y_min, y_max in zip(range(50, 850, 100), range(150, 900, 100)):
            _draw_edges(x_min, x_max, y_min, y_max)
            _draw_nodes(x_min, x_max, y_min, y_max)
    # py5.no_loop()
    py5.fill('#000000', 100)
    py5.text_size(20)
    py5.text("@natera", 50, 925)
    # py5.save_frame("20230922_lattice/images/lattice_02.png", use_thread=True)


py5.run_sketch()
