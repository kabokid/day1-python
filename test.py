score = int(input("点数を入力してください:"))

if score >= 90:
    print("評価:A")
elif score >= 70:
    print("評価:B")
elif score >= 50:
    print("評価:C")
else:
    print("評価:D")