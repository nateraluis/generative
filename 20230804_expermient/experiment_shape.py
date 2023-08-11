import py5
import random


width_canvas = 900
height_canvas = 900

background = '#FFFFFF'

lines = 20

factor = 1



def setup():
    """Setup the canvas"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.color_mode(py5.HSB)
    py5.blend_mode(py5.MULTIPLY)
    py5.frame_rate(10)


def draw():
    randomize = False
    draw_black = True
    draw_cyan = True
    draw_yellow = True
    draw_magenta = True
    py5.background(background)
    for y in range(50, 830, 80):
        start_point_cyan = y
        end_point_cyan = y + 60
        start_point_yellow = y
        end_point_yellow = y + 60
        start_point_magenta = 50
        end_point_magenta = 110
        for x in range(50, 830, 80):
            start_point_k = x
            end_point_k = x + 60
            mid_x_k = random.randint(5, 60) + x
            mid_y_k = random.randint(5, 75) + y
            mid_y_cyan = random.randint(5, 60) + y
            mid_x_cyan = random.randint(40, 75)
            mid_x_cyan += x
            mid_y_yellow = random.randint(5, 60) + y
            mid_x_yellow = random.randint(5, 40)
            mid_x_yellow += x
            mid_y_magenta = random.randint(40, 75) + y
            mid_x_magenta = random.randint(5, 60)
            mid_x_magenta += x
            if x != 50:
                start_point_cyan -= (factor * lines)
                end_point_cyan -= (factor * lines)
                start_point_yellow -= (factor * lines)
                end_point_yellow -= (factor * lines)
                start_point_magenta = x
                end_point_magenta = 60 + x
            if randomize:
                draw_black = random.choice([True, False])
                draw_yellow = random.choice([True, False])
                draw_cyan = random.choice([True, False])
                draw_magenta = random.choice([True, False])

            if draw_black:
                for line in range(lines):
                    points = [
                            [start_point_k, y+80],
                            [mid_x_k, mid_y_k],
                            [end_point_k, y+80]
                            ]
                    py5.no_fill()
                    py5.stroke('#231F20', 75)
                    py5.begin_shape()
                    py5.vertices(points)
                    py5.end_shape()
                    start_point_k += factor
                    end_point_k += factor
                    mid_x_k += factor

            if draw_cyan:
                for line in range(lines):
                    points = [
                            [x, start_point_cyan],
                            [mid_x_cyan, mid_y_cyan],
                            [x, end_point_cyan]
                            ]
                    py5.no_fill()
                    py5.stroke('#00FFFF')
                    py5.begin_shape()
                    py5.vertices(points)
                    py5.end_shape()
                    mid_y_cyan += factor
                    start_point_cyan += factor
                    end_point_cyan += factor

            if draw_yellow:
                for line in range(lines):
                    points = [
                            [x + 80, start_point_yellow],
                            [mid_x_yellow, mid_y_yellow],
                            [x + 80, end_point_yellow]
                            ]
                    py5.stroke('#FFFF00')
                    py5.begin_shape()
                    py5.vertices(points)
                    py5.end_shape()
                    mid_y_yellow += factor
                    start_point_yellow += factor
                    end_point_yellow += factor

            if draw_magenta:
                for line in range(lines):
                    points = [
                            [start_point_magenta, y],
                            [mid_x_magenta, mid_y_magenta],
                            [end_point_magenta, y]
                            ]
                    py5.stroke('#FF00FF')
                    py5.begin_shape()
                    py5.vertices(points)
                    py5.end_shape()
                    start_point_magenta += factor
                    end_point_magenta += factor
                    mid_x_magenta += factor
    # py5.no_loop()
    py5.fill("#231F20", 100)
    py5.text_size(20)
    py5.text("@natera", 50, 880)
    # py5.save('20230804_expermient/cmyk_m.png')


py5.run_sketch()
