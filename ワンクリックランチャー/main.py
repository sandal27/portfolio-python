import subprocess     # OSごとのアプリ起動に使用
import platform       # 実行環境がMacかWindowsか判定
import tkinter as tk  # GUI（ボタン・ウィンドウ表示）
import webbrowser     # 既定ブラウザでWebサイトを開く

# ============== 起動セット ==============

# ==== 🖥️ 仕事用アプリ・サイトをまとめて起動 ====
def launch_work():
    system = platform.system()

    # -------- 音声支援 ------------------
    if system == "Darwin":  # Mac
        subprocess.Popen(["open", "-a", "Siri"])
    elif system == "Windows":
        subprocess.Popen(["control", "speech"])

    # -------- メモアプリ -----------------
    if system == "Darwin":
        subprocess.Popen(["open", "-a", "TextEdit"])
    elif system == "Windows":
        subprocess.Popen(['cmd', '/c', 'start', '', 'notepad'], shell=True)
    
    # ---- ChatGPT（既定ブラウザ） ---------
    webbrowser.open("https://chatgpt.com/")

    # -------- Zoom（Web版） --------------
    webbrowser.open("https://zoom.us/")

    # -------- Google カレンダー ----------
    webbrowser.open("https://calendar.google.com/")

    # -------- Google Drive ---------------
    webbrowser.open("https://drive.google.com/")

# ==== 🎶 プライベートアプリ・サイトをまとめて起動 ====
def launch_private():
    # -------- ChatGPT ----------
    webbrowser.open("https://chatgpt.com/")
    # -------- Instagram --------
    webbrowser.open("https://www.instagram.com/")
    # -------- YouTube ----------
    webbrowser.open("https://www.youtube.com/")
    # -------- Netflix ----------
    webbrowser.open("https://www.netflix.com/")
    # -------- Amazon -----------
    webbrowser.open("https://www.amazon.co.jp/")
    # -------- 楽天市場 ----------
    webbrowser.open("https://www.rakuten.co.jp/")
    # -------- Spotify ----------
    webbrowser.open("https://open.spotify.com/")

# ============== GUI作成 ==============

root = tk.Tk()
root.title("ワンクリックランチャー")  # ウィンドウタイトル
root.geometry("380x230")          # ウィンドウサイズ

center_frame = tk.Frame(root)
center_frame.pack(expand=True) # expand=True で上下左右中央寄せ

title_label = tk.Label(center_frame, text="起動セットを選んでください", font=("Arial", 16))
title_label.pack(pady=10)

# 仕事用ボタン
work_btn = tk.Button(center_frame, text="🖥️ 仕事用を開始", font=("Arial", 14), width=25, command=launch_work)
work_btn.pack(pady=12, ipady=4)

# プライベート用ボタン
private_btn = tk.Button(center_frame, text="🎶 プライベートを開始", font=("Arial", 14), width=25, command=launch_private)
private_btn.pack(pady=12, ipady=4)

root.mainloop()
