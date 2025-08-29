#!/usr/bin/env python3
"""
Final Brands Database Expansion
Adding brands from emerging markets and underrepresented regions.
"""

from brand_research import BrandResearcher


def get_final_expansion_brands():
    """Return final set of brands for maximum global diversity."""
    return [
        # Chinese Technology Giants
        {
            'name': 'Alibaba Group',
            'category': 'E-commerce',
            'founding_date': '1999-06-28',
            'country': 'China',
            'parent_company': None,
            'stock_ticker': 'BABA',
            'market_cap': 210000000000,  # $210B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Alibaba-Logo.png',
            'tagline': 'To Make it Easy to Do Business Anywhere',
            'cultural_data': {
                'colors': 'Orange, White',
                'notes': 'Named after Ali Baba and the 40 thieves. Orange represents energy and enthusiasm.'
            },
            'founder_data': {
                'full_name': 'Jack Ma',
                'birth_date': '1964-09-10'
            }
        },
        {
            'name': 'Tencent Holdings',
            'category': 'Technology',
            'founding_date': '1998-11-11',
            'country': 'China',
            'parent_company': None,
            'stock_ticker': 'TCEHY',
            'market_cap': 350000000000,  # $350B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Tencent-Logo.png',
            'tagline': 'Tech for Good',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Penguin mascot represents friendliness and innovation. Blue symbolizes trust and technology.'
            },
            'founder_data': {
                'full_name': 'Ma Huateng',
                'birth_date': '1971-10-29'
            }
        },
        
        # Indian Technology & Services
        {
            'name': 'Tata Consultancy Services',
            'category': 'Technology Services',
            'founding_date': '1968-04-01',
            'country': 'India',
            'parent_company': 'Tata Group',
            'stock_ticker': 'TCS',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/TCS-Logo.png',
            'tagline': 'Building on Belief',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Represents Indian IT excellence. Blue signifies trust and global presence.'
            }
        },
        {
            'name': 'Infosys Limited',
            'category': 'Technology Services',
            'founding_date': '1981-07-02',
            'country': 'India',
            'parent_company': None,
            'stock_ticker': 'INFY',
            'market_cap': 75000000000,  # $75B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Infosys-Logo.png',
            'tagline': 'Navigate Your Next',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'Infinity symbol represents limitless possibilities. Blue and orange represent stability and energy.'
            },
            'founder_data': {
                'full_name': 'N. R. Narayana Murthy',
                'birth_date': '1946-08-20'
            }
        },
        
        # European Conglomerates
        {
            'name': 'Siemens AG',
            'category': 'Industrial Conglomerate',
            'founding_date': '1847-10-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'SIEGY',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Siemens-Logo.png',
            'tagline': 'Ingenuity for Life',
            'cultural_data': {
                'colors': 'Teal, White',
                'notes': 'Teal represents innovation and technology. German engineering excellence and precision.'
            },
            'founder_data': {
                'full_name': 'Werner von Siemens',
                'birth_date': '1816-12-13'
            }
        },
        {
            'name': 'ASML Holding',
            'category': 'Semiconductors',
            'founding_date': '1984-04-01',
            'country': 'Netherlands',
            'parent_company': None,
            'stock_ticker': 'ASML',
            'market_cap': 300000000000,  # $300B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ASML-Logo.png',
            'tagline': 'Advancing Moore\'s Law',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Leading semiconductor lithography technology. Blue represents precision and innovation.'
            }
        },
        
        # Japanese Conglomerates
        {
            'name': 'SoftBank Group',
            'category': 'Investment',
            'founding_date': '1981-09-03',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'SFTBY',
            'market_cap': 90000000000,  # $90B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/SoftBank-Logo.png',
            'tagline': 'Information Revolution - Happiness for Everyone',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Yellow represents optimism and innovation. Focus on AI and technology investments.'
            },
            'founder_data': {
                'full_name': 'Masayoshi Son',
                'birth_date': '1957-08-11'
            }
        },
        {
            'name': 'Panasonic Corporation',
            'category': 'Electronics',
            'founding_date': '1918-03-07',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'PCRFY',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Panasonic-Logo.png',
            'tagline': 'A Better Life, A Better World',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Represents Japanese quality and innovation. Blue symbolizes trust and reliability.'
            },
            'founder_data': {
                'full_name': 'Konosuke Matsushita',
                'birth_date': '1894-11-27'
            }
        },
        
        # Brazilian & Latin American
        {
            'name': 'Vale S.A.',
            'category': 'Mining',
            'founding_date': '1942-06-01',
            'country': 'Brazil',
            'parent_company': None,
            'stock_ticker': 'VALE',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Vale-Logo.png',
            'tagline': 'Transforming to Transform',
            'cultural_data': {
                'colors': 'Green, Blue',
                'notes': 'Green represents natural resources and sustainability. Leading iron ore producer.'
            }
        },
        {
            'name': 'Banco Santander',
            'category': 'Banking',
            'founding_date': '1857-05-15',
            'country': 'Spain',
            'parent_company': None,
            'stock_ticker': 'SAN',
            'market_cap': 55000000000,  # $55B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Santander-Logo.png',
            'tagline': 'The Bank that Never Sleeps',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Red flame represents passion and Spanish heritage. Global banking presence.'
            }
        },
        
        # Middle Eastern
        {
            'name': 'Saudi Aramco',
            'category': 'Energy',
            'founding_date': '1933-05-29',
            'country': 'Saudi Arabia',
            'parent_company': None,
            'stock_ticker': '2222.SR',
            'market_cap': 2000000000000,  # $2T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Saudi-Aramco-Logo.png',
            'tagline': 'Energy to the World',
            'cultural_data': {
                'colors': 'Blue, Green',
                'notes': 'Green represents Islamic heritage and growth. Blue symbolizes energy and reliability.'
            }
        },
        
        # Australian & Oceania
        {
            'name': 'BHP Group',
            'category': 'Mining',
            'founding_date': '1885-08-13',
            'country': 'Australia',
            'parent_company': None,
            'stock_ticker': 'BHP',
            'market_cap': 150000000000,  # $150B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BHP-Logo.png',
            'tagline': 'Think Big, Act Fast, Together',
            'cultural_data': {
                'colors': 'Orange, Black',
                'notes': 'Orange represents earth and mining. Australian mining giant with global operations.'
            }
        },
        
        # Canadian
        {
            'name': 'Shopify Inc.',
            'category': 'E-commerce',
            'founding_date': '2006-06-01',
            'country': 'Canada',
            'parent_company': None,
            'stock_ticker': 'SHOP',
            'market_cap': 80000000000,  # $80B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Shopify-Logo.png',
            'tagline': 'Make Commerce Better for Everyone',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'Green represents growth and commerce. Canadian e-commerce platform leader.'
            },
            'founder_data': {
                'full_name': 'Tobias Lütke',
                'birth_date': '1981-07-16'
            }
        },
        {
            'name': 'Royal Bank of Canada',
            'category': 'Banking',
            'founding_date': '1869-06-29',
            'country': 'Canada',
            'parent_company': None,
            'stock_ticker': 'RY',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/RBC-Logo.png',
            'tagline': 'Here for You',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Royal lion represents heritage and strength. Blue symbolizes trust and stability.'
            }
        },
        
        # Russian
        {
            'name': 'Gazprom',
            'category': 'Energy',
            'founding_date': '1989-08-17',
            'country': 'Russia',
            'parent_company': None,
            'stock_ticker': 'OGZPY',
            'market_cap': 70000000000,  # $70B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Gazprom-Logo.png',
            'tagline': 'National Treasure',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents natural gas and energy. Major global energy supplier.'
            }
        },
        
        # Korean Conglomerate
        {
            'name': 'LG Corporation',
            'category': 'Electronics',
            'founding_date': '1947-02-01',
            'country': 'South Korea',
            'parent_company': None,
            'stock_ticker': 'LGEIY',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LG-Logo.png',
            'tagline': 'Life\'s Good',
            'cultural_data': {
                'colors': 'Red, Grey',
                'notes': 'Smiling face in logo represents customer satisfaction. LG stands for Lucky GoldStar.'
            },
            'founder_data': {
                'full_name': 'Koo In-hwoi',
                'birth_date': '1907-08-27'
            }
        },
        
        # French Fashion & Luxury
        {
            'name': 'Kering',
            'category': 'Luxury Goods',
            'founding_date': '1963-01-01',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'PPRUY',
            'market_cap': 80000000000,  # $80B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Kering-Logo.png',
            'tagline': 'Empowering Imagination',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Minimalist design represents luxury sophistication. Parent of Gucci, Saint Laurent.'
            },
            'founder_data': {
                'full_name': 'François Pinault',
                'birth_date': '1936-08-21'
            }
        }
    ]


def add_final_expansion():
    """Add final expansion brands to complete global coverage."""
    researcher = BrandResearcher()
    final_brands = get_final_expansion_brands()
    
    print(f"Adding {len(final_brands)} brands for maximum global diversity...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(final_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nFinal expansion completed successfully!")
    
    # Generate final statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    countries = set(brand['country'] for brand in updated_brands)
    categories = set(brand['category'] for brand in updated_brands)
    
    print(f"\nFINAL DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    print(f"  Countries represented: {len(countries)}")
    print(f"  Categories covered: {len(categories)}")
    
    # Top countries by brand count
    country_counts = {}
    for brand in updated_brands:
        country = brand['country']
        country_counts[country] = country_counts.get(country, 0) + 1
    
    print(f"\nTop countries by brand count:")
    for country, count in sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {country}: {count} brands")
    
    # Calculate total market cap
    total_market_cap = sum(brand.get('market_cap', 0) for brand in updated_brands if brand.get('market_cap'))
    print(f"\nTotal represented market cap: ${total_market_cap:,}")


if __name__ == "__main__":
    add_final_expansion()