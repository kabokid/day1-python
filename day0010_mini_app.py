# ------------------------------
# Day10 - Mini App
# ------------------------------
# ------------------------------
# Day10-001: データ準備（list + dict）
# ------------------------------
# ☆ この項目でやっていること
# - ログ（ユーザーとアクション）の一覧を list にまとめる
# - 1つのログは dict で「user」「action」を持つ
# ☆ こんな場面で使うイメージ
# - Webのアクセスログ
# - アプリ内の操作履歴
# - ゲームのプレイヤー行動ログ

logs = [
    {"user": "kabo", "action": "login"},
    {"user": "mikoto", "action": "view"},
    {"user": "kabo", "action": "edit"},
    {"user": "gonzou", "action": "login"},
    {"user": "mikoto", "action": "logout"},
    {"user": "kabo", "action": "view"},
]

# ------------------------------
# Day10-002: 集計関数（関数 + dict）
# ------------------------------
# ☆ この項目でやっていること
# - 関数にまとめることで、どこからでも使える集計ロジックを作る
# - dict を「ユーザー → 回数」の対応表として使う
# - ループで1件ずつ処理し、必要なら追加 or 更新する
# ☆ こんな場面で使うイメージ
# - ログ解析
# - ユーザーごとの行動統計
# - アプリの使用状況レポート

def count_actions(log_list):
    counts = {}
    for entry in log_list:
        name = entry["user"]
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    return counts
print("\n")
# ------------------------------
# Day10-003: アプリ本体（関数呼び出し）
# ------------------------------
# ☆ この項目でやっていること
# - count_actions() を呼んで集計を実行
# - 得られた dict をユーザーごとに表示していく
# - 実際の“集計アプリ”らしい動きになる部分
print("---- Day10 ミニアプリ ----" )

result = count_actions(logs)
for name in sorted(result.keys()):
    print(name, ":", result[name], "回")
print("\n")
# ------------------------------
# Day10-004: login 回数だけ集計する
# ------------------------------
# ☆ この項目でやっていること
# - 全ログの中から action が "login" のものだけを対象にする
# - 条件分岐 if を使って、集計対象を絞る
# ☆ こんな場面で使うイメージ
# - 「ログイン回数」だけを別レポートに出したいとき
# - 決まった種類の操作だけ集計したいとき

def count_logins(log_list):
    login_counts = {}
    for entry in log_list:
        if entry["action"] != "login":
            # login 以外はスキップ
            continue
        name = entry["user"]
        if name in login_counts:
            login_counts[name] += 1
        else:
            login_counts[name] = 1
    return login_counts

print("---- login 回数だけの集計 ----")
login_result = count_logins(logs)

for name in sorted(login_result.keys()):
    print(name, ":", login_result[name], "回 login")
print("\n")
# ------------------------------
# Day10-005: 特定ユーザーの回数だけを表示する
# ------------------------------
# ☆ この項目でやっていること
# - すでに計算済みの result から、知りたいユーザーだけ取り出す
# - dict からキーを指定して値を読む基本の応用
# ☆ こんな場面で使うイメージ
# - 「このユーザーだけ詳細を見たい」とき
# - 管理画面で個別ユーザーの情報を確認する処理

target_user = "kabo"

print("---- 特定ユーザーの回数 ----")
if target_user in result:
    print(target_user, "の行動回数:", result[target_user], "回")
else:
    print(target_user, "のデータはありません")
