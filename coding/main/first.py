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
            text='Добро пожаловать!',
            font_size = dp(24),
            bold = True,
            color = (0.3, 0.3, 0.3, 1),  # Темно-серый
            size_hint = (1, 0.3)
        )





        self.add_widget(title) #Такие строки выводят виджеты, которые мы ранее написали в UI




class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()