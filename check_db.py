#!/usr/bin/env python3
import sqlite3

def check_database():
    conn = sqlite3.connect('/workspace/brands.db')
    cursor = conn.cursor()
    
    # Check brands table
    print("=== BRANDS TABLE ===")
    cursor.execute("SELECT name, category, founding_date FROM brands LIMIT 5")
    for row in cursor.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]}")
    
    # Check brand_astro_data table
    print("\n=== BRAND_ASTRO_DATA TABLE ===")
    cursor.execute("SELECT COUNT(*) FROM brand_astro_data")
    count = cursor.fetchone()[0]
    print(f"Total records: {count}")
    
    if count > 0:
        cursor.execute("SELECT brand_id, western_zodiac, chinese_animal FROM brand_astro_data LIMIT 5")
        for row in cursor.fetchall():
            print(f"Brand ID {row[0]} | {row[1]} | {row[2]}")
    
    # Check brand_cultural_data table  
    print("\n=== BRAND_CULTURAL_DATA TABLE ===")
    cursor.execute("SELECT COUNT(*) FROM brand_cultural_data")
    count = cursor.fetchone()[0]
    print(f"Total records: {count}")
    
    # Check founders table
    print("\n=== FOUNDERS TABLE ===")
    cursor.execute("SELECT COUNT(*) FROM founders")
    count = cursor.fetchone()[0]
    print(f"Total records: {count}")
    
    # Check table structure
    print("\n=== TABLE STRUCTURE ===")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  {col[1]} {col[2]}")
    
    conn.close()

if __name__ == "__main__":
    check_database()