"""
TMP by Luis Natera

Provide some description about the script
"""

import py5


def setup():
    """Provides the setup for py5. It only runs once"""
    py5.full_screen()


def draw():
    """
    Drawing block, the function is run once per frame.
    To make the function only runs once, use no_loop()
    """

    py5.no_loop()
    py5.save_frame("TMP/images/TMP_####.png", use_thread=True)


py5.run_sketch()
