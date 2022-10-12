class WordString:

    def __init__(self, string=None):
        self.__words = string
        if string:
            self.__list_words = [a for a in string.split() if a != ' ']
    @property
    def string(self):
        return self.__words

    @string.setter
    def string(self, string):
        self.__list_words = [a for a in string.split() if a != ' ']
        #print(self.__list_words)
        self.__words = string

    def __len__(self):
        return len(self.__list_words)

    def __call__(self, *args, **kwargs):
        return self.__list_words[args[0]]


words = WordString()
words.string = "1 2 3    4 5 6 7"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
