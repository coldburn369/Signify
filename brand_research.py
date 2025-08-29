#!/usr/bin/env python3
"""
Global Brand Research System
Comprehensive tool for researching and cataloging major global brands
with astrological and numerological analysis.
"""

import sqlite3
from datetime import datetime, date
import re
from typing import Dict, List, Optional, Tuple
import json


class NumerologyCalculator:
    """Calculate numerology values using Pythagorean and Chaldean systems."""
    
    # Pythagorean numerology mapping
    PYTHAGOREAN_MAP = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    
    # Chaldean numerology mapping
    CHALDEAN_MAP = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 8, 'G': 3, 'H': 5, 'I': 1,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 7, 'P': 8, 'Q': 1, 'R': 2,
        'S': 3, 'T': 4, 'U': 6, 'V': 6, 'W': 6, 'X': 5, 'Y': 1, 'Z': 7
    }
    
    @staticmethod
    def reduce_to_single_digit(number: int) -> int:
        """Reduce a number to a single digit (1-9) unless it's 11, 22, or 33."""
        if number in [11, 22, 33]:
            return number
        while number > 9:
            number = sum(int(digit) for digit in str(number))
        return number
    
    @classmethod
    def calculate_expression_number(cls, name: str) -> int:
        """Calculate Pythagorean expression number from name."""
        name = name.upper().replace(' ', '').replace('-', '').replace('.', '')
        total = sum(cls.PYTHAGOREAN_MAP.get(char, 0) for char in name if char.isalpha())
        return cls.reduce_to_single_digit(total)
    
    @classmethod
    def calculate_chaldean_number(cls, name: str) -> int:
        """Calculate Chaldean number from name."""
        name = name.upper().replace(' ', '').replace('-', '').replace('.', '')
        total = sum(cls.CHALDEAN_MAP.get(char, 0) for char in name if char.isalpha())
        return cls.reduce_to_single_digit(total)
    
    @classmethod
    def calculate_life_path_number(cls, birth_date: date) -> int:
        """Calculate life path number from birth date."""
        total = birth_date.day + birth_date.month + birth_date.year
        return cls.reduce_to_single_digit(total)


class AstrologyCalculator:
    """Calculate astrological signs and Chinese zodiac information."""
    
    # Western zodiac date ranges
    ZODIAC_SIGNS = [
        ('Capricorn', (12, 22), (1, 19)),
        ('Aquarius', (1, 20), (2, 18)),
        ('Pisces', (2, 19), (3, 20)),
        ('Aries', (3, 21), (4, 19)),
        ('Taurus', (4, 20), (5, 20)),
        ('Gemini', (5, 21), (6, 20)),
        ('Cancer', (6, 21), (7, 22)),
        ('Leo', (7, 23), (8, 22)),
        ('Virgo', (8, 23), (9, 22)),
        ('Libra', (9, 23), (10, 22)),
        ('Scorpio', (10, 23), (11, 21)),
        ('Sagittarius', (11, 22), (12, 21))
    ]
    
    # Chinese zodiac animals (12-year cycle starting from 1900 = Rat)
    CHINESE_ANIMALS = [
        'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
        'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'
    ]
    
    # Chinese elements (5-element cycle)
    CHINESE_ELEMENTS = ['Metal', 'Water', 'Wood', 'Fire', 'Earth']
    
    @classmethod
    def get_western_zodiac(cls, birth_date: date) -> str:
        """Get Western zodiac sign from birth date."""
        month, day = birth_date.month, birth_date.day
        
        for sign, start, end in cls.ZODIAC_SIGNS:
            if start[0] == end[0]:  # Same month
                if start[1] <= day <= end[1]:
                    return sign
            else:  # Spans two months
                if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
                    return sign
        return 'Unknown'
    
    @classmethod
    def get_chinese_zodiac(cls, birth_date: date) -> Tuple[str, str]:
        """Get Chinese zodiac animal and element from birth date."""
        year = birth_date.year
        
        # Calculate animal (12-year cycle)
        animal_index = (year - 1900) % 12
        animal = cls.CHINESE_ANIMALS[animal_index]
        
        # Calculate element (10-year cycle, but alternating yin/yang)
        element_index = ((year - 1900) % 10) // 2
        element = cls.CHINESE_ELEMENTS[element_index]
        
        return animal, element


