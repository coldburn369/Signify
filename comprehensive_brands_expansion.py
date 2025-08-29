#!/usr/bin/env python3
"""
Comprehensive Brands Database Expansion
Adding major brands across all categories for maximum global coverage.
"""

from brand_research import BrandResearcher


def get_comprehensive_brands_expansion():
    """Return comprehensive expansion across all major categories."""
    return [
        # Technology Giants (Additional)
        {
            'name': 'Oracle Corporation',
            'category': 'Technology',
            'founding_date': '1977-06-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'ORCL',
            'market_cap': 350000000000,  # $350B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Oracle-Logo.png',
            'tagline': 'Hardware and Software, Engineered to Work Together',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Red represents power and enterprise strength. Named after CIA project codename.'
            },
            'founder_data': {
                'full_name': 'Larry Ellison',
                'birth_date': '1944-08-17'
            }
        },
        {
            'name': 'SAP SE',
            'category': 'Technology',
            'founding_date': '1972-04-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'SAP',
            'market_cap': 150000000000,  # $150B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/SAP-Logo.png',
            'tagline': 'Help the World Run Better',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Blue represents enterprise reliability. Leading German software company.'
            },
            'founder_data': {
                'full_name': 'Hasso Plattner',
                'birth_date': '1944-01-21'
            }
        },
        {
            'name': 'Adobe Inc.',
            'category': 'Technology',
            'founding_date': '1982-12-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'ADBE',
            'market_cap': 240000000000,  # $240B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Adobe-Logo.png',
            'tagline': 'Changing the World Through Digital Experiences',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Red A represents creativity and design innovation. Named after creek behind founder\'s house.'
            },
            'founder_data': {
                'full_name': 'John Warnock',
                'birth_date': '1940-10-06'
            }
        },
        {
            'name': 'Salesforce Inc.',
            'category': 'Technology',
            'founding_date': '1999-03-08',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CRM',
            'market_cap': 200000000000,  # $200B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Salesforce-Logo.png',
            'tagline': 'The Customer Success Platform',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Cloud icon represents cloud computing pioneer. Blue symbolizes trust and innovation.'
            },
            'founder_data': {
                'full_name': 'Marc Benioff',
                'birth_date': '1964-09-25'
            }
        },
        {
            'name': 'IBM Corporation',
            'category': 'Technology',
            'founding_date': '1911-06-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'IBM',
            'market_cap': 130000000000,  # $130B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/IBM-Logo.png',
            'tagline': 'Think',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Big Blue represents reliability and innovation. Pioneer in computing and AI.'
            },
            'founder_data': {
                'full_name': 'Thomas J. Watson',
                'birth_date': '1874-02-17'
            }
        },
        {
            'name': 'Cisco Systems Inc.',
            'category': 'Technology',
            'founding_date': '1984-12-10',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CSCO',
            'market_cap': 200000000000,  # $200B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Cisco-Logo.png',
            'tagline': 'The Bridge to Possible',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Bridge logo represents San Francisco Golden Gate Bridge and networking connectivity.'
            }
        },

        # Banking & Financial Services (Additional)
        {
            'name': 'Wells Fargo & Company',
            'category': 'Banking',
            'founding_date': '1852-03-18',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WFC',
            'market_cap': 160000000000,  # $160B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Wells-Fargo-Logo.png',
            'tagline': 'Together We\'ll Go Far',
            'cultural_data': {
                'colors': 'Red, Yellow',
                'notes': 'Stagecoach represents frontier heritage and reliability. Founded during Gold Rush.'
            }
        },
        {
            'name': 'Citigroup Inc.',
            'category': 'Banking',
            'founding_date': '1812-06-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'C',
            'market_cap': 90000000000,  # $90B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Citigroup-Logo.png',
            'tagline': 'Citi Never Sleeps',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Arc logo represents global reach and progress. One of the oldest US banks.'
            }
        },
        {
            'name': 'Goldman Sachs Group Inc.',
            'category': 'Banking',
            'founding_date': '1869-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'GS',
            'market_cap': 120000000000,  # $120B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Goldman-Sachs-Logo.png',
            'tagline': 'Progress is Everyone\'s Business',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Simple typography represents elite investment banking heritage and prestige.'
            },
            'founder_data': {
                'full_name': 'Marcus Goldman',
                'birth_date': '1821-12-09'
            }
        },
        {
            'name': 'Morgan Stanley',
            'category': 'Banking',
            'founding_date': '1935-09-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MS',
            'market_cap': 80000000000,  # $80B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Morgan-Stanley-Logo.png',
            'tagline': 'What We Do, We Do for You',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Clean design represents financial sophistication and Wall Street heritage.'
            }
        },
        {
            'name': 'American Express Company',
            'category': 'Financial Services',
            'founding_date': '1850-03-18',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'AXP',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/American-Express-Logo.png',
            'tagline': 'Don\'t Live Life Without It',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Centurion represents premium service and exclusivity. Blue conveys trust and prestige.'
            }
        },

        # Retail Giants (Additional)
        {
            'name': 'Target Corporation',
            'category': 'Retail',
            'founding_date': '1902-06-24',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'TGT',
            'market_cap': 70000000000,  # $70B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Target-Logo.png',
            'tagline': 'Expect More. Pay Less.',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Bullseye represents hitting the target with value and style. Red symbolizes energy and passion.'
            }
        },
        {
            'name': 'Costco Wholesale Corporation',
            'category': 'Retail',
            'founding_date': '1983-09-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'COST',
            'market_cap': 250000000000,  # $250B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Costco-Logo.png',
            'tagline': 'Do the Right Thing',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Simple design represents value and membership-based wholesale model.'
            }
        },
        {
            'name': 'Best Buy Co. Inc.',
            'category': 'Retail',
            'founding_date': '1966-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'BBY',
            'market_cap': 20000000000,  # $20B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Best-Buy-Logo.png',
            'tagline': 'Let\'s Talk About What\'s Possible',
            'cultural_data': {
                'colors': 'Blue, Yellow',
                'notes': 'Yellow tag represents best deals and consumer electronics expertise.'
            }
        },
        {
            'name': 'eBay Inc.',
            'category': 'E-commerce',
            'founding_date': '1995-09-03',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'EBAY',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/eBay-Logo.png',
            'tagline': 'Whatever It Is, You Can Get It on eBay',
            'cultural_data': {
                'colors': 'Blue, Red, Yellow, Green',
                'notes': 'Colorful letters represent diversity of products and global marketplace community.'
            },
            'founder_data': {
                'full_name': 'Pierre Omidyar',
                'birth_date': '1967-06-21'
            }
        },

        # Food & Beverages (Additional)
        {
            'name': 'Mondelez International',
            'category': 'Food & Beverages',
            'founding_date': '2012-10-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MDLZ',
            'market_cap': 90000000000,  # $90B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Mondelez-Logo.png',
            'tagline': 'Delicious Moments of Joy',
            'cultural_data': {
                'colors': 'Purple, Blue',
                'notes': 'Mondēlez means "delicious world" - combination of Latin and fabricated elements.'
            }
        },
        {
            'name': 'General Mills Inc.',
            'category': 'Food & Beverages',
            'founding_date': '1866-05-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'GIS',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/General-Mills-Logo.png',
            'tagline': 'Bringing Families Together Around Food They Love',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'G logo represents heritage in flour milling and American food traditions.'
            }
        },
        {
            'name': 'Kellogg Company',
            'category': 'Food & Beverages',
            'founding_date': '1906-02-19',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'K',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Kellogg-Logo.png',
            'tagline': 'Let\'s Make Today Great',
            'cultural_data': {
                'colors': 'Red, Green',
                'notes': 'Kellogg\'s script represents breakfast heritage and family nutrition tradition.'
            },
            'founder_data': {
                'full_name': 'Will Keith Kellogg',
                'birth_date': '1860-04-07'
            }
        },
        {
            'name': 'Kraft Heinz Company',
            'category': 'Food & Beverages',
            'founding_date': '2015-07-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'KHC',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Kraft-Heinz-Logo.png',
            'tagline': 'To Be the Best Food Company, Growing a Better World',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Merger of two iconic American food brands. Red represents Heinz heritage.'
            }
        },

        # Pharmaceuticals (Additional)
        {
            'name': 'Roche Holding AG',
            'category': 'Pharmaceuticals',
            'founding_date': '1896-10-01',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'RHHBY',
            'market_cap': 280000000000,  # $280B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Roche-Logo.png',
            'tagline': 'Doing Now What Patients Need Next',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Swiss precision in healthcare and pharmaceuticals. Blue represents trust and science.'
            },
            'founder_data': {
                'full_name': 'Fritz Hoffmann-La Roche',
                'birth_date': '1868-10-24'
            }
        },
        {
            'name': 'Novartis AG',
            'category': 'Pharmaceuticals',
            'founding_date': '1996-12-20',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'NVS',
            'market_cap': 210000000000,  # $210B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Novartis-Logo.png',
            'tagline': 'Reimagining Medicine',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Name means "new arts" in Latin. Blue represents scientific innovation and trust.'
            }
        },
        {
            'name': 'Merck & Co. Inc.',
            'category': 'Pharmaceuticals',
            'founding_date': '1891-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MRK',
            'market_cap': 250000000000,  # $250B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Merck-Logo.png',
            'tagline': 'Be Well',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Clean design represents pharmaceutical precision and healthcare commitment.'
            }
        },
        {
            'name': 'AbbVie Inc.',
            'category': 'Pharmaceuticals',
            'founding_date': '2013-01-02',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'ABBV',
            'market_cap': 300000000000,  # $300B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/AbbVie-Logo.png',
            'tagline': 'People. Passion. Possibilities.',
            'cultural_data': {
                'colors': 'Purple, White',
                'notes': 'Purple represents innovation in biotechnology and pharmaceutical research.'
            }
        },

        # Media & Entertainment (Additional)
        {
            'name': 'Comcast Corporation',
            'category': 'Media',
            'founding_date': '1963-06-28',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CMCSA',
            'market_cap': 150000000000,  # $150B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Comcast-Logo.png',
            'tagline': 'Connecting You to What Matters Most',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Peacock logo (NBCUniversal) represents colorful entertainment and broadcasting heritage.'
            }
        },
        {
            'name': 'Warner Bros. Discovery',
            'category': 'Media',
            'founding_date': '1923-04-04',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'WBD',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Warner-Bros-Logo.png',
            'tagline': 'If You Can Dream It, We Can Do It',
            'cultural_data': {
                'colors': 'Gold, Blue',
                'notes': 'Shield logo represents Hollywood heritage and entertainment legacy.'
            },
            'founder_data': {
                'full_name': 'Harry Warner',
                'birth_date': '1881-12-12'
            }
        },

        # Energy (Additional)
        {
            'name': 'Chevron Corporation',
            'category': 'Energy',
            'founding_date': '1879-09-10',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'CVX',
            'market_cap': 300000000000,  # $300B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Chevron-Logo.png',
            'tagline': 'Human Energy',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Chevron symbol represents energy and forward movement. Strong American energy heritage.'
            }
        },
        {
            'name': 'ConocoPhillips',
            'category': 'Energy',
            'founding_date': '2002-08-30',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'COP',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ConocoPhillips-Logo.png',
            'tagline': 'Know How to Succeed',
            'cultural_data': {
                'colors': 'Red, Blue',
                'notes': 'Merger of Conoco and Phillips Petroleum. Logo represents energy innovation.'
            }
        },
        {
            'name': 'TotalEnergies SE',
            'category': 'Energy',
            'founding_date': '1924-03-28',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'TTE',
            'market_cap': 160000000000,  # $160B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/TotalEnergies-Logo.png',
            'tagline': 'Energy is Reinventing Itself',
            'cultural_data': {
                'colors': 'Red, Blue, Green',
                'notes': 'Multi-energy logo represents transition to renewable energy and sustainability.'
            }
        },

        # Industrial Conglomerates (Additional)
        {
            'name': 'General Electric Company',
            'category': 'Industrial Conglomerate',
            'founding_date': '1892-04-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'GE',
            'market_cap': 180000000000,  # $180B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/GE-Logo.png',
            'tagline': 'Building a World That Works',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Monogram represents American industrial heritage and innovation across multiple sectors.'
            },
            'founder_data': {
                'full_name': 'Thomas Edison',
                'birth_date': '1847-02-11'
            }
        },
        {
            'name': '3M Company',
            'category': 'Industrial Conglomerate',
            'founding_date': '1902-06-13',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'MMM',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/3M-Logo.png',
            'tagline': 'Science Applied to Life',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Originally Minnesota Mining and Manufacturing. Red represents innovation and reliability.'
            }
        },
        {
            'name': 'Honeywell International Inc.',
            'category': 'Industrial Conglomerate',
            'founding_date': '1906-04-23',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'HON',
            'market_cap': 140000000000,  # $140B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Honeywell-Logo.png',
            'tagline': 'We Make What Matters Work',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Technology and manufacturing across aerospace, building tech, and performance materials.'
            }
        },

        # Luxury Goods (Additional)
        {
            'name': 'Richemont SA',
            'category': 'Luxury Goods',
            'founding_date': '1988-04-06',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': 'CFRUY',
            'market_cap': 75000000000,  # $75B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Richemont-Logo.png',
            'tagline': 'Excellence in Luxury',
            'cultural_data': {
                'colors': 'Gold, Black',
                'notes': 'Swiss luxury group owning Cartier, Van Cleef & Arpels. Gold represents ultimate luxury.'
            }
        },
        {
            'name': 'Estée Lauder Companies',
            'category': 'Cosmetics',
            'founding_date': '1946-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'EL',
            'market_cap': 50000000000,  # $50B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Estee-Lauder-Logo.png',
            'tagline': 'Bringing the Best to Everyone We Touch',
            'cultural_data': {
                'colors': 'Blue, Gold',
                'notes': 'Elegant script represents luxury cosmetics and beauty innovation heritage.'
            },
            'founder_data': {
                'full_name': 'Estée Lauder',
                'birth_date': '1908-07-01'
            }
        },

        # Telecommunications (Additional)
        {
            'name': 'T-Mobile US Inc.',
            'category': 'Telecommunications',
            'founding_date': '1994-07-01',
            'country': 'United States',
            'parent_company': 'Deutsche Telekom',
            'stock_ticker': 'TMUS',
            'market_cap': 190000000000,  # $190B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/T-Mobile-Logo.png',
            'tagline': 'The Un-carrier',
            'cultural_data': {
                'colors': 'Magenta, White',
                'notes': 'Magenta represents boldness and disruption in telecommunications industry.'
            }
        },

        # Aerospace (Additional)
        {
            'name': 'Lockheed Martin Corporation',
            'category': 'Aerospace',
            'founding_date': '1995-03-15',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'LMT',
            'market_cap': 110000000000,  # $110B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Lockheed-Martin-Logo.png',
            'tagline': 'We Never Forget Who We\'re Working For',
            'cultural_data': {
                'colors': 'Blue, Red',
                'notes': 'Star logo represents aerospace excellence and defense innovation.'
            }
        },
        {
            'name': 'Northrop Grumman Corporation',
            'category': 'Aerospace',
            'founding_date': '1994-01-01',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'NOC',
            'market_cap': 70000000000,  # $70B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Northrop-Grumman-Logo.png',
            'tagline': 'Defining Possible',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Represents advanced aerospace and defense technology innovation.'
            }
        }
    ]


def add_comprehensive_expansion():
    """Add comprehensive expansion across all categories."""
    researcher = BrandResearcher()
    expansion_brands = get_comprehensive_brands_expansion()
    
    print(f"Adding {len(expansion_brands)} brands across all major categories...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(expansion_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nComprehensive expansion completed!")
    
    # Generate updated statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    categories = set(brand['category'] for brand in updated_brands)
    countries = set(brand['country'] for brand in updated_brands)
    
    print(f"\nFINAL DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    print(f"  Categories: {len(categories)}")
    print(f"  Countries: {len(countries)}")
    
    # Top categories by brand count
    category_counts = {}
    for brand in updated_brands:
        category = brand['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    print(f"\nTop categories by brand count:")
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {category}: {count} brands")
    
    # Calculate total market cap
    total_market_cap = sum(brand.get('market_cap', 0) for brand in updated_brands if brand.get('market_cap'))
    print(f"\nTotal represented market cap: ${total_market_cap:,}")


if __name__ == "__main__":
    add_comprehensive_expansion()