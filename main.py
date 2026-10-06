# -*- coding: utf-8 -*-
"""
简单的 Kivy 示例应用
打包成 APK 后即可在 Android 手机上运行
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.counter = 0

        self.label = Label(text='欢迎使用 yang 的 Python 应用', font_size='20sp')
        self.btn = Button(text='点击计数: 0', size_hint=(1, 0.5))
        self.btn.bind(on_press=self.on_click)

        self.add_widget(self.label)
        self.add_widget(self.btn)

    def on_click(self, instance):
        self.counter += 1
        instance.text = f'点击计数: {self.counter}'


class YangApp(App):
    def build(self):
        self.title = 'Yang Python App'
        return MainLayout()


if __name__ == '__main__':
    YangApp().run()
