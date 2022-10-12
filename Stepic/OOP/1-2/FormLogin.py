from string import ascii_lowercase, digits

# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    #print(CHARS_CORRECT)
    @classmethod
    def check_name(cls, name):
        for i in name:
            if i not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")
            else:
                if 3 <= len(name) <= 50:
                    return True
                else:
                    return False


    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        html1 = f'<p class="login">{self.name}: <input type="text" size={self.size}/>'
        #print(html1)
        return html1


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        for i in name:
            if i not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")
            else:
                if 3 <= len(name) <= 50:
                    return True
                else:
                    return False

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        html2 = f'<p class="login">{self.name}: <input type="text" size={self.size}/>'
        #print(html2)
        return html2


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

