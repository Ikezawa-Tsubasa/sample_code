from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# データの読み込み
# ここでは、特徴量をX、クラスラベルをyとして読み込む
X, y = load_data()
# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# モデルの定義と学習
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
# テストデータの予測
y_pred = model.predict(X_test)
# 精度の評価
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
