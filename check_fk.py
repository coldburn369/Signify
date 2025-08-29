#!/usr/bin/env python3
import sqlite3

def check_foreign_keys():
    conn = sqlite3.connect('/workspace/brands.db')
    cursor = conn.cursor()
    
    print("=== Checking Foreign Key Relationships ===")
    
    # Check brands table IDs
    cursor.execute("SELECT id, name FROM brands ORDER BY id LIMIT 10")
    brand_rows = cursor.fetchall()
    print("\nBrands table IDs:")
    for row in brand_rows:
        print(f"  ID {row[0]}: {row[1]}")
    
    # Check brand_astro_data foreign keys
    cursor.execute("SELECT brand_id, western_zodiac FROM brand_astro_data ORDER BY brand_id LIMIT 10")
    astro_rows = cursor.fetchall()
    print("\nBrand_astro_data foreign keys:")
    for row in astro_rows:
        print(f"  brand_id {row[0]}: {row[1]}")
    
    # Try the JOIN manually
    print("\nManual JOIN test:")
    cursor.execute("""
        SELECT b.id, b.name, ba.brand_id, ba.western_zodiac
        FROM brands b, brand_astro_data ba
        WHERE b.id = ba.brand_id
        LIMIT 10
    """)
    join_rows = cursor.fetchall()
    for row in join_rows:
        print(f"  Brand {row[0]} ({row[1]}) -> Astro brand_id {row[2]} ({row[3]})")
    
    conn.close()

if __name__ == "__main__":
    check_foreign_keys()