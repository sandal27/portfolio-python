# tkinter（Tool Kit interface）モジュールでGUIを作成
import tkinter as tk
from tkinter import messagebox  # ポップアップ用モジュール

# リマインダーを表示する関数（繰り返し実行）
def show_reminder():
    global job_id
    task = task_entry.get()  # 入力欄からタスクを取得
    if task:  # タスクが空でなければ表示
        messagebox.showinfo("リマインダー", f"🚀 今やること：{task}")
    interval = int(interval_var.get()) * 60 * 1000  # 分 → ミリ秒変換
    job_id = root.after(interval, show_reminder)  # 指定時間後に再実行（ループ）

# 開始ボタンが押されたときの処理（最初の予約）
def start_reminder():
    global job_id
    interval = int(interval_var.get()) * 60 * 1000
    job_id = root.after(interval, show_reminder)

# 停止ボタンが押されたときの処理（予約のキャンセル）
def stop_reminder():
    global job_id
    if job_id:  # タイマーが設定されていればキャンセル
        root.after_cancel(job_id)
        job_id = None

# ウィンドウの作成と設定
root = tk.Tk()
root.title("集中タスクお知らせアプリ")
root.geometry("400x300")

# タイトルラベル
title_label = tk.Label(root, text="🧠 集中タスクお知らせアプリ", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# タスク入力欄
task_label = tk.Label(root, text="今やること")
task_label.pack()
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

# 繰り返し間隔メニュー
interval_label = tk.Label(root, text="繰り返し間隔（分）：")
interval_label.pack()
interval_var = tk.StringVar(value="1")  # 初期値は「1分」
interval_menu = tk.OptionMenu(root, interval_var, "1", "5", "10", "15")
interval_menu.pack(pady=5)

# 開始ボタン
start_button = tk.Button(root, text="開始", width=10, command=start_reminder)
start_button.pack(pady=5)

# 停止ボタン
stop_button = tk.Button(root, text="停止", width=10, command=stop_reminder)
stop_button.pack()

# タイマー予約ID（Noneなら未設定）
job_id = None

# アプリ起動
root.mainloop()
