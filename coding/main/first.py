from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen

# Настройки окна
Window.size = (360, 640)
Window.color = (0/255, 0/255, 0/255, 1)  #Черный фон
Window.title = "Re:fit"



class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(20))

        # Заголовок

        title = Label(
            text = 'Добро пожаловать в Re:FIT!',
            font_size = dp(23),
            bold = True,
            color = (0.3, 0.3, 0.3, 1),  # Темно-серый
            size_hint = (1, 1.35)
        )


        #Подзагаловок

        subtitle = Label(
            text = 'Для того чтобы использовать наше\nприложение вам'
                   ' нужно будет\nввести свои данные',
            font_size = dp(16),
            color = (0.4, 0.4, 0.4, 1),  # Серый
            text_size = (Window.width - dp(80), None),
            halign = 'center',
            size_hint = (1, 0.5)
        )

        #Кнопка

        start_btn = Button(
            text = 'ПРОДОЛЖИТЬ',
            size_hint = (1, None),
            height = dp(55),
            background_color = (0.2, 0.6, 0.9, 1),
            color = (1, 1, 1, 1),
            font_size = dp(18),
            bold = True
        )

        start_btn.bind(on_press = self.go_to_registration)

        # Такие строки выводят виджеты, которые мы ранее написали в UI
        self.add_widget(title)
        self.add_widget(subtitle)
        self.add_widget(start_btn)

        self.add_widget(layout)

    def go_to_registration(self, instance):
        self.manager.current = 'registration'


class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(15))

        # Заголовок регистрации
        title = Label(
            text='Регистрация',
            font_size=dp(24),
            bold=True,
            size_hint=(1, 0.2)
        )

        # Поле для имени
        self.name_input = TextInput(
            hint_text='Введите ваше имя',
            size_hint=(1, None),
            height=dp(50),
            font_size=dp(16)
        )

        # Поле для email
        self.height_input = TextInput(
            hint_text='Введите ваш рост',
            size_hint=(1, None),
            height=dp(50),
            font_size=dp(16)
        )

        # Поле для пароля
        self.weight_input = TextInput(
            hint_text='Введите ваш вес',
            size_hint=(1, None),
            height=dp(50),
            font_size=dp(16),
        )

        # Кнопка регистрации
        register_btn = Button(
            text='ЗАРЕГИСТРИРОВАТЬСЯ',
            size_hint=(1, None),
            height=dp(55),
            background_color=(0.2, 0.8, 0.4, 1),
            color=(1, 1, 1, 1),
            bold = True
        )
        register_btn.bind(on_press = self.register_user)

        # Кнопка назад
        back_btn = Button(
            text='НАЗАД',
            size_hint=(1, None),
            height=dp(55),
            background_color=(0.8, 0.8, 0.8, 1),
            bold = True
        )
        back_btn.bind(on_press = self.go_back)

        layout.add_widget(title)
        layout.add_widget(self.name_input)
        layout.add_widget(self.height_input)
        layout.add_widget(self.weight_input)
        layout.add_widget(register_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def register_user(self, instance):
        name = self.name_input.text
        height = self.weight_input.text
        weight = self.height_input.text

        if name and height and weight:
            print(f"Успешная регистрация: {name}")
            self.manager.current = 'training'
        else:
            print("Заполните все поля!")

    def go_back(self, instance):
        # Возврат на приветственный экран
        self.manager.current = 'welcome'



# ТРЕТИЙ ЭКРАН - Выбор режима тренировок
class TrainingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(15))

        # Заголовок
        title = Label(
            text='Выбор режима тренировок',
            font_size=dp(24),
            bold=True,
            size_hint=(1, 0.2),
            color=(0.2, 0.2, 0.2, 1)
        )

        # Кнопка режима "Начинающий"
        beginner_btn = Button(
            text='НАЧИНАЮЩИЙ\n\n• Легкие упражнения\n• Медленный темп\n• Для новичков',
            size_hint=(1, None),
            height=dp(100),
            background_color=(0.3, 0.7, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size=dp(16)
        )
        beginner_btn.bind(on_press=self.start_beginner)

        # Кнопка режима "Продвинутый"
        advanced_btn = Button(
            text='ПРОДВИНУТЫЙ\n\n• Сложные упражнения\n• Быстрый темп\n• Для опытных',
            size_hint=(1, None),
            height=dp(100),
            background_color=(0.9, 0.6, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=dp(16)
        )
        advanced_btn.bind(on_press=self.start_advanced)

        # Кнопка режима "Профессионал"
        pro_btn = Button(
            text='ПРОФЕССИОНАЛ\n\n• Максимальная нагрузка\n• Высокий темп\n• Для профессионалов',
            size_hint=(1, None),
            height=dp(100),
            background_color=(0.8, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=dp(16)
        )
        pro_btn.bind(on_press=self.start_pro)

        # Кнопка назад
        back_btn = Button(
            text='НАЗАД',
            size_hint=(1, None),
            height=dp(45),
            background_color=(0.8, 0.8, 0.8, 1),
            color=(0.2, 0.2, 0.2, 1)
        )
        back_btn.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(beginner_btn)
        layout.add_widget(advanced_btn)
        layout.add_widget(pro_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def start_beginner(self, instance):
        print("Запуск режима: Начинающий")
        # Здесь можно перейти к тренировке

    def start_advanced(self, instance):
        print("Запуск режима: Продвинутый")
        # Здесь можно перейти к тренировке

    def start_pro(self, instance):
        print("Запуск режима: Профессионал")
        # Здесь можно перейти к тренировке

    def go_back(self, instance):
        self.manager.current = 'registration'

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        # Добавляем экраны
        sm.add_widget(WelcomeScreen(name = 'welcome'))
        sm.add_widget(RegistrationScreen(name = 'registration'))
        sm.add_widget(TrainingScreen(name='training'))
        return sm

if __name__ == '__main__':
    MyApp().run()