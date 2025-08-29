#!/usr/bin/env python3
"""
Comprehensive Brand Data Collection
Hand-curated database of major global brands with verified information.
"""

from brand_research import BrandResearcher
from datetime import datetime


def get_major_brands_data():
    """Return comprehensive data for major global brands."""
    return [
        # Technology Companies
        {
            'name': 'Apple Inc.',
            'category': 'Technology',
            'founding_date': '1976-04-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'AAPL',
            'market_cap': 3000000000000,  # $3T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Apple-Logo.png',
            'tagline': 'Think Different',
            'cultural_data': {
                'colors': 'White, Black, Silver',
                'notes': 'Bitten apple symbolizes knowledge and innovation. Minimalist design philosophy.'
            },
            'founder_data': {
                'full_name': 'Steve Jobs',
                'birth_date': '1955-02-24'
            }
        },
        {
            'name': 'Microsoft Corporation',
            'category': 'Technology',
            'founding_date': '1975-04-04',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MSFT',
            'market_cap': 2800000000000,  # $2.8T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Microsoft-Logo.png',
            'tagline': 'Be What\'s Next',
            'cultural_data': {
                'colors': 'Blue, Red, Green, Yellow',
                'notes': 'Four-square logo represents diversity and Windows OS. Blue symbolizes trust and reliability.'
            },
            'founder_data': {
                'full_name': 'Bill Gates',
                'birth_date': '1955-10-28'
            }
        },
        {
            'name': 'Google LLC',
            'category': 'Technology',
            'founding_date': '1998-09-04',
            'country': 'United States',
            'parent_company': 'Alphabet Inc.',
            'stock_ticker': 'GOOGL',
            'market_cap': 1700000000000,  # $1.7T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Google-Logo.png',
            'tagline': 'Don\'t be evil',
            'cultural_data': {
                'colors': 'Blue, Red, Yellow, Green',
                'notes': 'Playful colors represent creativity and accessibility. Name derived from googol (10^100).'
            },
            'founder_data': {
                'full_name': 'Larry Page',
                'birth_date': '1973-03-26'
            }
        },
        {
            'name': 'Amazon.com Inc.',
            'category': 'Technology',
            'founding_date': '1994-07-05',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'AMZN',
            'market_cap': 1500000000000,  # $1.5T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Amazon-Logo.png',
            'tagline': 'Earth\'s Most Customer-Centric Company',
            'cultural_data': {
                'colors': 'Orange, Black',
                'notes': 'Arrow from A to Z represents comprehensive selection. Smile arrow suggests customer satisfaction.'
            },
            'founder_data': {
                'full_name': 'Jeff Bezos',
                'birth_date': '1964-01-12'
            }
        },
        {
            'name': 'Meta Platforms Inc.',
            'category': 'Technology',
            'founding_date': '2004-02-04',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'META',
            'market_cap': 800000000000,  # $800B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2021/11/Meta-Logo.png',
            'tagline': 'Move Fast and Break Things',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Infinity symbol represents metaverse and endless connections. Blue evokes trust and communication.'
            },
            'founder_data': {
                'full_name': 'Mark Zuckerberg',
                'birth_date': '1984-05-14'
            }
        },
        
        # Automotive Companies
        {
            'name': 'Toyota Motor Corporation',
            'category': 'Automotive',
            'founding_date': '1937-08-28',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'TM',
            'market_cap': 250000000000,  # $250B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Toyota-Logo.png',
            'tagline': 'Let\'s Go Places',
            'cultural_data': {
                'colors': 'Red, Silver',
                'notes': 'Three overlapping ellipses represent customer heart, product heart, and technological progress.'
            },
            'founder_data': {
                'full_name': 'Kiichiro Toyoda',
                'birth_date': '1894-06-11'
            }
        },
        {
            'name': 'Tesla Inc.',
            'category': 'Automotive',
            'founding_date': '2003-07-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'TSLA',
            'market_cap': 800000000000,  # $800B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Tesla-Logo.png',
            'tagline': 'Accelerating the World\'s Transition to Sustainable Energy',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'T-shaped logo represents cross-section of electric motor. Named after Nikola Tesla.'
            },
            'founder_data': {
                'full_name': 'Elon Musk',
                'birth_date': '1971-06-28'
            }
        },
        {
            'name': 'Volkswagen AG',
            'category': 'Automotive',
            'founding_date': '1937-05-28',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'VWAGY',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Volkswagen-Logo.png',
            'tagline': 'Das Auto (The Car)',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'VW monogram in circle represents people\'s car. Founded as Nazi project, later democratized.'
            }
        },
        {
            'name': 'BMW AG',
            'category': 'Automotive',
            'founding_date': '1916-03-07',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'BMWYY',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/BMW-Logo.png',
            'tagline': 'The Ultimate Driving Machine',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Roundel represents rotating aircraft propeller (aviation heritage). Blue/white from Bavarian flag.'
            },
            'founder_data': {
                'full_name': 'Karl Rapp',
                'birth_date': '1882-09-24'
            }
        },
        
        # Fashion & Luxury
        {
            'name': 'LVMH',
            'category': 'Luxury Goods',
            'founding_date': '1987-06-15',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'LVMUY',
            'market_cap': 400000000000,  # $400B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LVMH-Logo.png',
            'tagline': 'The Art of Living',
            'cultural_data': {
                'colors': 'Gold, Black',
                'notes': 'Luxury conglomerate. Gold represents luxury and exclusivity.'
            },
            'founder_data': {
                'full_name': 'Bernard Arnault',
                'birth_date': '1949-03-05'
            }
        },
        {
            'name': 'Nike Inc.',
            'category': 'Apparel',
            'founding_date': '1971-05-30',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'NKE',
            'market_cap': 170000000000,  # $170B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Nike-Logo.png',
            'tagline': 'Just Do It',
            'cultural_data': {
                'colors': 'Black, White, Orange',
                'notes': 'Swoosh represents motion and speed. Named after Greek goddess of victory.'
            },
            'founder_data': {
                'full_name': 'Phil Knight',
                'birth_date': '1938-02-24'
            }
        },
        {
            'name': 'Adidas AG',
            'category': 'Apparel',
            'founding_date': '1949-08-18',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'ADDYY',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Adidas-Logo.png',
            'tagline': 'Impossible is Nothing',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Three stripes represent mountain (challenges to overcome). Named after founder Adolf Dassler.'
            },
            'founder_data': {
                'full_name': 'Adolf Dassler',
                'birth_date': '1900-11-03'
            }
        },
        
        # Financial Services
        {
            'name': 'JPMorgan Chase & Co.',
            'category': 'Banking',
            'founding_date': '1799-09-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'JPM',
            'market_cap': 450000000000,  # $450B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/JPMorgan-Chase-Logo.png',
            'tagline': 'The Right Relationship is Everything',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue octagon represents strength and stability. Merger of JP Morgan and Chase Manhattan.'
            }
        },
        {
            'name': 'Bank of America Corporation',
            'category': 'Banking',
            'founding_date': '1904-10-17',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'BAC',
            'market_cap': 320000000000,  # $320B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Bank-of-America-Logo.png',
            'tagline': 'Life\'s Better When We\'re Connected',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Flag motif represents American values. Red symbolizes strength, blue trust.'
            }
        },
        
        # Beverages
        {
            'name': 'The Coca-Cola Company',
            'category': 'Beverages',
            'founding_date': '1892-01-29',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'KO',
            'market_cap': 270000000000,  # $270B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Coca-Cola-Logo.png',
            'tagline': 'Taste the Feeling',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Spencerian script represents heritage and authenticity. Red evokes energy and passion.'
            },
            'founder_data': {
                'full_name': 'John Stith Pemberton',
                'birth_date': '1831-07-08'
            }
        },
        {
            'name': 'PepsiCo Inc.',
            'category': 'Beverages',
            'founding_date': '1898-08-28',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PEP',
            'market_cap': 230000000000,  # $230B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Pepsi-Logo.png',
            'tagline': 'For the Love of It',
            'cultural_data': {
                'colors': 'Blue, Red, White',
                'notes': 'Circular logo with wave represents refreshment. Patriotic colors reference American heritage.'
            },
            'founder_data': {
                'full_name': 'Caleb Bradham',
                'birth_date': '1867-05-27'
            }
        },
        
        # Airlines
        {
            'name': 'Delta Air Lines Inc.',
            'category': 'Airlines',
            'founding_date': '1924-03-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'DAL',
            'market_cap': 28000000000,  # $28B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Delta-Logo.png',
            'tagline': 'Keep Climbing',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Triangle widget represents delta symbol (change) and aircraft nose. Blue represents sky.'
            }
        },
        {
            'name': 'Southwest Airlines Co.',
            'category': 'Airlines',
            'founding_date': '1971-06-18',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'LUV',
            'market_cap': 18000000000,  # $18B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Southwest-Airlines-Logo.png',
            'tagline': 'Low fares. Nothing to hide.',
            'cultural_data': {
                'colors': 'Blue, Orange, Red',
                'notes': 'Heart logo represents love and care. Ticker LUV references Dallas Love Field airport.'
            }
        },
        
        # Luxury & Watches
        {
            'name': 'Rolex SA',
            'category': 'Luxury Goods',
            'founding_date': '1905-07-02',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': None,  # Private company
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Rolex-Logo.png',
            'tagline': 'A Crown for Every Achievement',
            'cultural_data': {
                'colors': 'Gold, Green',
                'notes': 'Crown logo represents precision and excellence. Green represents prestige and luxury.'
            },
            'founder_data': {
                'full_name': 'Hans Wilsdorf',
                'birth_date': '1881-03-22'
            }
        },
        
        # Motorcycles
        {
            'name': 'Harley-Davidson Inc.',
            'category': 'Motorcycles',
            'founding_date': '1903-08-28',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'HOG',
            'market_cap': 5000000000,  # $5B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Harley-Davidson-Logo.png',
            'tagline': 'Live Your Legend',
            'cultural_data': {
                'colors': 'Orange, Black',
                'notes': 'Bar and shield logo represents strength and heritage. Orange represents energy and rebellion.'
            },
            'founder_data': {
                'full_name': 'William Harley',
                'birth_date': '1880-12-29'
            }
        }
    ]


def main():
    """Load all brand data into the database."""
    researcher = BrandResearcher()
    brands_data = get_major_brands_data()
    
    print(f"Processing {len(brands_data)} major global brands...")
    
    for i, brand_data in enumerate(brands_data, 1):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nDatabase populated successfully!")
    print(f"Database location: {researcher.db.db_path}")


if __name__ == "__main__":
    main()