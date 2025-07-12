def show_menu():
    print("\n==============================")
    print("      タスク管理メモ帳")
    print("==============================")
    print("1. タスクを追加")
    print("2. タスク一覧を表示")
    print("3. タスクを削除")
    print("4. 終了")
    print("5. タスクを修正")
    print("------------------------------")

# タスク一覧をファイルから読み込む
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

# タスク一覧をファイルに保存する
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("番号を入力してください: ").strip()

        if choice == "1":
            task = input("追加するタスクを入力してください: ").strip()
            tasks.append(task)
            save_tasks(tasks)
            print("✔ タスクを追加しました。")

        elif choice == "2":
            print("\n＜現在のタスク一覧＞")
            if not tasks:
                print("（タスクはありません）")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")

        elif choice == "3":
            print("\n＜タスク削除モード＞")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("削除したいタスクの番号を入力してください: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"✔ 『{removed}』を削除しました。")
                else:
                    print("⚠ 有効な番号を入力してください。")
            except ValueError:
                print("⚠ 数字で入力してください。")

        elif choice == "4":
            print("終了します。ご利用ありがとうございました。")
            break

        elif choice == "5":
            print("\n＜タスク修正モード＞")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("修正したいタスクの番号を入力してください: "))
                if 1 <= num <= len(tasks):
                    new_task = input("新しいタスク内容を入力してください: ").strip()
                    old_task = tasks[num - 1]
                    tasks[num - 1] = new_task
                    save_tasks(tasks)
                    print(f"✔ 『{old_task}』を『{new_task}』に修正しました。")
                else:
                    print("⚠ 有効な番号を入力してください。")
            except ValueError:
                print("⚠ 数字で入力してください。")

        else:
            print("⚠ 無効な入力です。1〜5の番号を入力してください。")

# スクリプトが直接実行されたときだけmain()を呼び出す
if __name__ == "__main__":
    main()
