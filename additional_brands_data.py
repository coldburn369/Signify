#!/usr/bin/env python3
"""
Additional Brands Data Collection
Expanding the database with more diverse global brands across new categories.
"""

from brand_research import BrandResearcher


def get_additional_brands_data():
    """Return additional diverse global brands data across new categories."""
    return [
        # Entertainment & Media
        {
            'name': 'The Walt Disney Company',
            'category': 'Entertainment',
            'founding_date': '1923-10-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'DIS',
            'market_cap': 190000000000,  # $190B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/11/Disney-Logo.png',
            'tagline': 'The Most Magical Place on Earth',
            'cultural_data': {
                'colors': 'Blue, White, Red',
                'notes': 'Mickey Mouse head represents joy and imagination. Castle logo symbolizes dreams and magic.'
            },
            'founder_data': {
                'full_name': 'Walt Disney',
                'birth_date': '1901-12-05'
            }
        },
        {
            'name': 'Netflix Inc.',
            'category': 'Entertainment',
            'founding_date': '1997-08-29',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'NFLX',
            'market_cap': 160000000000,  # $160B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Netflix-Logo.png',
            'tagline': 'See What\'s Next',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Red represents excitement and entertainment. Black background emphasizes premium content.'
            },
            'founder_data': {
                'full_name': 'Reed Hastings',
                'birth_date': '1960-10-08'
            }
        },
        {
            'name': 'Spotify Technology',
            'category': 'Entertainment',
            'founding_date': '2006-04-23',
            'country': 'Sweden',
            'parent_company': None,
            'stock_ticker': 'SPOT',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Spotify-Logo.png',
            'tagline': 'Music for Everyone',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'Green represents growth and energy. Sound waves in logo symbolize music streaming.'
            },
            'founder_data': {
                'full_name': 'Daniel Ek',
                'birth_date': '1983-02-21'
            }
        },

        # Furniture & Home
        {
            'name': 'IKEA',
            'category': 'Furniture',
            'founding_date': '1943-07-28',
            'country': 'Sweden',
            'parent_company': None,
            'stock_ticker': None,  # Private company
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/IKEA-Logo.png',
            'tagline': 'Wunderful Everyday',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Swedish flag colors represent heritage. Blue signifies trust, yellow represents happiness and optimism.'
            },
            'founder_data': {
                'full_name': 'Ingvar Kamprad',
                'birth_date': '1926-03-30'
            }
        },

        # Logistics & Shipping
        {
            'name': 'FedEx Corporation',
            'category': 'Logistics',
            'founding_date': '1971-06-18',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'FDX',
            'market_cap': 65000000000,  # $65B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/FedEx-Logo.png',
            'tagline': 'When it Absolutely, Positively has to be There Overnight',
            'cultural_data': {
                'colors': 'Purple, Orange',
                'notes': 'Purple represents reliability, orange represents speed. Hidden arrow between E and X symbolizes forward movement.'
            },
            'founder_data': {
                'full_name': 'Frederick W. Smith',
                'birth_date': '1944-08-11'
            }
        },
        {
            'name': 'United Parcel Service',
            'category': 'Logistics',
            'founding_date': '1907-08-28',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'UPS',
            'market_cap': 110000000000,  # $110B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/UPS-Logo.png',
            'tagline': 'What Can Brown Do for You?',
            'cultural_data': {
                'colors': 'Brown, Gold',
                'notes': 'Brown represents reliability and earthiness. Shield logo symbolizes protection and trust.'
            },
            'founder_data': {
                'full_name': 'James Casey',
                'birth_date': '1888-03-29'
            }
        },

        # Aerospace & Defense
        {
            'name': 'Boeing Company',
            'category': 'Aerospace',
            'founding_date': '1916-07-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'BA',
            'market_cap': 130000000000,  # $130B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Boeing-Logo.png',
            'tagline': 'Forever New Frontiers',
            'cultural_data': {
                'colors': 'Blue, Grey',
                'notes': 'Blue represents sky and reliability. Modern design reflects aerospace innovation.'
            },
            'founder_data': {
                'full_name': 'William Boeing',
                'birth_date': '1881-10-01'
            }
        },
        {
            'name': 'Airbus SE',
            'category': 'Aerospace',
            'founding_date': '1970-12-18',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'EADSY',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Airbus-Logo.png',
            'tagline': 'We Make It Fly',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Stylized A represents aerospace excellence. Blue symbolizes sky and innovation.'
            }
        },

        # Fashion & Luxury (European)
        {
            'name': 'Gucci',
            'category': 'Luxury Goods',
            'founding_date': '1921-01-01',
            'country': 'Italy',
            'parent_company': 'Kering',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Gucci-Logo.png',
            'tagline': 'Quality is Remembered Long After Price is Forgotten',
            'cultural_data': {
                'colors': 'Green, Red',
                'notes': 'Italian flag colors represent heritage. Double G logo represents founder Guccio Gucci.'
            },
            'founder_data': {
                'full_name': 'Guccio Gucci',
                'birth_date': '1881-03-26'
            }
        },
        {
            'name': 'Prada S.p.A.',
            'category': 'Luxury Goods',
            'founding_date': '1913-01-01',
            'country': 'Italy',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Prada-Logo.png',
            'tagline': 'Made to Measure',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Minimalist design represents sophistication. Triangle logo symbolizes strength and style.'
            },
            'founder_data': {
                'full_name': 'Mario Prada',
                'birth_date': '1883-05-12'
            }
        },

        # Beverages (Alcoholic)
        {
            'name': 'Heineken N.V.',
            'category': 'Alcoholic Beverages',
            'founding_date': '1864-02-15',
            'country': 'Netherlands',
            'parent_company': None,
            'stock_ticker': 'HEINY',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Heineken-Logo.png',
            'tagline': 'Open Your World',
            'cultural_data': {
                'colors': 'Green, Red, Silver',
                'notes': 'Green represents freshness and nature. Red star is symbol of quality brewing.'
            },
            'founder_data': {
                'full_name': 'Gerard Adriaan Heineken',
                'birth_date': '1841-02-09'
            }
        },
        {
            'name': 'Anheuser-Busch InBev',
            'category': 'Alcoholic Beverages',
            'founding_date': '1852-01-01',
            'country': 'Belgium',
            'parent_company': None,
            'stock_ticker': 'BUD',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Anheuser-Busch-Logo.png',
            'tagline': 'King of Beers',
            'cultural_data': {
                'colors': 'Red, White, Blue',
                'notes': 'Eagle logo represents strength and American heritage. Red, white, blue evoke patriotism.'
            }
        },

        # Semiconductors & Electronics
        {
            'name': 'Intel Corporation',
            'category': 'Semiconductors',
            'founding_date': '1968-07-18',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'INTC',
            'market_cap': 200000000000,  # $200B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Intel-Logo.png',
            'tagline': 'Intel Inside',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents technology and reliability. Dropped "e" in logo represents innovation.'
            },
            'founder_data': {
                'full_name': 'Gordon Moore',
                'birth_date': '1929-01-03'
            }
        },
        {
            'name': 'NVIDIA Corporation',
            'category': 'Semiconductors',
            'founding_date': '1993-04-05',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'NVDA',
            'market_cap': 1800000000000,  # $1.8T approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/NVIDIA-Logo.png',
            'tagline': 'The Way It\'s Meant to be Played',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'Green eye represents vision and graphics processing. Name combines "invidia" (envy) and "video".'
            },
            'founder_data': {
                'full_name': 'Jensen Huang',
                'birth_date': '1963-02-17'
            }
        },

        # Telecommunications (Asian)
        {
            'name': 'Huawei Technologies',
            'category': 'Telecommunications',
            'founding_date': '1987-09-15',
            'country': 'China',
            'parent_company': None,
            'stock_ticker': None,  # Private company
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Huawei-Logo.png',
            'tagline': 'Make it Possible',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Red flower petals represent blooming and growth. Huawei means "splendid act" in Chinese.'
            },
            'founder_data': {
                'full_name': 'Ren Zhengfei',
                'birth_date': '1944-10-25'
            }
        },

        # Airlines (International)
        {
            'name': 'Emirates Airline',
            'category': 'Airlines',
            'founding_date': '1985-03-25',
            'country': 'United Arab Emirates',
            'parent_company': None,
            'stock_ticker': None,  # Government-owned
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Emirates-Logo.png',
            'tagline': 'Fly Better',
            'cultural_data': {
                'colors': 'Red, Gold',
                'notes': 'Arabic calligraphy represents cultural heritage. Red and gold symbolize luxury and hospitality.'
            }
        },
        {
            'name': 'Lufthansa Group',
            'category': 'Airlines',
            'founding_date': '1955-01-06',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'DLAKY',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Lufthansa-Logo.png',
            'tagline': 'Say Yes to the World',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Crane logo represents grace and flight. Blue represents sky, yellow represents sun.'
            }
        },

        # Hotels & Hospitality
        {
            'name': 'Marriott International',
            'category': 'Hospitality',
            'founding_date': '1927-05-20',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MAR',
            'market_cap': 70000000000,  # $70B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Marriott-Logo.png',
            'tagline': 'Travel Brilliantly',
            'cultural_data': {
                'colors': 'Red, Gold',
                'notes': 'Red represents warmth and hospitality. M logo signifies premium service and luxury.'
            },
            'founder_data': {
                'full_name': 'J.W. Marriott Sr.',
                'birth_date': '1900-09-17'
            }
        },
        {
            'name': 'Hilton Worldwide',
            'category': 'Hospitality',
            'founding_date': '1919-05-31',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'HLT',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Hilton-Logo.png',
            'tagline': 'Travel Should Take You Places',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Blue represents trust and luxury. Clean design reflects modern hospitality standards.'
            },
            'founder_data': {
                'full_name': 'Conrad Hilton',
                'birth_date': '1887-12-25'
            }
        },

        # Cosmetics & Beauty
        {
            'name': 'L\'Oréal S.A.',
            'category': 'Cosmetics',
            'founding_date': '1909-07-30',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'LRLCY',
            'market_cap': 220000000000,  # $220B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LOreal-Logo.png',
            'tagline': 'Because You\'re Worth It',
            'cultural_data': {
                'colors': 'Black, White, Gold',
                'notes': 'Elegant typography represents beauty and sophistication. French heritage in luxury cosmetics.'
            },
            'founder_data': {
                'full_name': 'Eugène Schueller',
                'birth_date': '1881-03-20'
            }
        },

        # Gaming & Entertainment Technology
        {
            'name': 'Electronic Arts',
            'category': 'Gaming',
            'founding_date': '1982-05-27',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'EA',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/06/Electronic-Arts-Logo.png',
            'tagline': 'EA Sports - It\'s in the Game',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Bold typography represents gaming excitement. Red symbolizes energy and competition.'
            }
        },

        # Insurance
        {
            'name': 'Berkshire Hathaway',
            'category': 'Insurance',
            'founding_date': '1839-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'BRK.A',
            'market_cap': 900000000000,  # $900B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/05/Berkshire-Hathaway-Logo.png',
            'tagline': 'Value Investing',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Conservative design represents stability and long-term investment philosophy.'
            },
            'founder_data': {
                'full_name': 'Warren Buffett',
                'birth_date': '1930-08-30'
            }
        }
    ]


def add_additional_brands():
    """Add additional brand data to the database."""
    researcher = BrandResearcher()
    additional_brands = get_additional_brands_data()
    
    print(f"Adding {len(additional_brands)} additional global brands...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(additional_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nAdditional brands added successfully!")
    
    # Generate updated statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    new_categories = set(brand['category'] for brand in updated_brands)
    
    print(f"Updated database statistics:")
    print(f"  Total brands: {total_brands}")
    print(f"  Total categories: {len(new_categories)}")
    print(f"  New categories added: {len(new_categories) - 15}")  # Previous count was 15


if __name__ == "__main__":
    add_additional_brands()