import sqlite3
# データベースに接続
conn = sqlite3.connect('sample.db')
# カーソルを取得
cursor = conn.cursor()
# テーブル作成
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL)''')
# データ挿入
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 35))
# データ取得
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
# データ更新
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (40, 'Alice'))
# データ削除
cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))
# コミットして変更を確定
conn.commit()
# データベース接続を閉じる
conn.close()
