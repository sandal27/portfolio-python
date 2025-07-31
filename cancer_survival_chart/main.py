# がんの5年生存率を種類別に色分け棒グラフで可視化するプログラム

import pandas as pd                     # データ処理用ライブラリ
import matplotlib.pyplot as plt         # グラフ描画ライブラリ
from matplotlib.patches import Patch    # 凡例（色ラベル）作成用
from matplotlib import rcParams         # フォント設定用

# 日本語フォントを指定（Macの場合）
rcParams['font.family'] = 'Hiragino Mincho ProN'

# CSVファイルからデータを読み込む
# ファイル名: cancer_survival.csv（がんの種類と5年生存率の表）
df = pd.read_csv("cancer_survival.csv")

# 生存率の列（%）を取り出す
rates = df["5年生存率（%）"]

# 生存率に応じて棒グラフの色を決定（低:赤, 中:黄, 高:緑）
colors = [
    '#E74C3C' if r < 40 else '#F4D03F' if r < 70 else '#2ECC71'
    for r in rates
]

# グラフの作成（サイズ指定）
plt.figure(figsize=(10, 6))

# 棒グラフを描画（横: がんの種類, 縦: 生存率, 色分け）
bars = plt.bar(df["がんの種類"], rates, width=0.6, color=colors)

# 凡例（色の説明）を作成
legend_labels = [
    Patch(color='#E74C3C', label='低（<40%）'),
    Patch(color='#F4D03F', label='中（40〜69%）'),
    Patch(color='#2ECC71', label='高（70%以上）')
]
plt.legend(handles=legend_labels, title="生存率")

# 各棒の上に生存率を数値表示
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        yval + 1,
        f'{yval:.1f}%',
        ha='center'
    )

# タイトルと軸ラベルを設定
plt.title("がんの5年生存率（種類別）", fontsize=24, fontweight='bold')
plt.xlabel("がんの種類", fontsize=18, labelpad=15)
plt.ylabel("5年生存率（%）", fontsize=18)

# Y軸の範囲を0〜100に固定
plt.ylim(0, 100)

# Y軸に補助線（点線）を表示
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 全体のレイアウトを自動調整
plt.tight_layout()

#スクリーンショット作成
plt.savefig("screenshot.png")

# グラフを表示
plt.show()
