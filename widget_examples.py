from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, StringProperty
from kivy.lang import Builder

Builder.load_file("widget_examples.kv")


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    # slider_value_txt = StringProperty("50")
    text_input_str = StringProperty("foo")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
        else:
            print("Counting is disabled")

    def on_toggle_button_state(self, widget):
        print("Toggle State: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #     print("Slider: " + str(int(widget.value)))
    #     self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        print("Input: " + widget.text)
