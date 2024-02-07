"""
imaginary_map by Luis Natera

Provide some description about the script
"""

import py5

width_canvas = 900
height_canvas = 950
background = "#f8f0e0"


def setup():
    """Provides the setup for py5. It only runs once"""
    py5.size(width_canvas, height_canvas)
    py5.background(background)
    py5.frame_rate(1)


def draw():
    """
    Drawing block, the function is run once per frame.
    To make the function only runs once, use no_loop()
    """
    seed = py5.random_int(999999)
    py5.random_seed(seed)

    py5.background(background)
    py5.stroke_weight(2)
    for x_origin in range(50, 800, 50):
        y_origin = 50
        for y_origin in range(50, 800, 50):
            if py5.random(1) >= 0.7:
                choice = py5.random_choice([0, 1, 2, 3, 4])
                if choice == 0:
                    number = py5.random_int(1, 33)
                    photo = py5.load_image(f"MapParts/cities/{number}.png")
                elif choice == 1:
                    number = py5.random_int(1, 159)
                    photo = py5.load_image(f"MapParts/hills/{number}.png")
                elif choice == 2:
                    number = py5.random_int(1, 26)
                    photo = py5.load_image(f"MapParts/mountains/{number}.png")
                    for i in range(py5.random_int(1, 3)):
                        number = py5.random_int(1, 26)
                        _photo = py5.load_image(f"MapParts/mountains/{number}.png")
                        py5.image(
                            _photo,
                            x_origin + py5.random_int(-50, 50),
                            y_origin + py5.random_int(-50, 50),
                        )
                elif choice == 3:
                    number = py5.random_int(1, 121)
                    photo = py5.load_image(f"MapParts/towns/{number}.png")
                else:
                    number = py5.random_int(1, 78)
                    photo = py5.load_image(f"MapParts/trees/{number}.png")
                    for i in range(py5.random_int(25, 80)):
                        number = py5.random_int(1, 78)
                        _photo = py5.load_image(f"MapParts/trees/{number}.png")
                        py5.image(
                            _photo,
                            x_origin + py5.random_int(-50, 50),
                            y_origin + py5.random_int(-50, 50),
                        )
                py5.image(
                    photo,
                    x_origin + py5.random_int(-50, 50),
                    y_origin + py5.random_int(-50, 50),
                )
    # py5.no_loop()
    my_font = py5.create_font("MesloLGS-NF-Regular", 32)
    py5.text_font(my_font)
    py5.text_size(33)
    py5.text_align(py5.CENTER, py5.BOTTOM)
    py5.fill(0)
    py5.text(f"The territory is {bin(seed)}", 450, 900)
    py5.fill(0, 100)
    py5.text_size(15)
    py5.text("@natera", 450, 925)
    py5.text_align(py5.RIGHT, py5.BOTTOM)
    py5.text_size(10)
    py5.text("Images source: David Stark", 850, 925)
    # py5.save_frame(f"imaginary_map/images/imaginary_map_{seed}.png", use_thread=True)


if __name__ == "__main__":
    py5.run_sketch()