class BrandDatabase:
    """Database operations for brand data."""
    
    def __init__(self, db_path: str = '/workspace/brands.db'):
        self.db_path = db_path
        self.setup_database()
    
    def setup_database(self):
        """Create database tables."""
        with sqlite3.connect(self.db_path) as conn:
            # Read and execute schema
            with open('/workspace/database_setup.sql', 'r') as f:
                schema = f.read()
            # Remove CREATE statements and execute individually
            statements = schema.split(';')
            for statement in statements:
                if statement.strip():
                    try:
                        conn.execute(statement.strip())
                    except sqlite3.OperationalError as e:
                        if "already exists" not in str(e):
                            print(f"Error creating table: {e}")
            conn.commit()
    
    def insert_brand(self, brand_data: Dict) -> int:
        """Insert brand data and return brand_id."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO brands (name, category, founding_date, country, parent_company, 
                                  stock_ticker, market_cap, logo_url, tagline)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                brand_data['name'],
                brand_data['category'],
                brand_data['founding_date'],
                brand_data['country'],
                brand_data.get('parent_company'),
                brand_data.get('stock_ticker'),
                brand_data.get('market_cap'),
                brand_data.get('logo_url'),
                brand_data.get('tagline')
            ))
            return cursor.lastrowid
    
    def insert_astro_data(self, brand_id: int, astro_data: Dict):
        """Insert astrological data for a brand."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO brand_astro_data (brand_id, western_zodiac, chinese_animal, 
                                            chinese_element, life_path_number, 
                                            expression_number, chaldean_number)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                brand_id,
                astro_data['western_zodiac'],
                astro_data['chinese_animal'],
                astro_data['chinese_element'],
                astro_data['life_path_number'],
                astro_data['expression_number'],
                astro_data['chaldean_number']
            ))
    
    def insert_cultural_data(self, brand_id: int, cultural_data: Dict):
        """Insert cultural data for a brand."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO brand_cultural_data (brand_id, colors, notes)
                VALUES (?, ?, ?)
            """, (
                brand_id,
                cultural_data.get('colors'),
                cultural_data.get('notes')
            ))
    
    def insert_founder(self, brand_id: int, founder_data: Dict):
        """Insert founder data for a brand."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO founders (brand_id, full_name, birth_date, western_zodiac,
                                    chinese_animal, chinese_element, life_path_number,
                                    expression_number)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                brand_id,
                founder_data['full_name'],
                founder_data.get('birth_date'),
                founder_data.get('western_zodiac'),
                founder_data.get('chinese_animal'),
                founder_data.get('chinese_element'),
                founder_data.get('life_path_number'),
                founder_data.get('expression_number')
            ))


class BrandResearcher:
    """Main class for researching and processing brand data."""
    
    def __init__(self):
        self.db = BrandDatabase()
        self.numerology = NumerologyCalculator()
        self.astrology = AstrologyCalculator()
    
    def calculate_brand_astro_data(self, brand_name: str, founding_date: date) -> Dict:
        """Calculate all astrological and numerological data for a brand."""
        return {
            'western_zodiac': self.astrology.get_western_zodiac(founding_date),
            'chinese_animal': self.astrology.get_chinese_zodiac(founding_date)[0],
            'chinese_element': self.astrology.get_chinese_zodiac(founding_date)[1],
            'life_path_number': self.numerology.calculate_life_path_number(founding_date),
            'expression_number': self.numerology.calculate_expression_number(brand_name),
            'chaldean_number': self.numerology.calculate_chaldean_number(brand_name)
        }
    
    def process_brand(self, brand_data: Dict) -> int:
        """Process a complete brand entry with all associated data."""
        # Insert main brand data
        brand_id = self.db.insert_brand(brand_data)
        
        # Calculate and insert astrological data
        if brand_data.get('founding_date'):
            founding_date = datetime.strptime(brand_data['founding_date'], '%Y-%m-%d').date()
            astro_data = self.calculate_brand_astro_data(brand_data['name'], founding_date)
            self.db.insert_astro_data(brand_id, astro_data)
        
        # Insert cultural data
        if brand_data.get('cultural_data'):
            self.db.insert_cultural_data(brand_id, brand_data['cultural_data'])
        
        # Insert founder data if available
        if brand_data.get('founder_data'):
            founder_data = brand_data['founder_data']
            if founder_data.get('birth_date'):
                birth_date = datetime.strptime(founder_data['birth_date'], '%Y-%m-%d').date()
                founder_data['western_zodiac'] = self.astrology.get_western_zodiac(birth_date)
                founder_data['chinese_animal'] = self.astrology.get_chinese_zodiac(birth_date)[0]
                founder_data['chinese_element'] = self.astrology.get_chinese_zodiac(birth_date)[1]
                founder_data['life_path_number'] = self.numerology.calculate_life_path_number(birth_date)
                founder_data['expression_number'] = self.numerology.calculate_expression_number(founder_data['full_name'])
            self.db.insert_founder(brand_id, founder_data)
        
        return brand_id


if __name__ == "__main__":
    # Test the system
    researcher = BrandResearcher()
    print("Brand research system initialized successfully!")
    print(f"Database created at: {researcher.db.db_path}")