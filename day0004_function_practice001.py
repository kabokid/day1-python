# -------------------------
# Day4-001: 関数の基本
# -------------------------
def greet():
    print("Hello, Mikoto!")

greet()

# -------------------------
# Day4-002: 引数付き関数
# -------------------------
def greet_name(name):
    print("Hello, " + name + "!")

greet_name("kabo")

# -------------------------
# Day4-003: 戻り値の練習
# -------------------------
def add(a, b):
    return a + b

print(add(10, 5))

# -------------------------
# Day4-004: 条件付きのretutneの応用
# -------------------------

def check_score(score):
    # 点数に応じて評価を返す関数
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"
 
# 実際に関数を使ってみる
score_input = 82
result = check_score(score_input)
print("点数", score_input, "→評価:", result)

# いくつかテストしてみよう
print("点数: 95 → 評価:", check_score(95))
print("点数: 73 → 評価:", check_score(73))
print("点数: 60 → 評価:", check_score(60))
print("点数: 40 → 評価:", check_score(40))

# -------------------------
# Day4-005: ユーザー入力 × 関数
# -------------------------

def check_score(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

# ユーザーから点数を入力してもらう
score_input = int(input("点数を入力してください:"))

# 関数を使って評価を取得
result = check_score(score_input)

# 結果を表示
print("あなたの評価は", result, "です！")

#--------------------------
#"," は複数の値を「スペース区切りで表示」する。
#"+" は文字列として「直接つなぐ」。
# -------------------------
# Day4-006: f文字列と + の比較
# -------------------------

def check_score(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "D"

score_input = int(input("点数を入力してください:"))
result = check_score(score_input)

# f文字列で入力
print(f"[f文字列] あなたの評価は {result} です！")

# + で出力(全部文字列としてつなげる)
print("[+連結] あなたの評価は" + result + "です！")

#-----------------------
#💬 ポイント確認！

# f"" → {} の中に変数を直接書ける。

# + → すべて文字列としてつなげる。数字を入れるときは str() 必要。

# 両方の出力が同じなら大成功✨