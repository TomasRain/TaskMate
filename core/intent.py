
from typing import Literal

def identify_intent(user_input: str) -> Literal["study", "exercise", "rest", "chat", "unknown"]:
    input_lower = user_input.lower()
    if any(keyword in input_lower for keyword in ["学习", "复习", "备考", "看书"]):
        return "study"
    elif any(keyword in input_lower for keyword in ["锻炼", "运动", "健身", "跑步"]):
        return "exercise"
    elif any(keyword in input_lower for keyword in ["休息", "放松", "睡觉"]):
        return "rest"
    elif any(keyword in input_lower for keyword in ["聊天", "倾诉", "无聊"]):
        return "chat"
    else:
        return "unknown"
