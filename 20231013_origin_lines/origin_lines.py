"""
origin_lines by Luis Natera

Provide some description about the script
"""

import py5

width_canvas = 900
height_canvas = 950
background = 0


def setup():
    """Provides the setup for py5. It only runs once"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.frame_rate(30)


def draw():
    """
    Drawing block, the function is run once per frame.
    To make the function only runs once, use no_loop()
    """
    seed = py5.random_int(999999)
    py5.random_seed(seed)
    for i in range(3):
        py5.background(background)
        py5.stroke(255, 10)
        for y_start in range(50, 850, 100):
            y_end = y_start + 100
            x1s = [py5.random_int(50, 850) for i in range(py5.random_int(1, 5))]
            x2s = [py5.random_int(50, 850) for i in range(py5.random_int(1, 5))]
            for x_end in range(50, 850, 1):
                for x1, x2 in zip(x1s, x2s):
                    py5.line(x1, y_start, x_end, y_end)
                    py5.line(x2, y_end, x_end, y_start)

        py5.fill(255, 100)
        py5.text_size(20)
        py5.text_align(py5.LEFT)
        py5.text("@natera", 50, 880)
        py5.text_align(py5.RIGHT)
        py5.text(f"{i+1}/3", 850, 880)

        py5.save_frame(
            f"20231013_origin_lines/images/origin_lines_{i+1}.png", use_thread=True
        )
    file = open("20231013_origin_lines/images/seed.txt", "w")
    file.write("\nRandom Seed: " + repr(seed))
    file.close()

    py5.no_loop()


py5.run_sketch()
