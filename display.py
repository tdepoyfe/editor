import curses

class Window():
    "The part of the buffer that is currently visible on screen."

    def __init__(self):
        """
        Initialize the window.
        The view starts at the begining of the buffer.
        """
        self.begin = 0

    def draw(self, buf, screen):
        """
        Draw the visible part of the buffer to the screen.

        The screen should have the basic interface of a curses window.
        """
        # Clear screen
        screen.clear()

        # Get the current screen and cursor info
        (window_height, window_width) = screen.getmaxyx()
        (cursor_line, cursor_column) = buf.cursor_position()

        # Update the window with the new info
        self._update(cursor_line, window_height - 1)

        # Display title
        title = "editor"
        screen.addstr(title.center(window_width), curses.color_pair(8))

        # Display the visible part of the buffer
        end = self.begin + window_height - 1
        vis_data = buf.data[self.begin:end]
        self._write(vis_data, cursor_line, cursor_column, screen, window_width)

        # Draw cursor
        cursor_line_visible = cursor_line - self.begin + 1
        screen.move(cursor_line_visible, cursor_column % window_width)

        screen.refresh()

    def _update(self, cursor_line, height):
        """
        Update the window using the cursor position. 
        """
        if self.begin > cursor_line:
            self.begin = cursor_line
        elif self.begin + height <= cursor_line:
            self.begin = cursor_line - height + 1

    def _write(self, data, cursor_line, cursor_column, screen, window_width):
        "Write the visible part of the text to the string."
        for (ind, line) in enumerate(data):
            screen.move(ind+1, 0)
            if cursor_line == ind:
                self._write_cur_line(line, cursor_column, screen, window_width)
            else:
                self._write_other_line(line, screen, window_width)

    def _write_cur_line(self, line, cursor_column, screen, window_width):
        """
        Write the current line to the screen.

        If the line is too long, display the part of it containing the cursor.
        """
        frame = cursor_column // window_width
        for byte in line[frame * window_width:(frame+1) * window_width]:
            screen.addstr(chr(byte))

    def _write_other_line(self, line, screen, window_width):
        """
        Write a line to the screen.

        If the line is too long, display only the beginning.
        """
        for byte in line[:window_width]:
            screen.addstr(chr(byte))

