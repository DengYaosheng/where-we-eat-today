# gps_module.py
from gps3 import gps3

def get_current_location():
    """
    获取当前的GPS位置，返回一个包含纬度和经度的元组 (latitude, longitude)。
    """
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
                return latitude, longitude

    return None  # 如果无法获取位置，返回None
