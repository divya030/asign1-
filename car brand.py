from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    Car_Brand = ObjectProperty(TextInput())
    Fuel_type = ObjectProperty(TextInput())
    Body_type = ObjectProperty(TextInput())
    Colour = ObjectProperty(TextInput())
    # displaying message

    def press(self):
        Car_Brand = self.Car_Brand
        Fuel_type = self.Fuel_type
        Body_type = self.Body_type
        Colour = self.Colour
        print(f"I love a {Colour} {Car_Brand} car of {Body_type} type which runs in {Fuel_type}")
        # self.add_widget(Label(text=f"I love a {color} {brand} car of {body} type which runs in {fuel}"))


class CarListDetailsApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    kv_app = CarListDetailsApp()
    kv_app.run()
