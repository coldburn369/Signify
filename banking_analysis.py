#!/usr/bin/env python3
"""
Comprehensive Banking Sector Analysis
Specialized analysis of all banking institutions with focus on European and German banks.
"""

from database_query import BrandAnalyzer


class BankingAnalyzer(BrandAnalyzer):
    """Specialized analyzer for banking industry."""
    
    def get_banking_institutions_analysis(self):
        """Get comprehensive analysis of all banking institutions."""
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
        WHERE b.category = 'Banking'
        ORDER BY b.market_cap DESC NULLS LAST, b.name
        """
        return self.execute_query(query)
    
    def get_german_banks_analysis(self):
        """Analyze German banking institutions specifically."""
        query = """
        SELECT 
            b.name,
            b.founding_date,
            b.market_cap,
            ba.western_zodiac,
            ba.life_path_number,
            bc.colors
        FROM brands b
        LEFT JOIN brand_astro_data ba ON b.id = ba.brand_id
        LEFT JOIN brand_cultural_data bc ON b.id = bc.brand_id
        WHERE b.category = 'Banking' AND b.country = 'Germany'
        ORDER BY b.market_cap DESC NULLS LAST, b.name
        """
        return self.execute_query(query)
    
    def get_european_banks_by_country(self):
        """Analyze European banks by country."""
        european_countries = ['Germany', 'France', 'United Kingdom', 'Italy', 'Spain', 
                             'Netherlands', 'Switzerland', 'Austria', 'Belgium', 'Finland', 
                             'Denmark', 'Sweden', 'Portugal', 'Poland']
        
        placeholders = ','.join(['?' for _ in european_countries])
        query = f"""
        SELECT 
            country,
            COUNT(*) as bank_count,
            SUM(market_cap) as total_market_cap,
            AVG(market_cap) as avg_market_cap,
            GROUP_CONCAT(name, ', ') as banks
        FROM brands 
        WHERE category = 'Banking' AND country IN ({placeholders})
        GROUP BY country
        ORDER BY bank_count DESC, total_market_cap DESC NULLS LAST
        """
        return self.execute_query_with_params(query, european_countries)
    
    def get_banking_zodiac_patterns(self):
        """Analyze zodiac patterns in banking institutions."""
        query = """
        SELECT 
            ba.western_zodiac,
            COUNT(*) as bank_count,
            AVG(b.market_cap) as avg_market_cap,
            GROUP_CONCAT(b.name, ', ') as banks
        FROM brand_astro_data ba
        JOIN brands b ON ba.brand_id = b.id
        WHERE b.category = 'Banking'
        GROUP BY ba.western_zodiac
        ORDER BY bank_count DESC
        """
        return self.execute_query(query)
    
    def get_banking_founding_periods(self):
        """Analyze banking institutions by founding periods."""
        query = """
        SELECT 
            CASE 
                WHEN founding_date < '1850-01-01' THEN 'Historic (Pre-1850)'
                WHEN founding_date < '1900-01-01' THEN '19th Century (1850-1900)'
                WHEN founding_date < '1950-01-01' THEN 'Early Modern (1900-1950)'
                WHEN founding_date < '2000-01-01' THEN 'Modern Era (1950-2000)'
                ELSE 'Contemporary (2000+)'
            END as period,
            COUNT(*) as bank_count,
            AVG(market_cap) as avg_market_cap,
            GROUP_CONCAT(name, ', ') as banks
        FROM brands 
        WHERE category = 'Banking'
        GROUP BY period
        ORDER BY MIN(founding_date)
        """
        return self.execute_query(query)
    
    def get_banking_founders_analysis(self):
        """Analyze banking institution founders."""
        query = """
        SELECT 
            f.full_name,
            f.birth_date,
            f.western_zodiac,
            f.chinese_animal,
            b.name as bank_name,
            b.country,
            b.market_cap,
            b.founding_date
        FROM founders f
        JOIN brands b ON f.brand_id = b.id
        WHERE b.category = 'Banking'
        ORDER BY b.market_cap DESC NULLS LAST
        """
        return self.execute_query(query)
    
    def execute_query_with_params(self, query, params):
        """Execute query with parameters."""
        import sqlite3
        
        try:
            conn = sqlite3.connect('/workspace/brands.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            
            results = []
            for row in cursor.fetchall():
                results.append(dict(row))
            
            conn.close()
            return results
        except Exception as e:
            print(f"Database error: {e}")
            return []
    
    def generate_banking_report(self):
        """Generate comprehensive banking sector report."""
        report = []
        report.append("=" * 80)
        report.append("COMPREHENSIVE BANKING SECTOR ANALYSIS")
        report.append("=" * 80)
        
        # Get all banking institutions
        banking_institutions = self.get_banking_institutions_analysis()
        total_banks = len(banking_institutions)
        
        report.append(f"\nTotal Banking Institutions in Database: {total_banks}")
        
        # Market cap analysis
        banks_with_market_cap = [b for b in banking_institutions if b['market_cap']]
        total_market_cap = sum(b['market_cap'] for b in banks_with_market_cap)
        avg_market_cap = total_market_cap / len(banks_with_market_cap) if banks_with_market_cap else 0
        
        report.append(f"Banks with Market Cap Data: {len(banks_with_market_cap)}")
        report.append(f"Total Banking Market Cap: ${total_market_cap:,}")
        report.append(f"Average Bank Market Cap: ${avg_market_cap:,.0f}")
        
        # Top banks by market cap
        report.append("\n" + "=" * 60)
        report.append("TOP BANKING INSTITUTIONS BY MARKET VALUE")
        report.append("=" * 60)
        
        top_banks = sorted(banks_with_market_cap, key=lambda x: x['market_cap'], reverse=True)[:10]
        for i, bank in enumerate(top_banks, 1):
            market_cap = f"${bank['market_cap']:,}" if bank['market_cap'] else "N/A"
            report.append(f"{i:2d}. {bank['name']} ({bank['country']}) - {market_cap}")
            report.append(f"    Founded: {bank['founding_date']} | Zodiac: {bank['western_zodiac']}")
        
        # German banks analysis
        report.append("\n" + "=" * 60)
        report.append("GERMAN BANKING POWERHOUSES")
        report.append("=" * 60)
        
        german_banks = self.get_german_banks_analysis()
        report.append(f"Total German Banks: {len(german_banks)}")
        
        german_with_cap = [b for b in german_banks if b['market_cap']]
        if german_with_cap:
            german_total_cap = sum(b['market_cap'] for b in german_with_cap)
            german_avg_cap = german_total_cap / len(german_with_cap)
            report.append(f"German Banks Market Cap: ${german_total_cap:,}")
            report.append(f"German Banks Average Cap: ${german_avg_cap:,.0f}")
        
        report.append("\nGerman Banking Institutions:")
        for i, bank in enumerate(german_banks, 1):
            market_cap = f"${bank['market_cap']:,}" if bank['market_cap'] else "State/Cooperative"
            founding_year = bank['founding_date'].split('-')[0] if bank['founding_date'] else "N/A"
            report.append(f"{i:2d}. {bank['name']} (Est. {founding_year}) - {market_cap}")
            report.append(f"    Zodiac: {bank['western_zodiac']} | Life Path: {bank['life_path_number']}")
        
        # European banks by country
        report.append("\n" + "=" * 60)
        report.append("EUROPEAN BANKING BY COUNTRY")
        report.append("=" * 60)
        
        european_analysis = self.get_european_banks_by_country()
        for country in european_analysis:
            total_cap = f"${country['total_market_cap']:,}" if country['total_market_cap'] else "Private/State-Owned"
            avg_cap = f"${country['avg_market_cap']:,.0f}" if country['avg_market_cap'] else "N/A"
            report.append(f"\n{country['country']}: {country['bank_count']} banks")
            report.append(f"  Total Market Cap: {total_cap}")
            report.append(f"  Average Market Cap: {avg_cap}")
            
            # Show sample banks
            banks_list = country['banks'].split(', ') if country['banks'] else []
            if len(banks_list) <= 3:
                report.append(f"  Banks: {country['banks']}")
            else:
                report.append(f"  Sample Banks: {', '.join(banks_list[:3])}")
                if len(banks_list) > 3:
                    report.append(f"  Additional: {', '.join(banks_list[3:])}")
        
        # Banking zodiac analysis
        report.append("\n" + "=" * 60)
        report.append("BANKING INSTITUTIONS BY ZODIAC SIGN")
        report.append("=" * 60)
        
        zodiac_analysis = self.get_banking_zodiac_patterns()
        for zodiac in zodiac_analysis:
            avg_cap = f"${zodiac['avg_market_cap']:,.0f}" if zodiac['avg_market_cap'] else "N/A"
            report.append(f"\n{zodiac['western_zodiac']}: {zodiac['bank_count']} banks (Avg: {avg_cap})")
            banks_list = zodiac['banks'].split(', ') if zodiac['banks'] else []
            if len(banks_list) <= 4:
                report.append(f"  {zodiac['banks']}")
            else:
                report.append(f"  {', '.join(banks_list[:4])} + {len(banks_list)-4} more")
        
        # Historical founding periods
        report.append("\n" + "=" * 60)
        report.append("BANKING INSTITUTIONS BY FOUNDING ERA")
        report.append("=" * 60)
        
        period_analysis = self.get_banking_founding_periods()
        for period in period_analysis:
            avg_cap = f"${period['avg_market_cap']:,.0f}" if period['avg_market_cap'] else "N/A"
            report.append(f"\n{period['period']}: {period['bank_count']} banks (Avg: {avg_cap})")
            banks_list = period['banks'].split(', ') if period['banks'] else []
            if len(banks_list) <= 3:
                report.append(f"  {period['banks']}")
            else:
                report.append(f"  {', '.join(banks_list[:3])} + {len(banks_list)-3} more")
        
        # Banking founders analysis
        report.append("\n" + "=" * 60)
        report.append("BANKING INDUSTRY FOUNDERS")
        report.append("=" * 60)
        
        founders = self.get_banking_founders_analysis()
        report.append(f"Total Banking Founders: {len(founders)}")
        
        if founders:
            report.append("\nNotable Banking Founders:")
            for founder in founders[:10]:
                market_cap = f"${founder['market_cap']:,}" if founder['market_cap'] else "State/Private"
                founding_year = founder['founding_date'].split('-')[0] if founder['founding_date'] else "N/A"
                report.append(f"  {founder['full_name']} ({founder['bank_name']}, {founding_year}) - {market_cap}")
                if founder['birth_date']:
                    birth_year = founder['birth_date'].split('-')[0]
                    report.append(f"    Born: {birth_year} ({founder['western_zodiac']})")
        
        # Banking sector insights
        report.append("\n" + "=" * 60)
        report.append("EUROPEAN BANKING INSIGHTS")
        report.append("=" * 60)
        
        # Regional dominance
        report.append("Regional Banking Centers:")
        regional_insights = {
            'Germany': 'Financial center of Central Europe - Frankfurt as EU financial hub',
            'France': 'Global banking leaders - Universal banking model pioneers',
            'United Kingdom': 'International financial services - City of London tradition',
            'Netherlands': 'Commercial banking innovation - International trade finance',
            'Italy': 'Regional banking strength - Cooperative banking tradition',
            'Spain': 'Latin American expansion leaders - Global retail banking',
            'Switzerland': 'Private banking and wealth management excellence',
            'Nordic': 'Sustainable banking leadership - Digital innovation pioneers'
        }
        
        country_stats = {c['country']: c for c in european_analysis}
        for region, description in regional_insights.items():
            if region in country_stats:
                stats = country_stats[region]
                report.append(f"\n{region}: {description}")
                report.append(f"  Banks: {stats['bank_count']} | Market Cap: ${stats['total_market_cap']:,}" if stats['total_market_cap'] else f"  Banks: {stats['bank_count']} | Market Cap: Mixed Ownership")
            elif region == 'Nordic':
                nordic_countries = ['Finland', 'Sweden', 'Denmark']
                nordic_banks = sum(country_stats.get(c, {'bank_count': 0})['bank_count'] for c in nordic_countries if c in country_stats)
                report.append(f"\n{region}: {description}")
                report.append(f"  Banks: {nordic_banks} across Finland, Sweden, Denmark")
        
        # Banking model analysis
        report.append("\n" + "=" * 60)
        report.append("EUROPEAN BANKING MODELS")
        report.append("=" * 60)
        
        banking_models = [
            "Universal Banking (Germany): Comprehensive financial services under one roof",
            "Cooperative Banking (Germany/Austria): Member-owned, community-focused institutions", 
            "Retail Banking (UK/Netherlands): Consumer-focused, digital-first approaches",
            "Investment Banking (Switzerland/UK): Wealth management and capital markets",
            "State Banking (Germany): Development and promotional banking for economic growth",
            "Regional Banking (Italy/Spain): Localized banking with international expansion"
        ]
        
        for model in banking_models:
            report.append(f"• {model}")
        
        report.append("\n" + "=" * 80)
        
        return "\n".join(report)


def main():
    """Run comprehensive banking sector analysis."""
    analyzer = BankingAnalyzer()
    
    print("Generating comprehensive banking sector analysis...")
    report = analyzer.generate_banking_report()
    print(report)
    
    # Save report
    with open('/workspace/banking_analysis_report.txt', 'w') as f:
        f.write(report)
    print(f"\nBanking analysis saved to: /workspace/banking_analysis_report.txt")


if __name__ == "__main__":
    main()