#!/usr/bin/env python3
"""
Extended Brand Data Collection
Additional diverse global brands to expand the database.
"""

from brand_research import BrandResearcher


def get_extended_brands_data():
    """Return additional diverse global brands data."""
    return [
        # Asian Technology Companies
        {
            'name': 'Samsung Electronics',
            'category': 'Technology',
            'founding_date': '1969-01-13',
            'country': 'South Korea',
            'parent_company': 'Samsung Group',
            'stock_ticker': 'SSNLF',
            'market_cap': 320000000000,  # $320B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Samsung-Logo.png',
            'tagline': 'Imagine the Possibilities',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Samsung means "three stars" in Korean. Blue represents reliability and technology innovation.'
            },
            'founder_data': {
                'full_name': 'Lee Byung-chul',
                'birth_date': '1910-02-12'
            }
        },
        {
            'name': 'Sony Corporation',
            'category': 'Technology',
            'founding_date': '1946-05-07',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'SNE',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Sony-Logo.png',
            'tagline': 'Make.Believe',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Name combines Latin sonus (sound) and English sonny (youth). Represents innovation and entertainment.'
            },
            'founder_data': {
                'full_name': 'Akio Morita',
                'birth_date': '1921-01-26'
            }
        },
        
        # Automotive - Asian Brands
        {
            'name': 'Honda Motor Co.',
            'category': 'Automotive',
            'founding_date': '1948-09-24',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'HMC',
            'market_cap': 50000000000,  # $50B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Honda-Logo.png',
            'tagline': 'The Power of Dreams',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'H logo represents Honda heritage. Red symbolizes energy and passion for engineering.'
            },
            'founder_data': {
                'full_name': 'Soichiro Honda',
                'birth_date': '1906-11-17'
            }
        },
        {
            'name': 'Hyundai Motor Company',
            'category': 'Automotive',
            'founding_date': '1967-12-29',
            'country': 'South Korea',
            'parent_company': 'Hyundai Motor Group',
            'stock_ticker': 'HYMTF',
            'market_cap': 35000000000,  # $35B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Hyundai-Logo.png',
            'tagline': 'New Thinking. New Possibilities.',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Oval H represents handshake between company and customer. Hyundai means "modernity" in Korean.'
            },
            'founder_data': {
                'full_name': 'Chung Ju-yung',
                'birth_date': '1915-11-25'
            }
        },
        
        # Food & Beverages
        {
            'name': 'McDonald\'s Corporation',
            'category': 'Food Service',
            'founding_date': '1940-05-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MCD',
            'market_cap': 180000000000,  # $180B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/McDonalds-Logo.png',
            'tagline': 'I\'m Lovin\' It',
            'cultural_data': {
                'colors': 'Red, Yellow',
                'notes': 'Golden Arches (M) represent consistency and familiarity. Red and yellow evoke appetite and energy.'
            },
            'founder_data': {
                'full_name': 'Ray Kroc',
                'birth_date': '1902-10-05'
            }
        },
        {
            'name': 'Nestlé S.A.',
            'category': 'Food & Beverages',
            'founding_date': '1866-08-20',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'NSRGY',
            'market_cap': 350000000000,  # $350B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Nestle-Logo.png',
            'tagline': 'Good Food, Good Life',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Nest with birds represents family, nurturing, and care. Blue evokes trust and quality.'
            },
            'founder_data': {
                'full_name': 'Henri Nestlé',
                'birth_date': '1814-08-10'
            }
        },
        {
            'name': 'Starbucks Corporation',
            'category': 'Food & Beverages',
            'founding_date': '1971-03-30',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'SBUX',
            'market_cap': 110000000000,  # $110B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Starbucks-Logo.png',
            'tagline': 'To inspire and nurture the human spirit',
            'cultural_data': {
                'colors': 'Green, White',
                'notes': 'Siren logo represents maritime coffee trading heritage. Green symbolizes growth and freshness.'
            },
            'founder_data': {
                'full_name': 'Howard Schultz',
                'birth_date': '1953-07-19'
            }
        },
        
        # Consumer Goods
        {
            'name': 'Unilever PLC',
            'category': 'Consumer Goods',
            'founding_date': '1929-09-02',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'UL',
            'market_cap': 130000000000,  # $130B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Unilever-Logo.png',
            'tagline': 'Making Sustainable Living Commonplace',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'U made of 25 icons representing diverse business areas. Blue represents trust and sustainability.'
            },
            'founder_data': {
                'full_name': 'William Lever',
                'birth_date': '1851-09-19'
            }
        },
        {
            'name': 'Procter & Gamble',
            'category': 'Consumer Goods',
            'founding_date': '1837-10-31',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PG',
            'market_cap': 380000000000,  # $380B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Procter-and-Gamble-Logo.png',
            'tagline': 'Touching Lives, Improving Life',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'P&G logo represents reliability and innovation in consumer goods. Blue signifies trust.'
            }
        },
        
        # Luxury & Fashion
        {
            'name': 'Hermès International',
            'category': 'Luxury Goods',
            'founding_date': '1837-06-01',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'HESAY',
            'market_cap': 220000000000,  # $220B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Hermes-Logo.png',
            'tagline': 'Leather Forever',
            'cultural_data': {
                'colors': 'Orange, Black',
                'notes': 'Orange boxes represent luxury and exclusivity. Heritage in leather craftsmanship and equestrian roots.'
            },
            'founder_data': {
                'full_name': 'Thierry Hermès',
                'birth_date': '1801-01-10'
            }
        },
        {
            'name': 'Chanel S.A.',
            'category': 'Luxury Goods',
            'founding_date': '1910-08-19',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': None,  # Private company
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Chanel-Logo.png',
            'tagline': 'Fashion Fades, Style is Eternal',
            'cultural_data': {
                'colors': 'Black, White, Gold',
                'notes': 'Double C logo represents founder\'s initials. Black and white embody timeless elegance.'
            },
            'founder_data': {
                'full_name': 'Gabrielle Chanel',
                'birth_date': '1883-08-19'
            }
        },
        
        # Telecommunications
        {
            'name': 'Verizon Communications',
            'category': 'Telecommunications',
            'founding_date': '1983-10-07',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'VZ',
            'market_cap': 170000000000,  # $170B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Verizon-Logo.png',
            'tagline': 'Can You Hear Me Now?',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Checkmark represents reliability and coverage. Red signifies energy and connectivity.'
            }
        },
        {
            'name': 'AT&T Inc.',
            'category': 'Telecommunications',
            'founding_date': '1983-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'T',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/ATT-Logo.png',
            'tagline': 'Rethink Possible',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Globe logo represents worldwide connectivity. Blue symbolizes reliability and communication.'
            }
        },
        
        # Energy & Oil
        {
            'name': 'ExxonMobil Corporation',
            'category': 'Energy',
            'founding_date': '1870-01-10',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'XOM',
            'market_cap': 450000000000,  # $450B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/ExxonMobil-Logo.png',
            'tagline': 'Taking on the World\'s Toughest Energy Challenges',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Double X represents strength and reliability in energy. Red and blue signify power and trust.'
            }
        },
        {
            'name': 'Shell plc',
            'category': 'Energy',
            'founding_date': '1907-02-20',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'SHEL',
            'market_cap': 200000000000,  # $200B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Shell-Logo.png',
            'tagline': 'Powering Progress',
            'cultural_data': {
                'colors': 'Red, Yellow',
                'notes': 'Shell represents the company\'s heritage in shell trading. Red and yellow evoke energy and warmth.'
            }
        },
        
        # Retail
        {
            'name': 'Walmart Inc.',
            'category': 'Retail',
            'founding_date': '1962-07-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WMT',
            'market_cap': 500000000000,  # $500B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Walmart-Logo.png',
            'tagline': 'Save Money. Live Better.',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Spark logo represents inspiration and ideas. Blue signifies trust, yellow represents optimism.'
            },
            'founder_data': {
                'full_name': 'Sam Walton',
                'birth_date': '1918-03-29'
            }
        },
        {
            'name': 'The Home Depot',
            'category': 'Retail',
            'founding_date': '1978-06-22',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'HD',
            'market_cap': 400000000000,  # $400B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Home-Depot-Logo.png',
            'tagline': 'How Doers Get More Done',
            'cultural_data': {
                'colors': 'Orange, White',
                'notes': 'Orange apron represents hands-on service and expertise. Orange evokes energy and construction.'
            }
        },
        
        # Pharmaceuticals
        {
            'name': 'Johnson & Johnson',
            'category': 'Pharmaceuticals',
            'founding_date': '1886-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'JNJ',
            'market_cap': 420000000000,  # $420B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Johnson-and-Johnson-Logo.png',
            'tagline': 'For All You Love',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Script logo represents heritage and trust in healthcare. Red signifies care and health.'
            }
        },
        {
            'name': 'Pfizer Inc.',
            'category': 'Pharmaceuticals',
            'founding_date': '1849-05-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PFE',
            'market_cap': 280000000000,  # $280B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Pfizer-Logo.png',
            'tagline': 'Breakthroughs that Change Patients\' Lives',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'DNA helix in logo represents scientific innovation. Blue symbolizes trust and medical expertise.'
            }
        }
    ]


def add_extended_brands():
    """Add extended brand data to the database."""
    researcher = BrandResearcher()
    extended_brands = get_extended_brands_data()
    
    print(f"Adding {len(extended_brands)} additional global brands...")
    
    start_id = 21  # Continue from existing brands
    for i, brand_data in enumerate(extended_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nExtended database populated successfully!")
    
    # Generate updated analysis
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    total_brands = len(analyzer.get_all_brands())
    print(f"Total brands in database: {total_brands}")


if __name__ == "__main__":
    add_extended_brands()