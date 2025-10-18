from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label

# Настройки окна
Window.size = (360, 640)
Window.clearcolor = (0/255, 0/255, 0/255, 1)  # Черный фон
Window.title = "Мое приложение"

class MyApp(App):

    def build(self):
        return Label(text = 'Hello world')

if __name__ == '__main__':
    MyApp().run()