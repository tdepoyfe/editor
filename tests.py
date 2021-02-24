import unittest

from buffer import Buffer

class TestBuffer(unittest.TestCase):
    def test_init_empty(self):
        "Test that the buffer is initialized empty"
        buf = Buffer()
        self.assertEqual(buf.data, [b''])

    def test_write_one_line(self):
        "Test that it can write a line of characters in the buffer."
        buf = Buffer()
        text = "Hello, world!"
        for char in text:
            buf.write(ord(char))
        self.assertEqual(buf.data, [b'Hello, world!'])

    def test_write_multiple_lines(self):
        "Test that it can write multiple lines of characters in the buffer."
        buf = Buffer()
        text = "Hello,\nworld!"
        for char in text:
            buf.write(ord(char))
        self.assertEqual(buf.data, [b'Hello,', b'world!'])

    def test_cursor_position(self):
        "Test that the cursor moves when writing text."
        buf = Buffer()
        text = "Hello,\neditor\nworld!"
        for char in text:
            buf.write(ord(char))
        self.assertEqual(buf.cursor_position(), (2, 6))

    def test_move_cursor(self):
        "Test that the cursor can be moved with arrow keys."
        buf = Buffer()
        text = "Hello,\nworld!"
        for char in text:
            buf.write(ord(char))
        buf.cursor_up()

if __name__ == '__main__':
    unittest.main()
