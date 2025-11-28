
# -------------------------
# Day6-001: ネスト＋条件分岐（特定条件だけ特別メッセージ）
# -------------------------
names = ["ミコト", "カボ", "アリス"]
days = ["月", "火", "水"]
times = ["午前", "午後"]

for day in days:
    for time in times:
        for name in names:
            if name == "カボ" and day == "火" and time == "午後":
                print(f"{day}曜日の{time}:{name}は集中タイム！★")
            else:
                print(f"{day}曜日の{time}:{name}は通常練習中")

# -------------------------
# Day6-002: 見やすくグループ化して出力
# -------------------------
print("\n== グルーピング表示 ==")
for day in days:
    print(f"=== {day}曜日 ===")
    for time in times:
        badges = []
        for name in names:
            label = "集中★" if(name == "カボ" and day == "火" and time == "午後") else "通常"
            badges.append(f"{name}:{label}")
        print(f"{time} -> " + ",".join(badges))

# -------------------------
# Day6-003: ネスト内の break / continue
# -------------------------
print("\n== ネスト + break/continue ==")
for day in days:
    for time in times:
        if day == "火" and time == "午後":
            print(f"{day}曜{time}: スキップ (continue)")
            continue # ← ここで"この時間帯の処理"だけ飛ばす
    
        for name in names:
            print(f"{day}曜{time}:{name}")
            if day == "水" and time == "午前" and name =="ミコト":
                print("→ 内側ループをbreak (名前ループだけ終了)")
                break # ← 一番内側 (nameループ) だけ止まる
#-----------------------------
# 検証用
#-----------------------------
print("\n== TRACE ==")
for day in days:
    for time in times:
        if day == "火" and time == "午後":
            print(f"[SKIP] {day}曜{time}")
            continue
        print(f"[ENTER] {day}曜{time}")
        for name in names:
            print("  -", name)
            if day == "水" and time == "午前" and name == "ミコト":
                print("  -> break name-loop")
                break
        print(f"[LEAVE] {day}曜{time}")

#-----------------------------
# 構文	         意味	           よく使う場面
# for in	くり返し処理	       リストや辞書の走査
# break 	ループを途中で止める	条件を満たしたら終了
# continue 	その1回だけスキップ	    条件外を無視
# f"..."	文字列に変数を埋め込む	出力・ログ・テンプレート