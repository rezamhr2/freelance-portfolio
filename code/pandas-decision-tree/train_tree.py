# train_tree.py — نمونه کار: درخت تصمیم با پانداس و سایکیت‌لرن
#
# داده‌ها خیالی و ساخته‌ی دست هستند (customers.csv) و فقط برای نمایش روش کارند.
# هدف: پیش‌بینی اینکه مشتری اشتراک می‌خرد (subscribed=1) یا نه (۰)،
# بر اساس سن، تعداد بازدید ماهانه و میانگین مبلغ سفارش.
#
# نصب: pip install -r requirements.txt
# اجرا: python3 train_tree.py

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

DATA_PATH = "customers.csv"


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    print(f"تعداد ردیف‌ها: {len(df)}")
    print("ستون‌ها:", list(df.columns))
    print()
    print("آمار توصیفی:")
    print(df.describe().round(1))
    print()

    features = ["age", "monthly_visits", "avg_order_toman"]
    X = df[features]
    y = df["subscribed"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"دقت روی داده‌ی تست: {accuracy:.2%}")
    print()
    print("گزارش طبقه‌بندی:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("قوانین درخت:")
    print(export_text(model, feature_names=features))

    print("پیش‌بینی چند مشتری نمونه:")
    samples = pd.DataFrame(
        [
            {"age": 30, "monthly_visits": 15, "avg_order_toman": 300000},
            {"age": 45, "monthly_visits": 3, "avg_order_toman": 80000},
            {"age": 25, "monthly_visits": 20, "avg_order_toman": 400000},
        ]
    )
    predictions = model.predict(samples)
    for row, pred in zip(samples.to_dict("records"), predictions):
        label = "اشتراک می‌خرد ✅" if pred == 1 else "اشتراک نمی‌خرد ❌"
        print(f"  سن {row['age']}، بازدید ماهانه {row['monthly_visits']}، "
              f"سفارش {row['avg_order_toman']:,} تومان → {label}")


if __name__ == "__main__":
    main()
