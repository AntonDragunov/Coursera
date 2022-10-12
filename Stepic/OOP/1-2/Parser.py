# Здесь объявляется класс Factory
class Factory:


    def build_sequence(self):
        return []

    def build_number(self, sub):
        self.sub = sub
        return float(self.sub)

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())