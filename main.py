import tkinter as tk
from tkinter import ttk, messagebox
import project

def analyze():
    selected_item = cb.get()
    initial_velocity = float(velocity_entry.get())
    angle = float(angle_entry.get())
    if selected_item == "能量":
        messagebox.showinfo("信息", "你选择了研究能量")
        project.energy(initial_velocity, angle)
    elif selected_item == "动量":
        messagebox.showinfo("信息", "你选择了研究动量")
        project.momentum(initial_velocity, angle)
    elif selected_item == "角动量":
        messagebox.showinfo("信息", "你选择了研究角动量")
        project.angle(initial_velocity, angle)
    elif selected_item == "抛体":
        messagebox.showinfo("信息","你选择了研究抛体运动")
        project.project(initial_velocity, angle)
    elif selected_item == "导函数图像":
        messagebox.showinfo("信息","即将为你展示导函数图像")
        project.derive(initial_velocity,angle)
    else:
        messagebox.showerror("错误", "请选择一个选项")

def main():
    global cb, velocity_entry, angle_entry
    root = tk.Tk()
    root.geometry("1000x400")
    root.title("Assignment1:The Physical of Sport")

    information_label = ttk.Label(root,text="This program helps us to analyze different situation in basketball.")
    information_label.pack()
    label = ttk.Label(root, text="请选择要研究的物理量：")
    label.pack()

    cb = ttk.Combobox(root, values=["能量", "动量", "角动量","抛体","导函数图像"])
    cb.pack()

    velocity_label = ttk.Label(root, text="请输入初始速度（m/s）：")
    velocity_label.pack()
    velocity_entry = ttk.Entry(root)
    velocity_entry.pack()

    angle_label = ttk.Label(root, text="请输入投掷角度（度）：")
    angle_label.pack()
    angle_entry = ttk.Entry(root)
    angle_entry.pack()

    button = ttk.Button(root, text="分析", command=analyze)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()



