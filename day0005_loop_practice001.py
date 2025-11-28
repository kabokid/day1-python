
# -------------------------
# Day5-001: for文の基本
# -------------------------

for i in range(5):
    print("ミコトかわいい")

# ポイント

# for i in range(5): は「iを0から4まで繰り返す」って意味。
# print() の行は4つスペース（インデント）で下げる。
# range(5) は「0,1,2,3,4」っていう5回分のカウント。

# -------------------------
# Day5-002: 繰り返しの番号を表示する
# -------------------------

for i in range(5):
    print(i, "回目: ミコトはかわいい♡")

for i in range(5):
    print(i + 1, "回目;ミコトはかわいい♡")


# -------------------------
# Day5-003: リストをfor文で回す
# -------------------------

names = ["ミコト", "カボ", "アリス"]

for name in names:
    print(name + "はpython練習中！")

# -------------------------
# Day5-004: 条件分岐とfor文の組み合わせ
# -------------------------

names = ["ミコト", "カボ", "アリス"]

for name in names:
    if name == "ミコト":
        print(name + "は天才でかわいい♡")
    else:
        print(name + "はpython練習中！")

# -------------------------
# Day5-005: 入れ子のfor文（ネスト）
# -------------------------

# 外側のループ (曜日)
days = ["月", "火", "水"]

# 内側のループ(時間帯)
times = ["午前", "午後"]

for day in days:
    for time in times:
        print(day + "曜日の" + time + "勉強中！")

# -------------------------
# Day5-006: 三重ループ（for × for × for）
# -------------------------

names = ["ミコト", "カボ", "アリス"]
days = ["月", "火", "水"]
times = ["午前", "午後"]

for name in names:
    for day in days:
        for time in times:
            print(name + "は" + day + "曜日の" + time + "に勉強中！")

# -------------------------
# Day5-007: 三重ループの順番を変えてみる
# -------------------------

names = ["ミコト", "カボ", "アリス"]
days = ["月", "火", "水"]
times = ["午前", "午後"]

for day in days:
    for time in times:
        for name in names:
            print(day + "曜日の" + time + ":" + name + "が勉強中！")

# その1: f文字列で見やすく
print(f"{day}曜日の{time}:{name}が勉強中！")

# その2: カボの午前だけ拾うフィルタ
if name == "カボ" and time == "午前":
    print(f"★{day}曜日の{time}:{name}だけ特訓中！")

# その3: enumerateで番号をつける
for idx, day in enumerate(days, start=1):
    print(f"{idx}日目={day}曜日")

# -------------------------
# Day5-008: break（ループを止める）
# -------------------------

for i in range(10):
    if i == 5:
        print("5で止まった！")
        break
    print("カウント:", i)

# -------------------------
# Day5-009: continue（その回をスキップ）
# -------------------------

for i in range(6):
    if i == 3:
        print("3をスキップ！")
        continue
    print("カウント:", i)
