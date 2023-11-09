from kivy.app import App
from navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty
from canvas_examples import (
    CanvasExample1, CanvasExample2, CanvasExample3, CanvasExample4,
    CanvasExample5, CanvasExample6, CanvasExample7
)


class MyScreenManager(NavigationScreenManager):
    pass


class ExtremeWayApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExample7()


ExtremeWayApp().run()
