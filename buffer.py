class Buffer():
    "The buffer containing the current text."

    def __init__(self):
        """
        Initializes with a unique empty line.
        """
        # The text is stored in a list of bytearrays, each of which is a line.
        self.data = [bytearray()]
        self.cursor = Cursor()

    def write(self, char):
        "Write the given ASCII character to the buffer."
        if char == ord('\n'):
            self.data.insert(self.cursor.line+1, 
                    self.data[self.cursor.line][self.cursor.column:])
            del self.data[self.cursor.line][self.cursor.column:]
            self.cursor_newline()
        elif char == 127:
            self.delete_left()
        else:
            self.data[self.cursor.line].insert(self.cursor.column, char)
            self.cursor_right()

    def cursor_newline(self):
        "Moves the cursor down once and to the leftmost column."
        self.cursor.line += 1
        self.cursor.column = 0

    def cursor_up(self):
        "Move the cursor up one line. Always stays in range in the buffer."
        if self.cursor.line > 0:
            self.cursor.line -= 1
            col = min(self.cursor.column, len(self.data[self.cursor.line])) 
            self.cursor.column = col

    def cursor_down(self):
        "Move the cursor down one line. Always stays in range in the buffer."
        if self.cursor.line < len(self.data) - 1:
            self.cursor.line += 1
            col = min(self.cursor.column, len(self.data[self.cursor.line])) 
            self.cursor.column = col

    def cursor_left(self):
        "Move the cursor left one time. Always stays in range in the buffer."
        if self.cursor.column > 0:
            self.cursor.column -= 1

    def cursor_right(self):
        "Move the cursor right one time. Always stays in range in the buffer."
        if self.cursor.column < len(self.data[self.cursor.line]):
            self.cursor.column += 1

    def cursor_position(self):
        "Return the current cursor position in the buffer as a tuple (y,x)."
        return self.cursor.line, self.cursor.column

    def delete_left(self):
        "Delete one character to the left of the cursor."
        if self.cursor.column == 0:
            if self.cursor.line != 0:
                # Update cursor
                self.cursor.line -= 1
                self.cursor.column = len(self.data[self.cursor.line])

                # Copy current line to the end of previous one
                line_above = self.data[self.cursor.line]
                old_line = self.data[self.cursor.line + 1]
                line_above.extend(old_line)

                # remove old line
                del self.data[self.cursor.line + 1]
        else:
            self.cursor.column -= 1
            del self.data[self.cursor.line][self.cursor.column]
            

class Cursor():
    """
    The position of the cursor in the buffer. 
    Should always be within the window, caller's responsability.
    """

    def __init__(self):
        "Initialize the cursor at the top left corner."
        self.line = 0
        self.column = 0
