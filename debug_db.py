#!/usr/bin/env python3
import sqlite3

def debug_queries():
    conn = sqlite3.connect('/workspace/brands.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    print("=== Testing individual queries ===")
    
    # Test 1: Simple zodiac query
    print("\n1. Simple zodiac query:")
    cursor.execute("SELECT western_zodiac, COUNT(*) FROM brand_astro_data GROUP BY western_zodiac")
    results = cursor.fetchall()
    for row in results:
        print(f"  {row[0]}: {row[1]}")
    
    # Test 2: JOIN with brands
    print("\n2. JOIN with brands:")
    cursor.execute("""
        SELECT ba.western_zodiac, b.name 
        FROM brand_astro_data ba 
        JOIN brands b ON ba.brand_id = b.id 
        LIMIT 10
    """)
    results = cursor.fetchall()
    for row in results:
        print(f"  {row[0]} - {row[1]}")
    
    # Test 3: Check GROUP_CONCAT function
    print("\n3. Testing GROUP_CONCAT:")
    try:
        cursor.execute("""
            SELECT ba.western_zodiac, COUNT(*) as count, GROUP_CONCAT(b.name, ', ') as brands
            FROM brand_astro_data ba
            JOIN brands b ON ba.brand_id = b.id
            GROUP BY ba.western_zodiac
        """)
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[1]} brands - {row[2]}")
    except Exception as e:
        print(f"  Error with GROUP_CONCAT: {e}")
        
        # Try alternative without GROUP_CONCAT
        print("\n3b. Alternative without GROUP_CONCAT:")
        cursor.execute("""
            SELECT ba.western_zodiac, COUNT(*) as count
            FROM brand_astro_data ba
            JOIN brands b ON ba.brand_id = b.id
            GROUP BY ba.western_zodiac
        """)
        results = cursor.fetchall()
        for row in results:
            print(f"  {row[0]}: {row[1]} brands")
    
    # Test 4: Check numerology data
    print("\n4. Numerology data:")
    cursor.execute("SELECT life_path_number, expression_number, chaldean_number FROM brand_astro_data LIMIT 5")
    results = cursor.fetchall()
    for row in results:
        print(f"  Life: {row[0]}, Expression: {row[1]}, Chaldean: {row[2]}")
    
    # Test 5: Check founders
    print("\n5. Founders data:")
    cursor.execute("SELECT full_name, birth_date FROM founders LIMIT 5")
    results = cursor.fetchall()
    for row in results:
        print(f"  {row[0]} - {row[1]}")
    
    conn.close()

if __name__ == "__main__":
    debug_queries()