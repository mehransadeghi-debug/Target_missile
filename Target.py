import tkinter as tk
from tkinter import ttk
import threading
import time

def start_progress():
    # در یک thread جداگانه اجرا می‌کنیم تا GUI فریز نکنه
    def run():
        progress['value'] = 0  # شروع از 0
        for i in range(101):
            progress['value'] = i
            percent_label.config(text=f"{i}%")
            root.update_idletasks()  # آپدیت GUI بدون فریز کردن
            time.sleep(0.05)  # سرعت پیشرفت — هر 0.05 ثانیه 1%
        status_label.config(text="✅ تکمیل شد!", fg="red")

    # اجرا در thread جداگانه
    threading.Thread(target=run).start()

# ساخت پنجره اصلی
root = tk.Tk()
root.title("Target Missile")
root.geometry("600x400")
root.resizable(False, False)

# برچسب بالا
label = tk.Label(root, text="برای شروع نوار پیشرفت، دکمه را بزنید", font=("Arial", 12))
label.pack(pady=20)

# نوار پیشرفت
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

# برچسب درصد
percent_label = tk.Label(root, text="0%", font=("Arial", 16))
percent_label.pack()

# برچسب وضعیت
status_label = tk.Label(root, text="", font=("Arial", 16))
status_label.pack(pady=5)

# دکمه شروع
start_button = tk.Button(root, text="شروع پیشرفت", command=start_progress, bg="#4CAF50", fg="red", font=("Arial", 10), padx=10)
start_button.pack(pady=15)

# اجرای برنامه
root.mainloop()