# where-we-eat-today

# 要使用gps3库从GPS设备获取当前位置
pip install gps3
需要编写GPSD服务通信以获得GPS数据，如：
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()
for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)
        if hasattr(data_stream.TPV, 'lat') and hasattr(data_stream.TPV, 'lon'):
            latitude = data_stream.TPV['lat']
            longitude = data_stream.TPV['lon']
            print(f"当前的GPS位置: 纬度: {latitude}, 经度: {longitude}")
            ... ... 

# 安装并运行GPSD服务
sudo apt-get install gpsd gpsd-clients
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock

# 适用于移动设备的替代方法

Android/iOS: 在移动设备上，通常会使用原生API来获取GPS数据，如Android的LocationManager或iOS的CoreLocation。这些API更适合移动应用开发，而不是在Python中直接获取。
https://developer.apple.com/documentation/corelocation/cllocationmanager

# Kivy or BeeWare
Kivy可以在Android设备上运行Python代码，同时支持JNI调用。
-pip install kivy

需要首先在Android Studio中创建一个新的Android项目，并设置权限和API调用AndroidManifest.xml.

