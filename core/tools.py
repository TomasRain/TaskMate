
import requests
from datetime import datetime



def get_weather(city: str = "北京") -> str:
    return "多云，适宜户外活动"

#def get_location() -> str:
#    return "北京大兴"
def get_location() -> str:
    """
    基于IP地址自动获取城市名
    使用ipapi.co
    """
    try:
        response = requests.get("http://ip-api.com/json", timeout=5)
        data = response.json()
        city = data.get("city")
        #print("状态码：", response.status_code)
        #print("响应内容：", response.text)
        return city if city else "未知城市"
    except Exception:
        return "未知城市"


def get_current_time() -> str:
    """
    获取当前系统时间，格式为 年-月-日 时:分:秒
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")