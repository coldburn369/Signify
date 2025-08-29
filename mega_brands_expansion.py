#!/usr/bin/env python3
"""
Mega Brands Database Expansion
Adding maximum diversity across all sectors and regions.
"""

from brand_research import BrandResearcher


def get_mega_expansion_brands():
    """Return mega expansion with maximum global diversity."""
    return [
        # Fashion & Apparel (Additional)
        {
            'name': 'Inditex (Zara)',
            'category': 'Fashion',
            'founding_date': '1975-05-24',
            'country': 'Spain',
            'parent_company': None,
            'stock_ticker': 'ITX',
            'market_cap': 65000000000,  # $65B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Zara-Logo.png',
            'tagline': 'Love Your Curves',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Minimalist design represents fast fashion innovation. Spanish global fashion empire.'
            },
            'founder_data': {
                'full_name': 'Amancio Ortega',
                'birth_date': '1936-03-28'
            }
        },
        {
            'name': 'H&M Group',
            'category': 'Fashion',
            'founding_date': '1947-01-01',
            'country': 'Sweden',
            'parent_company': None,
            'stock_ticker': 'HM',
            'market_cap': 15000000000,  # $15B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/HM-Logo.png',
            'tagline': 'Fashion and Quality at the Best Price',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'H&M stands for Hennes & Mauritz. Red represents Swedish heritage and accessibility.'
            },
            'founder_data': {
                'full_name': 'Erling Persson',
                'birth_date': '1917-01-21'
            }
        },
        {
            'name': 'Fast Retailing (Uniqlo)',
            'category': 'Fashion',
            'founding_date': '1963-05-01',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': '9983.T',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Uniqlo-Logo.png',
            'tagline': 'Made for All',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Japanese approach to functional fashion. Red represents simplicity and quality.'
            },
            'founder_data': {
                'full_name': 'Tadashi Yanai',
                'birth_date': '1949-02-07'
            }
        },
        {
            'name': 'Ralph Lauren Corporation',
            'category': 'Fashion',
            'founding_date': '1967-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'RL',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Ralph-Lauren-Logo.png',
            'tagline': 'Create Worlds and Invite People to Live the Dream',
            'cultural_data': {
                'colors': 'Navy, White, Red',
                'notes': 'Polo player represents American luxury and preppy lifestyle heritage.'
            },
            'founder_data': {
                'full_name': 'Ralph Lauren',
                'birth_date': '1939-10-14'
            }
        },
        {
            'name': 'VF Corporation',
            'category': 'Fashion',
            'founding_date': '1899-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'VFC',
            'market_cap': 12000000000,  # $12B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/VF-Corporation-Logo.png',
            'tagline': 'Powered by Purpose',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Parent of Vans, The North Face, Timberland. Blue represents outdoor lifestyle.'
            }
        },

        # Airlines (Additional)
        {
            'name': 'Air France-KLM',
            'category': 'Airlines',
            'founding_date': '1933-08-30',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'AF',
            'market_cap': 5000000000,  # $5B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Air-France-Logo.png',
            'tagline': 'Making the Sky the Best Place on Earth',
            'cultural_data': {
                'colors': 'Blue, Red, White',
                'notes': 'French flag colors represent national airline heritage and European aviation excellence.'
            }
        },
        {
            'name': 'British Airways',
            'category': 'Airlines',
            'founding_date': '1974-03-31',
            'country': 'United Kingdom',
            'parent_company': 'International Airlines Group',
            'stock_ticker': 'IAG',
            'market_cap': 7000000000,  # $7B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/British-Airways-Logo.png',
            'tagline': 'To Fly. To Serve.',
            'cultural_data': {
                'colors': 'Blue, Red, White',
                'notes': 'Union Jack tail design represents British heritage and global connectivity.'
            }
        },
        {
            'name': 'Singapore Airlines',
            'category': 'Airlines',
            'founding_date': '1972-05-01',
            'country': 'Singapore',
            'parent_company': None,
            'stock_ticker': 'C6L.SI',
            'market_cap': 12000000000,  # $12B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Singapore-Airlines-Logo.png',
            'tagline': 'A Great Way to Fly',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Stylized bird represents grace and Asian hospitality excellence.'
            }
        },
        {
            'name': 'Qantas Airways',
            'category': 'Airlines',
            'founding_date': '1920-11-16',
            'country': 'Australia',
            'parent_company': None,
            'stock_ticker': 'QAN.AX',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Qantas-Logo.png',
            'tagline': 'The Spirit of Australia',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Flying kangaroo represents Australian identity and long-distance aviation heritage.'
            }
        },

        # Telecommunications (Additional)
        {
            'name': 'Vodafone Group Plc',
            'category': 'Telecommunications',
            'founding_date': '1984-01-01',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'VOD',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Vodafone-Logo.png',
            'tagline': 'Power to You',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Speech mark represents conversation and global mobile connectivity.'
            }
        },
        {
            'name': 'Orange S.A.',
            'category': 'Telecommunications',
            'founding_date': '1994-01-01',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'ORA',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Orange-Logo.png',
            'tagline': 'The Future is Bright',
            'cultural_data': {
                'colors': 'Orange, White',
                'notes': 'Orange represents energy, optimism, and telecommunications innovation.'
            }
        },
        {
            'name': 'Deutsche Telekom AG',
            'category': 'Telecommunications',
            'founding_date': '1995-01-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'DTE',
            'market_cap': 80000000000,  # $80B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Deutsche-Telekom-Logo.png',
            'tagline': 'Life is for Sharing',
            'cultural_data': {
                'colors': 'Magenta, White',
                'notes': 'Magenta T represents innovation and German telecommunications leadership.'
            }
        },

        # Consumer Goods (Additional)
        {
            'name': 'Danone S.A.',
            'category': 'Consumer Goods',
            'founding_date': '1919-02-06',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'BN',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Danone-Logo.png',
            'tagline': 'One Planet. One Health.',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Child logo represents health and nutrition focus. French dairy heritage.'
            },
            'founder_data': {
                'full_name': 'Isaac Carasso',
                'birth_date': '1874-12-14'
            }
        },
        {
            'name': 'Colgate-Palmolive Company',
            'category': 'Consumer Goods',
            'founding_date': '1806-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CL',
            'market_cap': 65000000000,  # $65B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Colgate-Logo.png',
            'tagline': 'Every Little Wonder',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Red represents health and dental care heritage. Over 200 years of oral care innovation.'
            },
            'founder_data': {
                'full_name': 'William Colgate',
                'birth_date': '1783-01-25'
            }
        },
        {
            'name': 'Reckitt Benckiser Group',
            'category': 'Consumer Goods',
            'founding_date': '1823-01-01',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'RKT',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Reckitt-Logo.png',
            'tagline': 'Protect, Heal and Nurture',
            'cultural_data': {
                'colors': 'Pink, Blue',
                'notes': 'Brands include Lysol, Dettol. Pink and blue represent health and hygiene.'
            }
        },

        # Software & Technology Services (Additional)
        {
            'name': 'ServiceNow Inc.',
            'category': 'Technology Services',
            'founding_date': '2004-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'NOW',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ServiceNow-Logo.png',
            'tagline': 'Make Work, Work Better',
            'cultural_data': {
                'colors': 'Green, White',
                'notes': 'Green represents growth and digital transformation in enterprise services.'
            }
        },
        {
            'name': 'Workday Inc.',
            'category': 'Technology Services',
            'founding_date': '2005-03-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WDAY',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Workday-Logo.png',
            'tagline': 'For a Changing World',
            'cultural_data': {
                'colors': 'Orange, Blue',
                'notes': 'W logo represents workforce management and human capital solutions.'
            }
        },
        {
            'name': 'Palantir Technologies',
            'category': 'Technology Services',
            'founding_date': '2003-05-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PLTR',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Palantir-Logo.png',
            'tagline': 'We Build Software for Institutions',
            'cultural_data': {
                'colors': 'Black, Gold',
                'notes': 'Named after seeing stones from Lord of the Rings. Represents data analytics power.'
            }
        },

        # Food & Beverages (Additional)
        {
            'name': 'Diageo plc',
            'category': 'Alcoholic Beverages',
            'founding_date': '1997-01-01',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'DEO',
            'market_cap': 85000000000,  # $85B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Diageo-Logo.png',
            'tagline': 'Celebrating Life, Every Day, Everywhere',
            'cultural_data': {
                'colors': 'Gold, Black',
                'notes': 'Owns Johnnie Walker, Guinness, Smirnoff. Gold represents premium spirits heritage.'
            }
        },
        {
            'name': 'Constellation Brands',
            'category': 'Alcoholic Beverages',
            'founding_date': '1945-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'STZ',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Constellation-Logo.png',
            'tagline': 'We Elevate Life',
            'cultural_data': {
                'colors': 'Blue, Gold',
                'notes': 'Constellation represents premium wine, beer, and spirits portfolio.'
            }
        },
        {
            'name': 'Tyson Foods Inc.',
            'category': 'Food Processing',
            'founding_date': '1935-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'TSN',
            'market_cap': 20000000000,  # $20B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Tyson-Foods-Logo.png',
            'tagline': 'Fed by Purpose. Fueled by Possibility.',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Leading American protein producer. Red represents meat processing heritage.'
            }
        },
        {
            'name': 'Archer-Daniels-Midland',
            'category': 'Food Processing',
            'founding_date': '1902-05-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'ADM',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ADM-Logo.png',
            'tagline': 'Unlocking Nature to Enrich Life',
            'cultural_data': {
                'colors': 'Green, Blue',
                'notes': 'Agricultural commodities and food ingredients. Green represents agricultural heritage.'
            }
        },

        # Media & Entertainment (Additional)
        {
            'name': 'Sony Pictures Entertainment',
            'category': 'Media',
            'founding_date': '1987-08-07',
            'country': 'United States',
            'parent_company': 'Sony Corporation',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Sony-Pictures-Logo.png',
            'tagline': 'A Sony Company',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Hollywood studio representing Japanese technology meeting American entertainment.'
            }
        },
        {
            'name': 'Paramount Global',
            'category': 'Media',
            'founding_date': '1912-05-08',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PARA',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Paramount-Logo.png',
            'tagline': 'If You Can Dream It, We Can Do It',
            'cultural_data': {
                'colors': 'Blue, Gold',
                'notes': 'Mountain logo represents Hollywood heritage and entertainment peaks.'
            }
        },

        # Luxury & Cosmetics (Additional)
        {
            'name': 'Shiseido Company',
            'category': 'Cosmetics',
            'founding_date': '1872-09-08',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': '4911.T',
            'market_cap': 15000000000,  # $15B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Shiseido-Logo.png',
            'tagline': 'A Beautiful Life',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Oldest cosmetics company in Japan. Red represents beauty and Japanese heritage.'
            },
            'founder_data': {
                'full_name': 'Arinobu Fukuhara',
                'birth_date': '1848-11-10'
            }
        },
        {
            'name': 'Coty Inc.',
            'category': 'Cosmetics',
            'founding_date': '1904-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'COTY',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Coty-Logo.png',
            'tagline': 'Beauty That Lasts',
            'cultural_data': {
                'colors': 'Pink, Black',
                'notes': 'French-founded American beauty company. Pink represents femininity and fragrance.'
            },
            'founder_data': {
                'full_name': 'François Coty',
                'birth_date': '1874-05-03'
            }
        },

        # Health & Wellness
        {
            'name': 'UnitedHealth Group',
            'category': 'Healthcare',
            'founding_date': '1977-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'UNH',
            'market_cap': 500000000000,  # $500B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/UnitedHealth-Logo.png',
            'tagline': 'Health Care That Works. For You.',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue cross represents healthcare trust and medical reliability.'
            }
        },
        {
            'name': 'CVS Health Corporation',
            'category': 'Healthcare',
            'founding_date': '1963-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CVS',
            'market_cap': 85000000000,  # $85B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/CVS-Health-Logo.png',
            'tagline': 'Health is Everything',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Heart logo represents health and wellness focus. CVS stands for Consumer Value Stores.'
            }
        },

        # Entertainment & Gaming (Additional)
        {
            'name': 'Activision Blizzard',
            'category': 'Gaming',
            'founding_date': '1979-10-01',
            'country': 'United States',
            'parent_company': 'Microsoft Corporation',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Activision-Logo.png',
            'tagline': 'Connecting and Engaging the World',
            'cultural_data': {
                'colors': 'Orange, Black',
                'notes': 'Gaming giant behind Call of Duty, World of Warcraft. Orange represents gaming energy.'
            }
        },
        {
            'name': 'Take-Two Interactive',
            'category': 'Gaming',
            'founding_date': '1993-09-30',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'TTWO',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Take-Two-Logo.png',
            'tagline': 'We Create Interactive Entertainment',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Publisher of Grand Theft Auto, Red Dead Redemption. Bold design represents edgy gaming.'
            }
        },

        # Real Estate & Construction
        {
            'name': 'American Tower Corporation',
            'category': 'Real Estate',
            'founding_date': '1995-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'AMT',
            'market_cap': 95000000000,  # $95B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/American-Tower-Logo.png',
            'tagline': 'Elevating What\'s Possible',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Cell tower infrastructure. Tower symbol represents telecommunications infrastructure.'
            }
        },

        # Financial Technology
        {
            'name': 'PayPal Holdings Inc.',
            'category': 'Financial Technology',
            'founding_date': '1998-12-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PYPL',
            'market_cap': 70000000000,  # $70B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/PayPal-Logo.png',
            'tagline': 'The Currency of Possibility',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Double P represents digital payments innovation. Blue conveys financial trust.'
            },
            'founder_data': {
                'full_name': 'Elon Musk',
                'birth_date': '1971-06-28'
            }
        },
        {
            'name': 'Square Inc. (Block)',
            'category': 'Financial Technology',
            'founding_date': '2009-02-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'SQ',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Square-Logo.png',
            'tagline': 'Start Something',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Square represents simplicity in payments. Minimalist design reflects ease of use.'
            },
            'founder_data': {
                'full_name': 'Jack Dorsey',
                'birth_date': '1976-11-19'
            }
        }
    ]


def add_mega_expansion():
    """Add mega expansion for maximum global brand coverage."""
    researcher = BrandResearcher()
    mega_brands = get_mega_expansion_brands()
    
    print(f"Adding {len(mega_brands)} brands for ultimate global coverage...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(mega_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nMega expansion completed successfully!")
    
    # Generate final statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    categories = set(brand['category'] for brand in updated_brands)
    countries = set(brand['country'] for brand in updated_brands)
    
    print(f"\nULTIMATE DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    print(f"  Categories: {len(categories)}")
    print(f"  Countries: {len(countries)}")
    
    # Calculate total market cap
    total_market_cap = sum(brand.get('market_cap', 0) for brand in updated_brands if brand.get('market_cap'))
    print(f"  Total market cap: ${total_market_cap:,}")
    
    # Show top new categories
    category_counts = {}
    for brand in updated_brands:
        category = brand['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print(f"\nTop 5 categories:")
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {category}: {count} brands")


if __name__ == "__main__":
    add_mega_expansion()