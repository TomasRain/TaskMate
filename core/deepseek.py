"""
用于调用 DeepSeek Chat API，生成任务规划内容。
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def call_deepseek(prompt: str, model: str = "deepseek-chat") -> str:
    """
    调用 DeepSeek 接口进行任务规划生成
    默认 deepseek-chat
    """
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    json_data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你是一名智能任务规划助手"},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=json_data,
            timeout=40  # 设置超时时间为40秒
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[调用DeepSeek失败] {e}"
