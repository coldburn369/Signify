#!/usr/bin/env python3
"""
Database Query and Analysis Tools
Comprehensive tools for querying and analyzing the global brands database.
"""

import sqlite3
from typing import List, Dict, Any
import json


class BrandAnalyzer:
    """Database query and analysis tools for brand data."""
    
    def __init__(self, db_path: str = '/workspace/brands.db'):
        self.db_path = db_path
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Execute a query and return results as list of dictionaries."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def get_all_brands(self) -> List[Dict[str, Any]]:
        """Get all brands with their complete information."""
        query = """
        SELECT 
            b.*,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element,
            ba.life_path_number,
            ba.expression_number,
            ba.chaldean_number,
            bc.colors,
            bc.notes as cultural_notes
        FROM brands b
        LEFT JOIN brand_astro_data ba ON b.id = ba.brand_id
        LEFT JOIN brand_cultural_data bc ON b.id = bc.brand_id
        ORDER BY b.name
        """
        return self.execute_query(query)
    
    def get_brands_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all brands in a specific category."""
        query = """
        SELECT 
            b.*,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element,
            ba.life_path_number,
            ba.expression_number,
            ba.chaldean_number
        FROM brands b
        LEFT JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE b.category = ?
        ORDER BY b.market_cap DESC
        """
        return self.execute_query(query, (category,))
    
    def get_brands_by_zodiac(self, zodiac_sign: str) -> List[Dict[str, Any]]:
        """Get all brands with a specific Western zodiac sign."""
        query = """
        SELECT 
            b.name,
            b.category,
            b.founding_date,
            b.country,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element
        FROM brands b
        JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE ba.western_zodiac = ?
        ORDER BY b.founding_date
        """
        return self.execute_query(query, (zodiac_sign,))
    
    def get_brands_by_chinese_animal(self, animal: str) -> List[Dict[str, Any]]:
        """Get all brands with a specific Chinese zodiac animal."""
        query = """
        SELECT 
            b.name,
            b.category,
            b.founding_date,
            b.country,
            ba.chinese_animal,
            ba.chinese_element
        FROM brands b
        JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE ba.chinese_animal = ?
        ORDER BY b.founding_date
        """
        return self.execute_query(query, (animal,))
    
    def get_brands_by_life_path_number(self, number: int) -> List[Dict[str, Any]]:
        """Get all brands with a specific life path number."""
        query = """
        SELECT 
            b.name,
            b.category,
            b.founding_date,
            ba.life_path_number,
            ba.expression_number,
            ba.chaldean_number
        FROM brands b
        JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE ba.life_path_number = ?
        ORDER BY b.name
        """
        return self.execute_query(query, (number,))
    
    def get_market_cap_summary(self) -> List[Dict[str, Any]]:
        """Get market cap summary by category."""
        query = """
        SELECT 
            category,
            COUNT(*) as brand_count,
            AVG(market_cap) as avg_market_cap,
            SUM(market_cap) as total_market_cap,
            MAX(market_cap) as max_market_cap,
            MIN(market_cap) as min_market_cap
        FROM brands 
        WHERE market_cap IS NOT NULL
        GROUP BY category
        ORDER BY total_market_cap DESC
        """
        return self.execute_query(query)
    
    def get_country_summary(self) -> List[Dict[str, Any]]:
        """Get brand count by country."""
        query = """
        SELECT 
            country,
            COUNT(*) as brand_count,
            GROUP_CONCAT(name, ', ') as brands
        FROM brands 
        GROUP BY country
        ORDER BY brand_count DESC
        """
        return self.execute_query(query)
    
    def get_zodiac_distribution(self) -> List[Dict[str, Any]]:
        """Get distribution of brands by Western zodiac signs."""
        query = """
        SELECT 
            ba.western_zodiac,
            COUNT(*) as brand_count,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE ba.western_zodiac IS NOT NULL
        GROUP BY ba.western_zodiac
        ORDER BY brand_count DESC
        """
        return self.execute_query(query)
    
    def get_chinese_zodiac_distribution(self) -> List[Dict[str, Any]]:
        """Get distribution of brands by Chinese zodiac animals."""
        query = """
        SELECT 
            ba.chinese_animal,
            ba.chinese_element,
            COUNT(*) as brand_count,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE ba.chinese_animal IS NOT NULL
        GROUP BY ba.chinese_animal, ba.chinese_element
        ORDER BY brand_count DESC
        """
        return self.execute_query(query)
    
    def get_numerology_analysis(self) -> Dict[str, Any]:
        """Get numerology analysis of all brands."""
        # Life path number distribution
        life_path_query = """
        SELECT 
            life_path_number,
            COUNT(*) as count,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE life_path_number IS NOT NULL
        GROUP BY life_path_number
        ORDER BY life_path_number
        """
        
        # Expression number distribution
        expression_query = """
        SELECT 
            expression_number,
            COUNT(*) as count,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE expression_number IS NOT NULL
        GROUP BY expression_number
        ORDER BY expression_number
        """
        
        # Chaldean number distribution
        chaldean_query = """
        SELECT 
            chaldean_number,
            COUNT(*) as count,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE chaldean_number IS NOT NULL
        GROUP BY chaldean_number
        ORDER BY chaldean_number
        """
        
        return {
            'life_path_numbers': self.execute_query(life_path_query),
            'expression_numbers': self.execute_query(expression_query),
            'chaldean_numbers': self.execute_query(chaldean_query)
        }
    
    def get_founders_info(self) -> List[Dict[str, Any]]:
        """Get all founder information."""
        query = """
        SELECT 
            b.name as brand_name,
            b.category,
            f.full_name,
            f.birth_date,
            f.western_zodiac,
            f.chinese_animal,
            f.chinese_element,
            f.life_path_number,
            f.expression_number
        FROM founders f
        JOIN brands b ON f.brand_id = b.id
        ORDER BY b.name
        """
        return self.execute_query(query)
    
    def search_brands(self, search_term: str) -> List[Dict[str, Any]]:
        """Search brands by name, category, or country."""
        query = """
        SELECT 
            b.*,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element
        FROM brands b
        LEFT JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE b.name LIKE ? OR b.category LIKE ? OR b.country LIKE ?
        ORDER BY b.name
        """
        search_pattern = f"%{search_term}%"
        return self.execute_query(query, (search_pattern, search_pattern, search_pattern))
    
    def generate_report(self) -> str:
        """Generate a comprehensive analysis report."""
        report = []
        report.append("=" * 60)
        report.append("GLOBAL BRANDS DATABASE ANALYSIS REPORT")
        report.append("=" * 60)
        
        # Total brands
        total_brands = len(self.get_all_brands())
        report.append(f"\nTotal Brands in Database: {total_brands}")
        
        # Category breakdown
        report.append("\n" + "-" * 40)
        report.append("BRANDS BY CATEGORY")
        report.append("-" * 40)
        market_summary = self.get_market_cap_summary()
        for category in market_summary:
            report.append(f"{category['category']}: {category['brand_count']} brands")
            if category['avg_market_cap']:
                report.append(f"  Average Market Cap: ${category['avg_market_cap']:,.0f}")
                report.append(f"  Total Market Cap: ${category['total_market_cap']:,.0f}")
        
        # Country breakdown
        report.append("\n" + "-" * 40)
        report.append("BRANDS BY COUNTRY")
        report.append("-" * 40)
        country_summary = self.get_country_summary()
        for country in country_summary:
            report.append(f"{country['country']}: {country['brand_count']} brands")
        
        # Zodiac distribution
        report.append("\n" + "-" * 40)
        report.append("WESTERN ZODIAC DISTRIBUTION")
        report.append("-" * 40)
        zodiac_dist = self.get_zodiac_distribution()
        for zodiac in zodiac_dist:
            report.append(f"{zodiac['western_zodiac']}: {zodiac['brand_count']} brands")
        
        # Chinese zodiac distribution
        report.append("\n" + "-" * 40)
        report.append("CHINESE ZODIAC DISTRIBUTION")
        report.append("-" * 40)
        chinese_dist = self.get_chinese_zodiac_distribution()
        for chinese in chinese_dist:
            report.append(f"{chinese['chinese_animal']} ({chinese['chinese_element']}): {chinese['brand_count']} brands")
        
        # Numerology analysis
        report.append("\n" + "-" * 40)
        report.append("NUMEROLOGY ANALYSIS")
        report.append("-" * 40)
        numerology = self.get_numerology_analysis()
        
        report.append("\nLife Path Numbers:")
        for lp in numerology['life_path_numbers']:
            report.append(f"  Number {lp['life_path_number']}: {lp['count']} brands")
        
        report.append("\nExpression Numbers:")
        for exp in numerology['expression_numbers']:
            report.append(f"  Number {exp['expression_number']}: {exp['count']} brands")
        
        report.append("\nChaldean Numbers:")
        for chal in numerology['chaldean_numbers']:
            report.append(f"  Number {chal['chaldean_number']}: {chal['count']} brands")
        
        # Founders
        founders = self.get_founders_info()
        report.append(f"\n" + "-" * 40)
        report.append(f"FOUNDER INFORMATION ({len(founders)} founders)")
        report.append("-" * 40)
        for founder in founders:
            report.append(f"{founder['brand_name']}: {founder['full_name']}")
            if founder['birth_date']:
                report.append(f"  Born: {founder['birth_date']} ({founder['western_zodiac']})")
        
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)


def main():
    """Run database analysis and generate report."""
    analyzer = BrandAnalyzer()
    
    print("Generating comprehensive brand database analysis...")
    report = analyzer.generate_report()
    print(report)
    
    # Save report to file
    with open('/workspace/brand_analysis_report.txt', 'w') as f:
        f.write(report)
    print(f"\nReport saved to: /workspace/brand_analysis_report.txt")


if __name__ == "__main__":
    main()