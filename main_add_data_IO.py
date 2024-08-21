from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from jnius import autoclass

MainActivity = autoclass('com.example.gpsapp.MainActivity')

class GPSApp(App):
    def build(self):
        self.label = Label(text="等待GPS数据...")
        self.root = self.label
        return self.label

    def on_start(self):
        main_activity = MainActivity()
        main_activity.sendLocationToPython = self.receive_location

    def receive_location(self, latitude, longitude):
        self.label.text = f"纬度: {latitude}, 经度: {longitude}"
        self.add_button_for_canteen_choice()

    def add_button_for_canteen_choice(self):
        button = Button(text="选择食堂")
        button.bind(on_press=self.choose_canteen)
        self.root.add_widget(button)

    def choose_canteen(self, instance):
        # 在这里处理食堂选择逻辑
        pass

if __name__ == '__main__':
    GPSApp().run()
