from kivy.app import App
from kivy.uix.label import Label
from jnius import autoclass

# 获取Java的MainActivity类
MainActivity = autoclass('com.example.gpsapp.MainActivity')

class GPSApp(App):
    def build(self):
        return Label(text="等待GPS数据...")

    def on_start(self):
        # 在应用启动时，调用Java方法以获取GPS数据
        main_activity = MainActivity()
        main_activity.sendLocationToPython = self.receive_location

    def receive_location(self, latitude, longitude):
        # 接收来自Java的GPS数据
        print(f"接收到的GPS位置: 纬度: {latitude}, 经度: {longitude}")
        self.root.text = f"纬度: {latitude}, 经度: {longitude}"

if __name__ == '__main__':
    GPSApp().run()
