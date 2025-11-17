# ------------------------------
# Day8 - Loop Practice
# ------------------------------
# ------------------------------
# Day8-001: Warm up（for文のおさらい）
# ------------------------------

print("---- Day8-001: Warm up ----")

for i in range(1,6):
    print(i)

# ------------------------------
# Day8-002: range の応用（ステップ・逆順）
# ------------------------------

print("---- Day8-002: range 応用 ----")

#1. 2刻みで表示(0, 2, 4, 6, 8)
for i in range(0, 10, 2):
    print("2刻み:", i)

#"2. 逆順(10, 9, …, 1)

for n in range(10, 0, -1):
    print("逆順:", n)

# ------------------------------
# Day8-003: ループで合計やカウントを作る
# ------------------------------

print("---- Day8-003: 集計 ----")

#1. 1~10の合計
total = 0
for n in range(1,11):
    total += n
print("1~10の合計:", total)

#2. リストの中で偶数の個数を数える
numbers = [1, 4, 5, 10, 13, 20]
count_even = 0

for num in numbers:
    if num % 2 == 0:
        count_even += 1

print("偶数の数:", count_even)

# ------------------------------
# Day8-004: 文字列をループで処理する
# ------------------------------

print("---- Day8-004: 文字列処理 ----")

text = "mikoto is cute"

#1. 1文字ずつ表示
for ch in text:
    print(ch)

#2. 'o'の数を数える
count_o = 0
for ch in text:
    if ch == 'o' :
        count_o += 1

print("'o' の数:", count_o)

# ------------------------------
# Day8-005: 実務ミニ課題（フィルタ処理）
# ------------------------------

print("---- Day8-005: 実務ミニ課題 ----")

data = ["miko", "fox", "mikoto", "hi", "mi", "koto", "ai", "mkt"]

result = [] # ここに条件を満たした要素を入れる

for word in data:
    if len(word) >= 3: #3文字以上
        result.append(word)

print("3文字以上の単語:", result)