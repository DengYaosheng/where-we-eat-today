import requests

def fetch_canteen_data():
    try:
        # API-自定义, 缺失！
        response = requests.get("https://api.com/canteens")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"无法获取食堂数据: {e}")
        return []

# API-未定义
canteens = fetch_canteen_data()
