class WindowDlg:

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not 0 <= width <= 10000:
            pass
        elif width != self.__width:

            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not 0 <= height <= 10000:
            pass
        elif height != self.__height:
            self.__height = height
            self.show()

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")


w = WindowDlg('sdfsdfsdfsdf', 124, 524)
w.show()

w.width = 1205