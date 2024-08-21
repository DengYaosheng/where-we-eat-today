from kivy.uix.button import Button

class GPSApp(App):
    def build(self):
        self.label = Label(text="等待GPS数据...")
        return self.label

    def on_start(self):
        # 启动后加载界面元素
        main_activity = MainActivity()
        main_activity.sendLocationToPython = self.receive_location

    def receive_location(self, latitude, longitude):
        # 接收并显示GPS数据
        self.label.text = f"纬度: {latitude}, 经度: {longitude}"
        self.add_button_for_canteen_choice()

    def add_button_for_canteen_choice(self):
        # 添加按钮让用户选择奇数/偶数
        button = Button(text="选择食堂")
        button.bind(on_press=self.choose_canteen)
        self.root.add_widget(button)

    def choose_canteen(self, instance):
        # 用户选择食堂后的逻辑
        pass
