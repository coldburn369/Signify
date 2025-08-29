#!/usr/bin/env python3
"""
Specialized Automotive Brands Analysis
Comprehensive analysis of all automotive brands in the database.
"""

from database_query import BrandAnalyzer


class AutomotiveAnalyzer(BrandAnalyzer):
    """Specialized analyzer for automotive brands."""
    
    def get_automotive_brands_analysis(self):
        """Get comprehensive analysis of automotive brands."""
        query = """
        SELECT 
            b.name,
            b.founding_date,
            b.country,
            b.parent_company,
            b.market_cap,
            ba.western_zodiac,
            ba.chinese_animal,
            ba.chinese_element,
            ba.life_path_number,
            ba.expression_number,
            bc.colors
        FROM brands b
        LEFT JOIN brand_astro_data ba ON b.id = ba.brand_id
        LEFT JOIN brand_cultural_data bc ON b.id = bc.brand_id
        WHERE b.category = 'Automotive'
        ORDER BY b.market_cap DESC NULLS LAST, b.name
        """
        return self.execute_query(query)
    
    def get_automotive_by_country(self):
        """Get automotive brands grouped by country."""
        query = """
        SELECT 
            country,
            COUNT(*) as brand_count,
            SUM(market_cap) as total_market_cap,
            AVG(market_cap) as avg_market_cap,
            GROUP_CONCAT(name, ', ') as brands
        FROM brands 
        WHERE category = 'Automotive'
        GROUP BY country
        ORDER BY brand_count DESC
        """
        return self.execute_query(query)
    
    def get_automotive_by_decade(self):
        """Get automotive brands by founding decade."""
        query = """
        SELECT 
            CASE 
                WHEN CAST(SUBSTR(founding_date, 1, 4) AS INTEGER) < 1900 THEN 'Pre-1900'
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
        WHERE category = 'Automotive'
        GROUP BY period
        ORDER BY period
        """
        return self.execute_query(query)
    
    def get_automotive_founders_analysis(self):
        """Analyze automotive brand founders."""
        query = """
        SELECT 
            f.full_name,
            f.birth_date,
            f.western_zodiac,
            f.chinese_animal,
            f.chinese_element,
            b.name as brand_name,
            b.country,
            b.market_cap
        FROM founders f
        JOIN brands b ON f.brand_id = b.id
        WHERE b.category = 'Automotive'
        ORDER BY b.market_cap DESC NULLS LAST
        """
        return self.execute_query(query)
    
    def get_automotive_zodiac_patterns(self):
        """Analyze zodiac patterns in automotive brands."""
        query = """
        SELECT 
            ba.western_zodiac,
            COUNT(*) as brand_count,
            AVG(b.market_cap) as avg_market_cap,
            GROUP_CONCAT(b.name, ', ') as brands
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE b.category = 'Automotive'
        GROUP BY ba.western_zodiac
        ORDER BY brand_count DESC
        """
        return self.execute_query(query)
    
    def generate_automotive_report(self):
        """Generate comprehensive automotive industry report."""
        report = []
        report.append("=" * 80)
        report.append("COMPREHENSIVE AUTOMOTIVE BRANDS ANALYSIS")
        report.append("=" * 80)
        
        # Get all automotive brands
        automotive_brands = self.get_automotive_brands_analysis()
        total_brands = len(automotive_brands)
        
        report.append(f"\nTotal Automotive Brands in Database: {total_brands}")
        
        # Market cap analysis
        brands_with_market_cap = [b for b in automotive_brands if b['market_cap']]
        total_market_cap = sum(b['market_cap'] for b in brands_with_market_cap)
        avg_market_cap = total_market_cap / len(brands_with_market_cap) if brands_with_market_cap else 0
        
        report.append(f"Brands with Market Cap Data: {len(brands_with_market_cap)}")
        report.append(f"Total Automotive Market Cap: ${total_market_cap:,}")
        report.append(f"Average Market Cap: ${avg_market_cap:,.0f}")
        
        # Top 10 most valuable automotive brands
        report.append("\n" + "=" * 60)
        report.append("TOP 10 MOST VALUABLE AUTOMOTIVE BRANDS")
        report.append("=" * 60)
        
        top_brands = sorted(brands_with_market_cap, key=lambda x: x['market_cap'], reverse=True)[:10]
        for i, brand in enumerate(top_brands, 1):
            market_cap = f"${brand['market_cap']:,}" if brand['market_cap'] else "N/A"
            report.append(f"{i:2d}. {brand['name']} ({brand['country']}) - {market_cap}")
            report.append(f"    Founded: {brand['founding_date']} | Zodiac: {brand['western_zodiac']}")
        
        # Country analysis
        report.append("\n" + "=" * 60)
        report.append("AUTOMOTIVE BRANDS BY COUNTRY")
        report.append("=" * 60)
        
        country_analysis = self.get_automotive_by_country()
        for country in country_analysis:
            total_cap = f"${country['total_market_cap']:,}" if country['total_market_cap'] else "N/A"
            avg_cap = f"${country['avg_market_cap']:,.0f}" if country['avg_market_cap'] else "N/A"
            report.append(f"\n{country['country']}: {country['brand_count']} brands")
            report.append(f"  Total Market Cap: {total_cap}")
            report.append(f"  Average Market Cap: {avg_cap}")
            # Show first few brands
            brands_list = country['brands'].split(', ')
            if len(brands_list) <= 3:
                report.append(f"  Brands: {country['brands']}")
            else:
                report.append(f"  Brands: {', '.join(brands_list[:3])} + {len(brands_list)-3} more")
        
        # Historical analysis
        report.append("\n" + "=" * 60)
        report.append("AUTOMOTIVE BRANDS BY FOUNDING PERIOD")
        report.append("=" * 60)
        
        decade_analysis = self.get_automotive_by_decade()
        for decade in decade_analysis:
            report.append(f"\n{decade['period']}: {decade['brand_count']} brands")
            brands_list = decade['brands'].split(', ')
            if len(brands_list) <= 5:
                report.append(f"  {decade['brands']}")
            else:
                report.append(f"  {', '.join(brands_list[:5])} + {len(brands_list)-5} more")
        
        # Zodiac analysis
        report.append("\n" + "=" * 60)
        report.append("AUTOMOTIVE BRANDS BY ZODIAC SIGN")
        report.append("=" * 60)
        
        zodiac_analysis = self.get_automotive_zodiac_patterns()
        for zodiac in zodiac_analysis:
            avg_cap = f"${zodiac['avg_market_cap']:,.0f}" if zodiac['avg_market_cap'] else "N/A"
            report.append(f"\n{zodiac['western_zodiac']}: {zodiac['brand_count']} brands (Avg: {avg_cap})")
            brands_list = zodiac['brands'].split(', ')
            if len(brands_list) <= 4:
                report.append(f"  {zodiac['brands']}")
            else:
                report.append(f"  {', '.join(brands_list[:4])} + {len(brands_list)-4} more")
        
        # Founders analysis
        report.append("\n" + "=" * 60)
        report.append("AUTOMOTIVE BRAND FOUNDERS")
        report.append("=" * 60)
        
        founders = self.get_automotive_founders_analysis()
        founders_with_market_cap = [f for f in founders if f['market_cap']]
        
        report.append(f"Total Founders with Data: {len(founders)}")
        report.append(f"Founders of Publicly Traded Brands: {len(founders_with_market_cap)}")
        
        # Top founders by brand value
        if founders_with_market_cap:
            report.append("\nTop Automotive Founders by Brand Value:")
            top_founders = sorted(founders_with_market_cap, key=lambda x: x['market_cap'], reverse=True)[:5]
            for founder in top_founders:
                market_cap = f"${founder['market_cap']:,}"
                report.append(f"  {founder['full_name']} ({founder['brand_name']}) - {market_cap}")
                if founder['birth_date']:
                    report.append(f"    Born: {founder['birth_date']} ({founder['western_zodiac']})")
        
        # Luxury vs Mass Market
        report.append("\n" + "=" * 60)
        report.append("LUXURY VS MASS MARKET ANALYSIS")
        report.append("=" * 60)
        
        luxury_brands = ['Ferrari N.V.', 'Lamborghini S.p.A.', 'Maserati S.p.A.', 'Aston Martin Lagonda', 
                        'Bentley Motors', 'Rolls-Royce Motor Cars', 'Porsche AG']
        
        luxury_data = [b for b in automotive_brands if b['name'] in luxury_brands and b['market_cap']]
        mass_market_data = [b for b in automotive_brands if b['name'] not in luxury_brands and b['market_cap']]
        
        if luxury_data:
            luxury_avg = sum(b['market_cap'] for b in luxury_data) / len(luxury_data)
            report.append(f"Luxury Brands Average Market Cap: ${luxury_avg:,.0f}")
            report.append(f"Luxury Brands Count: {len(luxury_data)}")
        
        if mass_market_data:
            mass_avg = sum(b['market_cap'] for b in mass_market_data) / len(mass_market_data)
            report.append(f"Mass Market Brands Average Market Cap: ${mass_avg:,.0f}")
            report.append(f"Mass Market Brands Count: {len(mass_market_data)}")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)


def main():
    """Run automotive analysis."""
    analyzer = AutomotiveAnalyzer()
    
    print("Generating comprehensive automotive brands analysis...")
    report = analyzer.generate_automotive_report()
    print(report)
    
    # Save report
    with open('/workspace/automotive_analysis_report.txt', 'w') as f:
        f.write(report)
    print(f"\nAutomotive analysis saved to: /workspace/automotive_analysis_report.txt")


if __name__ == "__main__":
    main()