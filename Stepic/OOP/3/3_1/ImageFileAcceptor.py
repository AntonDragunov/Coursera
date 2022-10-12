class ImageFileAcceptor:


    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        #print(args[0].split('.'))
        if (args[0].split('.'))[1] not in self.extensions:
            return False
        else:
            #(args[0].split('.'))[1]
            return True


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg', 'png'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]