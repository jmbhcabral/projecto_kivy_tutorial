from kivy.app import App
from navigation_screen_manager import NavigationScreenManager
from kivy.properties import ObjectProperty


class MyScreenManager(NavigationScreenManager):
    pass


class ExtremeWayApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager


ExtremeWayApp().run()
