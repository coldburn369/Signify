#!/usr/bin/env python3
"""
Comprehensive Categories Expansion
Adding major global brands across underrepresented categories for better balance.
"""

from brand_research import BrandResearcher


def get_comprehensive_expansion():
    """Return major global brands across underrepresented categories."""
    return [
        # BEVERAGES EXPANSION (Currently 2 brands)
        {
            'name': 'The Coca-Cola Company',
            'category': 'Beverages',
            'founding_date': '1886-05-08',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'KO',
            'market_cap': 260000000000,  # $260B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Coca-Cola-Logo.png',
            'tagline': 'Taste the Feeling',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Iconic red represents energy and happiness. Global symbol of American consumer culture.'
            },
            'founder_data': {
                'full_name': 'John Stith Pemberton',
                'birth_date': '1831-07-08'
            }
        },
        {
            'name': 'PepsiCo Inc.',
            'category': 'Beverages',
            'founding_date': '1965-06-23',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PEP',
            'market_cap': 230000000000,  # $230B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Pepsi-Logo.png',
            'tagline': 'For the Love of It',
            'cultural_data': {
                'colors': 'Blue, Red, White',
                'notes': 'Blue circle represents youth and refreshment. Patriotic colors embody American spirit.'
            }
        },
        {
            'name': 'Monster Beverage Corporation',
            'category': 'Beverages',
            'founding_date': '1985-04-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MNST',
            'market_cap': 55000000000,  # $55B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Monster-Energy-Logo.png',
            'tagline': 'Unleash the Beast',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'Green claw marks represent energy and power. Black symbolizes strength and rebellion.'
            }
        },
        {
            'name': 'Red Bull GmbH',
            'category': 'Beverages',
            'founding_date': '1987-04-01',
            'country': 'Austria',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Red-Bull-Logo.png',
            'tagline': 'Red Bull Gives You Wings',
            'cultural_data': {
                'colors': 'Blue, Red, Yellow',
                'notes': 'Bulls represent power and energy. Blue and red create dynamic contrast symbolizing vitality.'
            },
            'founder_data': {
                'full_name': 'Dietrich Mateschitz',
                'birth_date': '1944-05-20'
            }
        },

        # RETAIL EXPANSION (Currently 5 brands)
        {
            'name': 'Walmart Inc.',
            'category': 'Retail',
            'founding_date': '1962-07-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WMT',
            'market_cap': 650000000000,  # $650B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Walmart-Logo.png',
            'tagline': 'Save Money. Live Better.',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Spark symbol represents inspiration. Blue conveys trust, yellow represents optimism and value.'
            },
            'founder_data': {
                'full_name': 'Sam Walton',
                'birth_date': '1918-03-29'
            }
        },
        {
            'name': 'Target Corporation',
            'category': 'Retail',
            'founding_date': '1902-06-24',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'TGT',
            'market_cap': 65000000000,  # $65B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Target-Logo.png',
            'tagline': 'Expect More. Pay Less.',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Bullseye represents precision and hitting targets. Red conveys energy and excitement.'
            }
        },
        {
            'name': 'Costco Wholesale Corporation',
            'category': 'Retail',
            'founding_date': '1976-07-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'COST',
            'market_cap': 380000000000,  # $380B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Costco-Logo.png',
            'tagline': 'Do the Right Thing',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Blue represents trust and reliability. Red conveys value and savings for members.'
            }
        },
        {
            'name': 'The Home Depot Inc.',
            'category': 'Retail',
            'founding_date': '1978-06-22',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'HD',
            'market_cap': 410000000000,  # $410B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Home-Depot-Logo.png',
            'tagline': 'How Doers Get More Done',
            'cultural_data': {
                'colors': 'Orange, White',
                'notes': 'Orange represents energy, enthusiasm, and the do-it-yourself spirit.'
            },
            'founder_data': {
                'full_name': 'Bernie Marcus',
                'birth_date': '1929-05-12'
            }
        },
        {
            'name': 'Lidl Stiftung & Co. KG',
            'category': 'Retail',
            'founding_date': '1973-01-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Lidl-Logo.png',
            'tagline': 'Big on Quality, Lidl on Price',
            'cultural_data': {
                'colors': 'Blue, Yellow, Red',
                'notes': 'Blue represents trust and quality. Yellow and red create dynamic contrast for value positioning.'
            }
        },
        {
            'name': 'Aldi Süd',
            'category': 'Retail',
            'founding_date': '1961-07-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Aldi-Logo.png',
            'tagline': 'Simply Smarter Shopping',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'Blue conveys trust and reliability. Orange represents value and accessibility.'
            }
        },

        # FOOD PROCESSING EXPANSION (Currently 2 brands)
        {
            'name': 'Nestlé S.A.',
            'category': 'Food Processing',
            'founding_date': '1866-01-01',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'NSRGY',
            'market_cap': 350000000000,  # $350B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Nestle-Logo.png',
            'tagline': 'Good Food, Good Life',
            'cultural_data': {
                'colors': 'Brown, White',
                'notes': 'Nest symbol represents nurturing and family care. Brown conveys naturalness and nourishment.'
            },
            'founder_data': {
                'full_name': 'Henri Nestlé',
                'birth_date': '1814-08-10'
            }
        },
        {
            'name': 'The Kraft Heinz Company',
            'category': 'Food Processing',
            'founding_date': '2015-07-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'KHC',
            'market_cap': 40000000000,  # $40B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Kraft-Heinz-Logo.png',
            'tagline': 'To Be the Best Food Company',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Blue represents trust and heritage. Red conveys energy and appetite appeal.'
            }
        },
        {
            'name': 'General Mills Inc.',
            'category': 'Food Processing',
            'founding_date': '1866-06-20',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'GIS',
            'market_cap': 42000000000,  # $42B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/General-Mills-Logo.png',
            'tagline': 'Nourishing Lives',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Red represents energy and appetite. Blue conveys trust and family values.'
            }
        },
        {
            'name': 'Kellogg Company',
            'category': 'Food Processing',
            'founding_date': '1906-02-19',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'K',
            'market_cap': 22000000000,  # $22B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Kelloggs-Logo.png',
            'tagline': 'Let\'s Make Today Great',
            'cultural_data': {
                'colors': 'Red, Green',
                'notes': 'Red represents energy and morning vitality. Green conveys health and nutrition.'
            },
            'founder_data': {
                'full_name': 'Will Keith Kellogg',
                'birth_date': '1860-04-07'
            }
        },

        # PHARMACEUTICALS EXPANSION (Currently 6 brands)
        {
            'name': 'Pfizer Inc.',
            'category': 'Pharmaceuticals',
            'founding_date': '1849-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PFE',
            'market_cap': 280000000000,  # $280B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Pfizer-Logo.png',
            'tagline': 'Breakthroughs That Change Patients\' Lives',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents trust, reliability, and medical expertise. DNA spiral symbolizes innovation.'
            },
            'founder_data': {
                'full_name': 'Charles Pfizer',
                'birth_date': '1824-03-22'
            }
        },
        {
            'name': 'Novartis AG',
            'category': 'Pharmaceuticals',
            'founding_date': '1996-03-07',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'NVS',
            'market_cap': 220000000000,  # $220B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Novartis-Logo.png',
            'tagline': 'Reimagining Medicine',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents scientific precision and healthcare trust. Clean design conveys innovation.'
            }
        },
        {
            'name': 'Roche Holding AG',
            'category': 'Pharmaceuticals',
            'founding_date': '1896-10-01',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'RHHBY',
            'market_cap': 280000000000,  # $280B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Roche-Logo.png',
            'tagline': 'Doing Now What Patients Need Next',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'Blue represents medical trust. Orange conveys innovation and human warmth in healthcare.'
            },
            'founder_data': {
                'full_name': 'Fritz Hoffmann-La Roche',
                'birth_date': '1868-10-24'
            }
        },
        {
            'name': 'AstraZeneca plc',
            'category': 'Pharmaceuticals',
            'founding_date': '1999-04-06',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'AZN',
            'market_cap': 200000000000,  # $200B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/AstraZeneca-Logo.png',
            'tagline': 'Following the Science',
            'cultural_data': {
                'colors': 'Purple, White',
                'notes': 'Purple represents innovation and scientific discovery. Conveys premium pharmaceutical expertise.'
            }
        },

        # COSMETICS EXPANSION (Currently 4 brands)
        {
            'name': 'L\'Oréal S.A.',
            'category': 'Cosmetics',
            'founding_date': '1909-07-30',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'OR',
            'market_cap': 200000000000,  # $200B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LOreal-Logo.png',
            'tagline': 'Because You\'re Worth It',
            'cultural_data': {
                'colors': 'Black, Gold',
                'notes': 'Black represents sophistication and luxury. Gold conveys premium quality and self-worth.'
            },
            'founder_data': {
                'full_name': 'Eugène Schueller',
                'birth_date': '1881-03-20'
            }
        },
        {
            'name': 'The Estée Lauder Companies',
            'category': 'Cosmetics',
            'founding_date': '1946-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'EL',
            'market_cap': 65000000000,  # $65B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Estee-Lauder-Logo.png',
            'tagline': 'Bringing the Best to Everyone We Touch',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents elegance and trustworthiness. Clean design conveys premium beauty standards.'
            },
            'founder_data': {
                'full_name': 'Estée Lauder',
                'birth_date': '1908-07-01'
            }
        },
        {
            'name': 'Coty Inc.',
            'category': 'Cosmetics',
            'founding_date': '1904-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'COTY',
            'market_cap': 8000000000,  # $8B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Coty-Logo.png',
            'tagline': 'Beauty That Lasts',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Black represents luxury and timeless elegance. Minimalist design conveys sophistication.'
            },
            'founder_data': {
                'full_name': 'François Coty',
                'birth_date': '1874-05-03'
            }
        },
        {
            'name': 'Shiseido Company',
            'category': 'Cosmetics',
            'founding_date': '1872-09-08',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': '4911',
            'market_cap': 15000000000,  # $15B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Shiseido-Logo.png',
            'tagline': 'A Beautiful Life',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Red represents beauty and vitality in Japanese culture. Black conveys elegance and precision.'
            },
            'founder_data': {
                'full_name': 'Arinobu Fukuhara',
                'birth_date': '1848-12-30'
            }
        },

        # ENTERTAINMENT EXPANSION (Currently 3 brands)
        {
            'name': 'The Walt Disney Company',
            'category': 'Entertainment',
            'founding_date': '1923-10-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'DIS',
            'market_cap': 175000000000,  # $175B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Disney-Logo.png',
            'tagline': 'The Magic of Disney',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Castle represents dreams and imagination. Blue conveys trust and family-friendly values.'
            },
            'founder_data': {
                'full_name': 'Walt Disney',
                'birth_date': '1901-12-05'
            }
        },
        {
            'name': 'Warner Bros. Discovery',
            'category': 'Entertainment',
            'founding_date': '2022-04-08',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WBD',
            'market_cap': 25000000000,  # $25B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Warner-Bros-Logo.png',
            'tagline': 'The Stuff That Dreams Are Made Of',
            'cultural_data': {
                'colors': 'Blue, Gold',
                'notes': 'Shield represents protection and quality content. Gold conveys premium entertainment value.'
            }
        },
        {
            'name': 'Universal Music Group',
            'category': 'Entertainment',
            'founding_date': '1934-01-01',
            'country': 'United States',
            'parent_company': 'Vivendi',
            'stock_ticker': 'UMG',
            'market_cap': 45000000000,  # $45B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Universal-Music-Logo.png',
            'tagline': 'Music Is Universal',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Globe represents worldwide music reach. Black and white convey timeless musical heritage.'
            }
        },

        # CONSUMER GOODS EXPANSION (Currently 5 brands)
        {
            'name': 'Procter & Gamble Co.',
            'category': 'Consumer Goods',
            'founding_date': '1837-10-31',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'PG',
            'market_cap': 380000000000,  # $380B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Procter-Gamble-Logo.png',
            'tagline': 'Touching Lives, Improving Life',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents trust and reliability in household products. Clean design conveys quality.'
            },
            'founder_data': {
                'full_name': 'William Procter',
                'birth_date': '1801-11-07'
            }
        },
        {
            'name': 'Colgate-Palmolive Company',
            'category': 'Consumer Goods',
            'founding_date': '1806-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CL',
            'market_cap': 65000000000,  # $65B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Colgate-Logo.png',
            'tagline': 'Smile. It\'s Contagious.',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Red represents health and vitality. White conveys cleanliness and oral hygiene.'
            },
            'founder_data': {
                'full_name': 'William Colgate',
                'birth_date': '1783-01-25'
            }
        },
        {
            'name': 'Henkel AG & Co. KGaA',
            'category': 'Consumer Goods',
            'founding_date': '1876-09-26',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'HEN3',
            'market_cap': 18000000000,  # $18B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Henkel-Logo.png',
            'tagline': 'Excellence Is Our Passion',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Red represents innovation and quality. Black conveys German engineering excellence.'
            },
            'founder_data': {
                'full_name': 'Fritz Henkel',
                'birth_date': '1848-03-20'
            }
        },

        # ELECTRONICS EXPANSION (Currently 2 brands)
        {
            'name': 'Sony Group Corporation',
            'category': 'Electronics',
            'founding_date': '1946-05-07',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'SONY',
            'market_cap': 110000000000,  # $110B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Sony-Logo.png',
            'tagline': 'Be Moved',
            'cultural_data': {
                'colors': 'Black, White',
                'notes': 'Clean typography represents Japanese minimalism and technological precision.'
            },
            'founder_data': {
                'full_name': 'Masaru Ibuka',
                'birth_date': '1908-04-11'
            }
        },
        {
            'name': 'LG Electronics Inc.',
            'category': 'Electronics',
            'founding_date': '1958-01-05',
            'country': 'South Korea',
            'parent_company': 'LG Corporation',
            'stock_ticker': '066570',
            'market_cap': 12000000000,  # $12B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LG-Logo.png',
            'tagline': 'Life\'s Good',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Circle represents harmony and human-centered technology. Red conveys energy and innovation.'
            }
        },
        {
            'name': 'Panasonic Holdings Corporation',
            'category': 'Electronics',
            'founding_date': '1918-03-07',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': '6752',
            'market_cap': 25000000000,  # $25B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Panasonic-Logo.png',
            'tagline': 'A Better Life, A Better World',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents reliability and technological advancement. Conveys trust in Japanese quality.'
            },
            'founder_data': {
                'full_name': 'Konosuke Matsushita',
                'birth_date': '1894-11-27'
            }
        },

        # FOOD SERVICE EXPANSION (Currently 1 brand)
        {
            'name': 'McDonald\'s Corporation',
            'category': 'Food Service',
            'founding_date': '1955-04-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MCD',
            'market_cap': 210000000000,  # $210B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/McDonalds-Logo.png',
            'tagline': 'I\'m Lovin\' It',
            'cultural_data': {
                'colors': 'Yellow, Red',
                'notes': 'Golden arches represent welcoming and happiness. Red and yellow stimulate appetite and energy.'
            },
            'founder_data': {
                'full_name': 'Ray Kroc',
                'birth_date': '1902-10-05'
            }
        },
        {
            'name': 'Starbucks Corporation',
            'category': 'Food Service',
            'founding_date': '1971-03-30',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'SBUX',
            'market_cap': 110000000000,  # $110B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Starbucks-Logo.png',
            'tagline': 'To Inspire and Nurture the Human Spirit',
            'cultural_data': {
                'colors': 'Green, White',
                'notes': 'Siren represents maritime coffee trading heritage. Green conveys growth and premium experience.'
            }
        },
        {
            'name': 'Yum! Brands Inc.',
            'category': 'Food Service',
            'founding_date': '1997-10-07',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'YUM',
            'market_cap': 40000000000,  # $40B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Yum-Brands-Logo.png',
            'tagline': 'How Hungry Are You?',
            'cultural_data': {
                'colors': 'Red, Yellow',
                'notes': 'Vibrant colors represent fun and appetite appeal. Conveys global food brand excitement.'
            }
        },

        # INSURANCE EXPANSION (Currently 1 brand)
        {
            'name': 'Berkshire Hathaway Inc.',
            'category': 'Insurance',
            'founding_date': '1839-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'BRK.A',
            'market_cap': 900000000000,  # $900B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Berkshire-Hathaway-Logo.png',
            'tagline': 'Building Value Through Diversification',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents trust and financial stability. Clean design conveys reliability and permanence.'
            }
        },
        {
            'name': 'Allianz SE',
            'category': 'Insurance',
            'founding_date': '1890-02-05',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'ALV',
            'market_cap': 95000000000,  # $95B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Allianz-Logo.png',
            'tagline': 'We Secure Your Future',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents security and trust. Eagle symbolizes protection and strength in insurance.'
            }
        },
        {
            'name': 'AXA Group',
            'category': 'Insurance',
            'founding_date': '1817-01-01',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'CS',
            'market_cap': 60000000000,  # $60B
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/AXA-Logo.png',
            'tagline': 'Know You Can',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Blue represents trust and security. Red conveys confidence and strength in protection.'
            }
        }
    ]


def add_comprehensive_expansion():
    """Add comprehensive brands across underrepresented categories."""
    researcher = BrandResearcher()
    expansion_brands = get_comprehensive_expansion()
    
    print(f"Adding {len(expansion_brands)} brands across underrepresented categories...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(expansion_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} ({brand_data['category']}) (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nComprehensive categories expansion completed!")
    
    # Generate updated statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    
    print(f"\nUPDATED DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    
    # Updated category distribution
    categories = {}
    for brand in updated_brands:
        cat = brand['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\nUpdated category distribution:")
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category}: {count} brands")
    
    # Market cap analysis
    brands_with_cap = [b for b in updated_brands if b['market_cap']]
    if brands_with_cap:
        total_cap = sum(b['market_cap'] for b in brands_with_cap)
        print(f"\nMarket cap analysis:")
        print(f"  Brands with market cap data: {len(brands_with_cap)}")
        print(f"  Total market cap: ${total_cap:,}")
        print(f"  Average market cap: ${total_cap/len(brands_with_cap):,.0f}")


if __name__ == "__main__":
    add_comprehensive_expansion()