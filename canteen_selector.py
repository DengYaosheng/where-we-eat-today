import random
from geopy.distance import geodesic

def get_nearest_canteens(current_location, canteens):
    """
    根据当前的GPS位置计算最近的8个食堂，并按距离排序。
    """
    canteens_with_distance = []
    for canteen in canteens:
        distance = geodesic(current_location, canteen["location"]).meters
        canteens_with_distance.append((canteen, distance))
    
    # 按距离排序
    canteens_with_distance.sort(key=lambda x: x[1])
    return [canteen[0] for canteen in canteens_with_distance[:8]]

def choose_canteen(canteens):
    """?
    """
    while len(canteens) > 1:
        # python2 支持？
        choice = random.sample(canteens, 2)
        print(f"选择：奇数 -> {choice[0]['name']}, 偶数 -> {choice[1]['name']}")
        
        # 奇数偶数
        user_input = input("输入奇数或偶数 (输入1代表奇数，输入2代表偶数): ")
        if user_input == '1':
            canteens.remove(choice[1])
        else:
            canteens.remove(choice[0])
    
    return canteens[0]
