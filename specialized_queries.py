#!/usr/bin/env python3
"""
Specialized Query Tools for Brand Analysis
Advanced queries for brand research and analysis.
"""

from database_query import BrandAnalyzer
import json


class AdvancedBrandAnalyzer(BrandAnalyzer):
    """Advanced analysis tools for brand database."""
    
    def get_brands_by_decade(self):
        """Analyze brands by founding decade."""
        query = """
        SELECT 
            (founding_date / 10) * 10 as decade,
            COUNT(*) as brand_count,
            GROUP_CONCAT(name, ', ') as brands
        FROM brands 
        WHERE founding_date IS NOT NULL
        GROUP BY decade
        ORDER BY decade
        """
        # Note: SQLite date handling - convert to year
        query = """
        SELECT 
            CASE 
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1850 THEN '1800s'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1900 THEN '1850-1899'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1920 THEN '1900-1919'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1940 THEN '1920-1939'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1960 THEN '1940-1959'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1980 THEN '1960-1979'
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 2000 THEN '1980-1999'
                ELSE '2000+'
            END as period,
            COUNT(*) as brand_count,
            GROUP_CONCAT(name, ', ') as brands
        FROM brands 
        WHERE founding_date IS NOT NULL
        GROUP BY period
        ORDER BY period
        """
        return self.execute_query(query)
    
    def get_most_valuable_by_category(self):
        """Get the most valuable brand in each category."""
        query = """
        SELECT 
            b1.category,
            b1.name,
            b1.market_cap,
            b1.country,
            ba.western_zodiac,
            ba.chinese_animal
        FROM brands b1
        LEFT JOIN brand_astro_data ba ON b1.id = ba.brand_id
        WHERE b1.market_cap = (
            SELECT MAX(b2.market_cap) 
            FROM brands b2 
            WHERE b2.category = b1.category AND b2.market_cap IS NOT NULL
        )
        ORDER BY b1.market_cap DESC
        """
        return self.execute_query(query)
    
    def get_zodiac_performance(self):
        """Analyze market performance by zodiac signs."""
        query = """
        SELECT 
            ba.western_zodiac,
            COUNT(*) as brand_count,
            AVG(b.market_cap) as avg_market_cap,
            SUM(b.market_cap) as total_market_cap,
            MAX(b.market_cap) as max_market_cap,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE b.market_cap IS NOT NULL
        GROUP BY ba.western_zodiac
        ORDER BY avg_market_cap DESC
        """
        return self.execute_query(query)
    
    def get_numerology_success_patterns(self):
        """Analyze success patterns by numerology numbers."""
        life_path_query = """
        SELECT 
            ba.life_path_number,
            COUNT(*) as brand_count,
            AVG(b.market_cap) as avg_market_cap,
            SUM(b.market_cap) as total_market_cap,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE b.market_cap IS NOT NULL AND ba.life_path_number IS NOT NULL
        GROUP BY ba.life_path_number
        ORDER BY avg_market_cap DESC
        """
        
        expression_query = """
        SELECT 
            ba.expression_number,
            COUNT(*) as brand_count,
            AVG(b.market_cap) as avg_market_cap,
            SUM(b.market_cap) as total_market_cap,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE b.market_cap IS NOT NULL AND ba.expression_number IS NOT NULL
        GROUP BY ba.expression_number
        ORDER BY avg_market_cap DESC
        """
        
        return {
            'life_path_analysis': self.execute_query(life_path_query),
            'expression_analysis': self.execute_query(expression_query)
        }
    
    def get_cultural_color_analysis(self):
        """Analyze brands by their cultural colors."""
        query = """
        SELECT 
            bc.colors,
            COUNT(*) as brand_count,
            AVG(b.market_cap) as avg_market_cap,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_cultural_data bc
        JOIN brands b ON bc.brand_id = b.id
        WHERE b.market_cap IS NOT NULL AND bc.colors IS NOT NULL
        GROUP BY bc.colors
        HAVING COUNT(*) > 1
        ORDER BY avg_market_cap DESC
        """
        return self.execute_query(query)
    
    def get_founder_zodiac_analysis(self):
        """Analyze founder zodiac distribution and success."""
        query = """
        SELECT 
            f.western_zodiac,
            COUNT(*) as founder_count,
            AVG(b.market_cap) as avg_brand_market_cap,
            GROUP_CONCAT(f.full_name || ' (' || b.name || ')', ', ') as founders_brands
        FROM founders f
        JOIN brands b ON f.brand_id = b.id
        WHERE f.western_zodiac IS NOT NULL AND b.market_cap IS NOT NULL
        GROUP BY f.western_zodiac
        ORDER BY avg_brand_market_cap DESC
        """
        return self.execute_query(query)
    
    def get_country_market_dominance(self):
        """Analyze market dominance by country."""
        query = """
        SELECT 
            b.country,
            COUNT(*) as brand_count,
            SUM(b.market_cap) as total_market_cap,
            AVG(b.market_cap) as avg_market_cap,
            MAX(b.market_cap) as largest_brand_value
        FROM brands b
        WHERE b.market_cap IS NOT NULL
        GROUP BY b.country
        ORDER BY total_market_cap DESC
        """
        return self.execute_query(query)
    
    def search_astrological_patterns(self, zodiac_sign: str = None, chinese_animal: str = None):
        """Search for specific astrological patterns."""
        conditions = []
        params = []
        
        if zodiac_sign:
            conditions.append("ba.western_zodiac = ?")
            params.append(zodiac_sign)
        
        if chinese_animal:
            conditions.append("ba.chinese_animal = ?")
            params.append(chinese_animal)
        
        where_clause = " AND ".join(conditions) if conditions else "1=1"
        
        query = f"""
        SELECT 
            b.name,
            b.category,
            b.country,
            b.founding_date,
            b.market_cap,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element,
            ba.life_path_number,
            ba.expression_number
        FROM brands b
        JOIN brand_astro_data ba ON b.id = ba.brand_id
        WHERE {where_clause}
        ORDER BY b.market_cap DESC
        """
        return self.execute_query(query, tuple(params))
    
    def generate_advanced_report(self):
        """Generate comprehensive advanced analysis report."""
        report = []
        report.append("=" * 80)
        report.append("ADVANCED GLOBAL BRANDS ASTROLOGICAL ANALYSIS")
        report.append("=" * 80)
        
        # Decade analysis
        report.append("\n" + "=" * 60)
        report.append("BRANDS BY FOUNDING PERIOD")
        report.append("=" * 60)
        decades = self.get_brands_by_decade()
        for decade in decades:
            report.append(f"\n{decade['period']}: {decade['brand_count']} brands")
            report.append(f"  {decade['brands']}")
        
        # Most valuable by category
        report.append("\n" + "=" * 60)
        report.append("MOST VALUABLE BRAND BY CATEGORY")
        report.append("=" * 60)
        top_brands = self.get_most_valuable_by_category()
        for brand in top_brands:
            market_cap = f"${brand['market_cap']:,}" if brand['market_cap'] else "N/A"
            report.append(f"\n{brand['category']}: {brand['name']} ({brand['country']})")
            report.append(f"  Market Cap: {market_cap}")
            report.append(f"  Zodiac: {brand['western_zodiac']} | Chinese: {brand['chinese_animal']}")
        
        # Zodiac performance
        report.append("\n" + "=" * 60)
        report.append("MARKET PERFORMANCE BY WESTERN ZODIAC")
        report.append("=" * 60)
        zodiac_perf = self.get_zodiac_performance()
        for zodiac in zodiac_perf:
            avg_cap = f"${zodiac['avg_market_cap']:,.0f}" if zodiac['avg_market_cap'] else "N/A"
            total_cap = f"${zodiac['total_market_cap']:,}" if zodiac['total_market_cap'] else "N/A"
            report.append(f"\n{zodiac['western_zodiac']}: {zodiac['brand_count']} brands")
            report.append(f"  Average Market Cap: {avg_cap}")
            report.append(f"  Total Market Cap: {total_cap}")
        
        # Numerology patterns
        report.append("\n" + "=" * 60)
        report.append("NUMEROLOGY SUCCESS PATTERNS")
        report.append("=" * 60)
        numerology = self.get_numerology_success_patterns()
        
        report.append("\nLife Path Number Performance:")
        for lp in numerology['life_path_analysis']:
            avg_cap = f"${lp['avg_market_cap']:,.0f}" if lp['avg_market_cap'] else "N/A"
            report.append(f"  Number {lp['life_path_number']}: {lp['brand_count']} brands - Avg: {avg_cap}")
        
        report.append("\nExpression Number Performance:")
        for exp in numerology['expression_analysis']:
            avg_cap = f"${exp['avg_market_cap']:,.0f}" if exp['avg_market_cap'] else "N/A"
            report.append(f"  Number {exp['expression_number']}: {exp['brand_count']} brands - Avg: {avg_cap}")
        
        # Founder analysis
        report.append("\n" + "=" * 60)
        report.append("FOUNDER ZODIAC PERFORMANCE")
        report.append("=" * 60)
        founder_zodiac = self.get_founder_zodiac_analysis()
        for fz in founder_zodiac:
            avg_cap = f"${fz['avg_brand_market_cap']:,.0f}" if fz['avg_brand_market_cap'] else "N/A"
            report.append(f"\n{fz['western_zodiac']}: {fz['founder_count']} founders")
            report.append(f"  Average Brand Value: {avg_cap}")
        
        # Country dominance
        report.append("\n" + "=" * 60)
        report.append("MARKET DOMINANCE BY COUNTRY")
        report.append("=" * 60)
        country_dom = self.get_country_market_dominance()
        for country in country_dom:
            total_cap = f"${country['total_market_cap']:,}" if country['total_market_cap'] else "N/A"
            avg_cap = f"${country['avg_market_cap']:,.0f}" if country['avg_market_cap'] else "N/A"
            report.append(f"\n{country['country']}: {country['brand_count']} brands")
            report.append(f"  Total Market Cap: {total_cap}")
            report.append(f"  Average Market Cap: {avg_cap}")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)


def main():
    """Run advanced analysis."""
    analyzer = AdvancedBrandAnalyzer()
    
    print("Generating advanced astrological brand analysis...")
    report = analyzer.generate_advanced_report()
    print(report)
    
    # Save report
    with open('/workspace/advanced_brand_analysis.txt', 'w') as f:
        f.write(report)
    print(f"\nAdvanced analysis saved to: /workspace/advanced_brand_analysis.txt")
    
    # Example specialized queries
    print("\n" + "=" * 60)
    print("EXAMPLE: VIRGO BRANDS")
    print("=" * 60)
    virgo_brands = analyzer.search_astrological_patterns(zodiac_sign='Virgo')
    for brand in virgo_brands:
        market_cap = f"${brand['market_cap']:,}" if brand['market_cap'] else "N/A"
        print(f"{brand['name']} ({brand['category']}) - {market_cap}")


if __name__ == "__main__":
    main()