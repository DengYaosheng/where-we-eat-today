# 食堂，启动！
from datetime import datetime, timedelta
import random
from gps_module import get_current_location
from canteen_data import get_canteen_data
from canteen_selector import get_nearest_canteens, choose_canteen

def main():
    # GPS位置
    current_location = get_current_location()
    if current_location is None:
        print("无法获取当前位置，请检查GPS设备。")
        return

    # 食堂的GPS
    canteens = get_canteen_data()

    # 8个食堂
    nearest_canteens = get_nearest_canteens(current_location, canteens)
    
    # 最终食堂
    selected_canteen = choose_canteen(nearest_canteens)
    print(f"最终选择的食堂是: {selected_canteen['name']}")

    # 骰子
    dice_roll = random.randint(1, 6)
    departure_time = datetime.now().replace(hour=17, minute=0, second=0) + timedelta(minutes=dice_roll * 5)
    print(f"你应该在 {departure_time.strftime('%H:%M')} 出发去 {selected_canteen['name']}")

if __name__ == "__main__":
    main()
