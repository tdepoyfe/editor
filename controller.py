import curses

class Controller():
    "An abstraction to process the input."
    
    def process(self, inp, buf):
        """
        Process the input by acting on the buffer.

        Input is a number coming from curses.
        """
        if inp == curses.KEY_LEFT:
            buf.cursor_left()
        elif inp == curses.KEY_RIGHT:
            buf.cursor_right()
        elif inp == curses.KEY_UP:
            buf.cursor_up()
        elif inp == curses.KEY_DOWN:
            buf.cursor_down()
        elif inp == curses.KEY_BTAB:
            buf.delete_left()
        elif 0 <= inp <= 255:
            buf.write(inp)
