#!/usr/bin/env python3
"""
Fix the database schema for SQLite compatibility and repopulate the data.
"""

import sqlite3
import os
from brand_research import BrandResearcher
from brand_data import get_major_brands_data

def fix_database():
    """Drop and recreate the database with proper SQLite schema."""
    
    # Remove existing database
    if os.path.exists('/workspace/brands.db'):
        os.remove('/workspace/brands.db')
        print("Removed existing database")
    
    # Create new database with SQLite-compatible schema
    conn = sqlite3.connect('/workspace/brands.db')
    
    # SQLite schema (SERIAL -> INTEGER PRIMARY KEY AUTOINCREMENT)
    schema = """
    CREATE TABLE brands (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        name            VARCHAR(255) NOT NULL,
        category        VARCHAR(100),
        founding_date   DATE,
        country         VARCHAR(100),
        parent_company  VARCHAR(255),
        stock_ticker    VARCHAR(20),
        market_cap      BIGINT,
        logo_url        TEXT,
        tagline         TEXT,
        created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE brand_astro_data (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_id            INTEGER REFERENCES brands(id) ON DELETE CASCADE,
        western_zodiac      VARCHAR(50),
        chinese_animal      VARCHAR(50),
        chinese_element     VARCHAR(50),
        life_path_number    INTEGER,
        expression_number   INTEGER,
        chaldean_number     INTEGER
    );

    CREATE TABLE brand_cultural_data (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_id    INTEGER REFERENCES brands(id) ON DELETE CASCADE,
        colors      VARCHAR(255),
        notes       TEXT
    );

    CREATE TABLE founders (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_id        INTEGER REFERENCES brands(id) ON DELETE CASCADE,
        full_name       VARCHAR(255),
        birth_date      DATE,
        western_zodiac  VARCHAR(50),
        chinese_animal  VARCHAR(50),
        chinese_element VARCHAR(50),
        life_path_number INTEGER,
        expression_number INTEGER
    );

    -- Indexes for better performance
    CREATE INDEX idx_brands_category ON brands(category);
    CREATE INDEX idx_brands_country ON brands(country);
    CREATE INDEX idx_brands_founding_date ON brands(founding_date);
    CREATE INDEX idx_brand_astro_data_brand_id ON brand_astro_data(brand_id);
    CREATE INDEX idx_brand_cultural_data_brand_id ON brand_cultural_data(brand_id);
    CREATE INDEX idx_founders_brand_id ON founders(brand_id);
    """
    
    # Execute schema
    statements = [s.strip() for s in schema.split(';') if s.strip()]
    for statement in statements:
        conn.execute(statement)
    
    conn.commit()
    conn.close()
    print("Created new database with SQLite-compatible schema")
    
    # Repopulate data using existing system
    print("Repopulating data...")
    researcher = BrandResearcher()
    brands_data = get_major_brands_data()
    
    for i, brand_data in enumerate(brands_data, 1):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print("Database fixed and repopulated successfully!")

if __name__ == "__main__":
    fix_database()