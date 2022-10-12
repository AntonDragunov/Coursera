files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']


myset = {c.lower() for c in files if '.png' in c.lower()}

print(*sorted(myset))