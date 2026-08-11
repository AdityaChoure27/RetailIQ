from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker("en_IN")

company_prefix = [
    "BlueNova", "PrimeTech", "Apex", "UrbanEdge", "Vertex",
    "NextGen", "Skyline", "Elite", "NovaMart", "Global"
]

company_suffix = [
    "Supplies Pvt Ltd",
    "Distributors",
    "Retail Solutions",
    "Trading Co.",
    "Wholesale",
    "Enterprises",
    "Supply Chain",
    "Traders"
]

cities = [
    ("Bhopal", "Madhya Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Pune", "Maharashtra"),
    ("Mumbai", "Maharashtra"),
    ("Jaipur", "Rajasthan"),
    ("Ahmedabad", "Gujarat"),
    ("Lucknow", "Uttar Pradesh"),
    ("Delhi", "Delhi"),
    ("Hyderabad", "Telangana"),
    ("Bengaluru", "Karnataka")
]

suppliers = []

for i in range(1, 101):

    supplier_id = f"S{i:05d}"

    supplier_name = f"{random.choice(company_prefix)} {random.choice(company_suffix)}"

    contact_person = fake.name()

    email = supplier_name.lower().replace(" ", "").replace(".", "") + "@gmail.com"

    phone = fake.phone_number()

    city, state = random.choice(cities)

    gst = str(random.randint(10, 35)) + fake.bothify("?????####?1Z#").upper()

    created_at = datetime.now().date()

    suppliers.append([
        supplier_id,
        supplier_name,
        contact_person,
        email,
        phone,
        city,
        state,
        gst,
        created_at
    ])

df = pd.DataFrame(
    suppliers,
    columns=[
        "supplier_id",
        "supplier_name",
        "contact_person",
        "email",
        "phone",
        "city",
        "state",
        "gst_number",
        "created_at"
    ]
)

df.to_csv("datasets/suppliers.csv", index=False)

print("✅ suppliers.csv generated successfully!")
print(df.head())