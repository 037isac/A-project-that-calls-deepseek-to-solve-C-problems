import tkinter as tk
from tkinter import simpledialog
import os
from datetime import datetime
from openai import OpenAI


def get_code_from_deepseek(prompt):
    client = OpenAI(
        base_url="https://api.deepseek.com",
        api_key="sk-:)"
    )

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[{
            "role": "user",
            "content": f"{prompt}\n请用C++实现最深刻本质的解决方案。要求：\n1. 仅返回代码\n2. 不要注释\n3. 使用现代C++特性\n4. 考虑极端边界条件\n5. 优化时间和空间复杂度\n6. 包含错误处理机制"
        }],
        temperature=0.3,
        stream=False
    )
    return response.choices[0].message.content


def save_code_to_desktop(code):
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"DeepSolution_{timestamp}.cpp"

    with open(os.path.join(desktop, filename), 'w', encoding='utf-8') as f:
        f.write(code.split('```cpp')[-1].split('```')[0].strip())


def main():
    root = tk.Tk()
    root.withdraw()

    user_prompt = simpledialog.askstring("深度问题求解", "请输入需要深度求解的C++编程问题:")
    if user_prompt:
        try:
            code = get_code_from_deepseek(user_prompt)
            save_code_to_desktop(code)
            tk.messagebox.showinfo("成功", f"深度解决方案已保存到桌面")
        except Exception as e:
            tk.messagebox.showerror("错误", f"发生异常: {str(e)}")

    root.destroy()


if __name__ == "__main__":
    main()