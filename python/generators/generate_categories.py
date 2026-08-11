import pandas as pd
categories = [
    ("CAT001", "Electronics", "Electronic devices and accessories"),
    ("CAT002", "Fashion", "Clothing, footwear and accessories"),
    ("CAT003", "Grocery", "Daily household groceries")
]

df = pd.DataFrame(
    categories,
    columns=["category_id", "category_name", "description"]
)

df.to_csv("datasets/categories.csv", index=False)

print("✅ categories.csv created successfully!")