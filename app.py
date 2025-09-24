import sqlite3

DB_NAME = "bakery.db"

# ---------------------------
# دوال التعامل مع قاعدة البيانات
# ---------------------------

def connect_db():
    """الاتصال بقاعدة البيانات"""
    return sqlite3.connect(DB_NAME)

def create_tables():
    """إنشاء الجداول لو مش موجودة"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT UNIQUE,
        address TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_customers(customers):
    """إضافة مجموعة عملاء"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT OR IGNORE INTO customers (name, phone, address) VALUES (?, ?, ?)",
        customers
    )

    conn.commit()
    conn.close()

def get_all_customers():
    """عرض جميع العملاء"""
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, phone, address FROM customers")
    rows = cursor.fetchall()

    conn.close()
    return rows

def show_customers(rows):
    """طباعة العملاء بشكل منظم"""
    print("\n📋 بيانات العملاء:")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Address: {row[3]}")

# ---------------------------
# الكود الرئيسي
# ---------------------------

def main():
    create_tables()

    customers = [
        ('ahmed','01020651679','Z/97/10'),
        ('mohamed','01022506535','Z/97/11'),
        ('alaa','01211978882','Z/97/12'),
        ('joe','01023506923','Z/97/13'),
        ('nabila','01062002180','Z/97/14'),
        ('abadie','01020651679','Z/97/15'),
        ('anything','01020651679','Z/97/16'),
    ]

    insert_customers(customers)

    rows = get_all_customers()
    show_customers(rows)

if __name__ == "__main__":
    main()
