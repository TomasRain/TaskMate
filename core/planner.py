"""
任务拆解与规划模块
使用 DeepSeek 大模型，根据用户画像和环境生成每日任务规划
"""

from typing import List, Dict
from core.deepseek import call_deepseek  # 👈 引入大模型接口调用函数

def generate_plan(user_input: str, user_profile: Dict, location: str = "", weather: str = "") -> List[str]:
    """
    调用大模型生成7日任务计划文本
    :param user_input: 用户自然语言输入（如：我想学习+健身）
    :param user_profile: 用户画像信息（性别、身高、偏好等）
    :param location: 当前城市
    :param weather: 天气描述
    :return: 每日任务计划文本（按行分割的字符串列表）
    """
    # 🧠 拼接 Prompt，用于发送给大模型
    prompt = f"""
你是一名任务规划助手，用户信息如下：
性别：{user_profile.get("gender")}, 身高：{user_profile.get("height")}cm, 体重：{user_profile.get("weight")}kg, 时间偏好：{user_profile.get("preferred_time")}
当前城市：{location}, 当前天气：{weather}

用户目标：{user_input}

请为用户规划接下来7天的每日任务，每天1~2项，合理安排时间段。格式如下：

Day 1：
- xx任务（时间建议：xx）

Day 2：
- ...

任务应简洁、具体，突出学习/锻炼/习惯等类别，语言自然。
    """.strip()

    output_text = call_deepseek(prompt)  # 🚀 发送给 DeepSeek
    return output_text.splitlines()      # 按行拆分，返回列表
