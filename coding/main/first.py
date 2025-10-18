from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp

# Настройки окна
Window.size = (360, 640)
Window.color = (0/255, 0/255, 0/255, 1)  #Черный фон
Window.title = "Re:fit"

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(40)
        self.spacing = dp(20)

        self.create_ui()

    def create_ui(self): #Функция со всеми виджетами

        # Заголовок

        title = Label(
            text = 'Добро пожаловать в Re:FIT!',
            font_size = dp(23),
            bold = True,
            color = (0.3, 0.3, 0.3, 1),  # Темно-серый
            size_hint = (1, 0.15)
        )

        #Подзагаловок

        subtitle = Label(
            text = 'Для того чтобы использовать наше\nприложение вам'
                   ' нужно будет\nввести свои данные',
            font_size = dp(16),
            color = (0.4, 0.4, 0.4, 1),  # Серый
            text_size = (Window.width - dp(80), None),
            halign = 'center',
            size_hint = (1, 0)
        )

        #Кнопка

        register_btn = Button(
            text = 'ПРОДОЛЖИТЬ',
            size_hint = (1, None),
            height = dp(55),
            background_color = (0.2, 0.6, 0.9, 1),
            color = (1, 1, 1, 1),
            font_size = dp(18),
            bold = True
        )

        # Такие строки выводят виджеты, которые мы ранее написали в UI
        self.add_widget(title)
        self.add_widget(subtitle)
        self.add_widget(register_btn)


class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()