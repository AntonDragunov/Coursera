class RenderList:
    def __init__(self, type_list):
        if type_list == 'ol':
            self.type_list = 'ol'

        else:
            self.type_list = 'ul'

    def __call__(self, *args, **kwargs):
        web = []
        s = ''
        for _ in range(len(args[0])):
            #print(args[0][_])
            web.append(f'<li>{args[0][_]}</li>')

        web.insert(0, ('<' + self.type_list + '>'))
        #res = '</' + self.type_list + '>'
        #print(res)
        web.append('</' + self.type_list + '>')
        for i in web:
            s = s + i + '\n'
        #print(s)
        return s


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)


#____________вариант короче
class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list if type_list in ('ul', 'ol') else 'ul'

    def __call__(self, lst, *args, **kwargs):
        return '\n'.join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', lst), f'</{self.type_list}>'])

