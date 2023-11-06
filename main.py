from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


# class GridLayoutExample(GridLayout):
#     pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None),
                       size=(size, size))
            self.add_widget(b)


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


""" def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="Button 1")
        b2 = Button(text="Button 2")
        b3 = Button(text="Button 3")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""


class MainWidget(Widget):
    pass


class ExtremeWayApp(App):
    pass


ExtremeWayApp().run()
