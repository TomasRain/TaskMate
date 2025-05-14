"""
main.py
TaskMate-AI 主程序入口

功能模块：
- 意图识别
- 用户画像读取
- 定位与天气感知
- 历史任务记忆
- 调用 DeepSeek 大模型生成7日任务计划
"""

from core.intent import identify_intent
from core.user_profile import get_user_profile
from core.tools import get_location, get_weather
from core.planner import generate_plan
from core.memory import load_memory, save_memory

def main():
    print("=" * 60)
    print("TaskMate-AI 智能任务规划系统")
    print("请按照提示输入任务目标，系统将为您生成合理的7日计划")
    print("=" * 60)

    # 用户输入任务目标（自然语言）
    user_input = input("请输入您的任务目标（例如：我想复习人工智能并锻炼）：\n> ")

    # 模块一：意图识别（主要用于内部展示）
    intent = identify_intent(user_input)
    print(f"\n识别到的主要任务意图：{intent}\n")

    # 模块二：获取用户画像信息
    profile = get_user_profile()
    print(f"用户画像信息：{profile}\n")

    # 模块三：定位与天气感知
    location = get_location()
    weather = get_weather(location)
    print(f"当前定位：{location}；天气情况：{weather}\n")

    # 模块四：读取历史任务（如有）
    memory = load_memory()
    if 'last_plan' in memory:
        print("上一轮任务计划摘要：")
        for line in memory['last_plan'][:3]:
            print(f"- {line}")
        print("......\n")

    # 模块五：调用大模型进行计划生成
    print("正在生成7日任务计划，请稍候...\n")
    plan = generate_plan(user_input, profile, location, weather)

    # 模块六：输出任务计划
    print("系统已为您生成以下任务安排：\n")
    for line in plan:
        print(line)

    # 模块七：将当前计划存入长期记忆
    memory['last_plan'] = plan
    save_memory(memory)

    print("\n当前任务计划已保存，感谢使用 TaskMate-AI。")

if __name__ == "__main__":
    main()
