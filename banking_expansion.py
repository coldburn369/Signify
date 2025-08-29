#!/usr/bin/env python3
"""
Comprehensive Banking Sector Expansion
Adding major German and European banks plus global banking leaders.
"""

from brand_research import BrandResearcher


def get_banking_expansion():
    """Return comprehensive banking institutions focused on German and European banks."""
    return [
        # Major German Banks
        {
            'name': 'Deutsche Bank AG',
            'category': 'Banking',
            'founding_date': '1870-03-10',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'DB',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Deutsche-Bank-Logo.png',
            'tagline': 'Banking for the Future',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'German financial powerhouse. Blue represents trust and stability in European banking tradition.'
            },
            'founder_data': {
                'full_name': 'Georg Siemens',
                'birth_date': '1839-10-21'
            }
        },
        {
            'name': 'Commerzbank AG',
            'category': 'Banking',
            'founding_date': '1870-02-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'CBK',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Commerzbank-Logo.png',
            'tagline': 'The Bank at Your Side',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Yellow represents innovation and optimism in German commercial banking.'
            }
        },
        {
            'name': 'DZ Bank AG',
            'category': 'Banking',
            'founding_date': '1949-01-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/DZ-Bank-Logo.png',
            'tagline': 'Cooperative Banking Excellence',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'Central institution for German cooperative banks. Orange represents community spirit.'
            }
        },
        {
            'name': 'KfW Bankengruppe',
            'category': 'Banking',
            'founding_date': '1948-11-16',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/KfW-Logo.png',
            'tagline': 'Financing Progress',
            'cultural_data': {
                'colors': 'Green, Blue',
                'notes': 'German development bank. Green represents sustainable development and environmental focus.'
            }
        },
        {
            'name': 'Bayerische Landesbank',
            'category': 'Banking',
            'founding_date': '1972-08-15',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BayernLB-Logo.png',
            'tagline': 'Your Bavarian Partner',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Bavarian state bank. Blue and white represent Bavarian regional identity and tradition.'
            }
        },
        {
            'name': 'Landesbank Baden-Württemberg',
            'category': 'Banking',
            'founding_date': '1999-01-01',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/LBBW-Logo.png',
            'tagline': 'Strong. Reliable. Close.',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'State bank of Baden-Württemberg. Red represents strength and regional commitment.'
            }
        },

        # Major French Banks
        {
            'name': 'BNP Paribas',
            'category': 'Banking',
            'founding_date': '1848-05-02',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'BNP',
            'market_cap': 75000000000,  # $75B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BNP-Paribas-Logo.png',
            'tagline': 'The Bank for a Changing World',
            'cultural_data': {
                'colors': 'Green, White',
                'notes': 'European banking leader. Green represents growth and environmental commitment.'
            }
        },
        {
            'name': 'Crédit Agricole',
            'category': 'Banking',
            'founding_date': '1894-02-05',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'ACA',
            'market_cap': 50000000000,  # $50B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Credit-Agricole-Logo.png',
            'tagline': 'Together, Everything is Possible',
            'cultural_data': {
                'colors': 'Green, Red',
                'notes': 'French cooperative bank. Green represents agricultural heritage and sustainability.'
            }
        },
        {
            'name': 'Société Générale',
            'category': 'Banking',
            'founding_date': '1864-05-04',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'GLE',
            'market_cap': 35000000000,  # $35B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Societe-Generale-Logo.png',
            'tagline': 'Together, We Are the Change',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'French universal bank. Red represents innovation and dynamic banking solutions.'
            },
            'founder_data': {
                'full_name': 'Paulin Talabot',
                'birth_date': '1799-05-18'
            }
        },
        {
            'name': 'Groupe BPCE',
            'category': 'Banking',
            'founding_date': '2009-07-31',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BPCE-Logo.png',
            'tagline': 'Cooperative Banking Together',
            'cultural_data': {
                'colors': 'Blue, Orange',
                'notes': 'French cooperative banking group. Orange represents warmth and community focus.'
            }
        },

        # Major Dutch Banks
        {
            'name': 'ING Group',
            'category': 'Banking',
            'founding_date': '1991-03-01',
            'country': 'Netherlands',
            'parent_company': None,
            'stock_ticker': 'INGA',
            'market_cap': 45000000000,  # $45B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ING-Logo.png',
            'tagline': 'Do Your Thing',
            'cultural_data': {
                'colors': 'Orange, White',
                'notes': 'Dutch banking and financial services. Orange represents Dutch national identity and innovation.'
            }
        },
        {
            'name': 'ABN AMRO Bank',
            'category': 'Banking',
            'founding_date': '1991-09-01',
            'country': 'Netherlands',
            'parent_company': None,
            'stock_ticker': 'ABN',
            'market_cap': 20000000000,  # $20B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/ABN-AMRO-Logo.png',
            'tagline': 'Personal Banking That Fits',
            'cultural_data': {
                'colors': 'Green, Yellow',
                'notes': 'Historic Dutch bank. Green represents stability and Dutch commercial tradition.'
            }
        },

        # Major Italian Banks
        {
            'name': 'UniCredit S.p.A.',
            'category': 'Banking',
            'founding_date': '1998-10-01',
            'country': 'Italy',
            'parent_company': None,
            'stock_ticker': 'UCG',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/UniCredit-Logo.png',
            'tagline': 'Unlocking Potential',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Pan-European banking group. Red represents Italian passion and European connectivity.'
            }
        },
        {
            'name': 'Intesa Sanpaolo',
            'category': 'Banking',
            'founding_date': '2007-01-01',
            'country': 'Italy',
            'parent_company': None,
            'stock_ticker': 'ISP',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Intesa-Sanpaolo-Logo.png',
            'tagline': 'Excellence Made Simple',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Italian banking leader. Blue represents trust and Mediterranean banking heritage.'
            }
        },

        # Major Spanish Banks
        {
            'name': 'Banco Santander',
            'category': 'Banking',
            'founding_date': '1857-05-15',
            'country': 'Spain',
            'parent_company': None,
            'stock_ticker': 'SAN',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Santander-Logo.png',
            'tagline': 'Simple, Personal, Fair',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Spanish multinational bank. Red flame represents passion and global Spanish banking reach.'
            },
            'founder_data': {
                'full_name': 'Queen Isabella II of Spain',
                'birth_date': '1830-10-10'
            }
        },
        {
            'name': 'Banco Bilbao Vizcaya Argentaria',
            'category': 'Banking',
            'founding_date': '1999-10-01',
            'country': 'Spain',
            'parent_company': None,
            'stock_ticker': 'BBVA',
            'market_cap': 35000000000,  # $35B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BBVA-Logo.png',
            'tagline': 'Creating Opportunities',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Spanish global bank. Blue represents digital innovation and international expansion.'
            }
        },

        # Major Nordic Banks
        {
            'name': 'Nordea Bank Abp',
            'category': 'Banking',
            'founding_date': '2000-03-01',
            'country': 'Finland',
            'parent_company': None,
            'stock_ticker': 'NDA',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Nordea-Logo.png',
            'tagline': 'Making It Possible',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Nordic banking leader. Blue represents Nordic values of trust and sustainability.'
            }
        },
        {
            'name': 'Skandinaviska Enskilda Banken',
            'category': 'Banking',
            'founding_date': '1856-01-01',
            'country': 'Sweden',
            'parent_company': None,
            'stock_ticker': 'SEB',
            'market_cap': 15000000000,  # $15B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/SEB-Logo.png',
            'tagline': 'For the Many People and Businesses',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'Swedish banking heritage. Green represents Nordic sustainability and environmental consciousness.'
            }
        },
        {
            'name': 'Danske Bank',
            'category': 'Banking',
            'founding_date': '1871-10-05',
            'country': 'Denmark',
            'parent_company': None,
            'stock_ticker': 'DANSKE',
            'market_cap': 12000000000,  # $12B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Danske-Bank-Logo.png',
            'tagline': 'New Standards',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Danish banking leader. Blue represents Danish design principles and Nordic reliability.'
            }
        },

        # Major Austrian Banks
        {
            'name': 'Raiffeisen Bank International',
            'category': 'Banking',
            'founding_date': '1927-01-01',
            'country': 'Austria',
            'parent_company': None,
            'stock_ticker': 'RBI',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Raiffeisen-Logo.png',
            'tagline': 'Banking for Central and Eastern Europe',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Austrian cooperative bank. Yellow represents agricultural heritage and cooperative values.'
            }
        },
        {
            'name': 'Erste Group Bank AG',
            'category': 'Banking',
            'founding_date': '1819-10-04',
            'country': 'Austria',
            'parent_company': None,
            'stock_ticker': 'EBS',
            'market_cap': 10000000000,  # $10B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Erste-Bank-Logo.png',
            'tagline': 'Believe in First',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Austrian savings bank. Red represents Austrian heritage and Central European banking tradition.'
            }
        },

        # Major UK Banks (Additional)
        {
            'name': 'Lloyds Banking Group',
            'category': 'Banking',
            'founding_date': '1765-01-01',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'LLOY',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Lloyds-Logo.png',
            'tagline': 'By Your Side',
            'cultural_data': {
                'colors': 'Green, Black',
                'notes': 'British banking heritage. Black horse represents strength and reliability.'
            }
        },
        {
            'name': 'NatWest Group',
            'category': 'Banking',
            'founding_date': '1968-12-01',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'NWG',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/NatWest-Logo.png',
            'tagline': 'Helpful Banking',
            'cultural_data': {
                'colors': 'Purple, White',
                'notes': 'British retail banking. Purple represents premium service and innovation.'
            }
        },

        # Major Belgian Banks
        {
            'name': 'KBC Group',
            'category': 'Banking',
            'founding_date': '1998-03-01',
            'country': 'Belgium',
            'parent_company': None,
            'stock_ticker': 'KBC',
            'market_cap': 20000000000,  # $20B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/KBC-Logo.png',
            'tagline': 'Live Your Passion',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Belgian banking and insurance. Blue represents Belgian reliability and European integration.'
            }
        },

        # Major Eastern European Banks
        {
            'name': 'PKO Bank Polski',
            'category': 'Banking',
            'founding_date': '1919-02-02',
            'country': 'Poland',
            'parent_company': None,
            'stock_ticker': 'PKO',
            'market_cap': 15000000000,  # $15B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/PKO-Bank-Logo.png',
            'tagline': 'Bank of Polish Dreams',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Polish national bank. Red and white represent Polish national colors and independence.'
            }
        },

        # Major Swiss Banks (Additional)
        {
            'name': 'Credit Suisse Group AG',
            'category': 'Banking',
            'founding_date': '1856-07-05',
            'country': 'Switzerland',
            'parent_company': None,
            'stock_ticker': None,  # Acquired by UBS
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/Credit-Suisse-Logo.png',
            'tagline': 'We Are Here to Help You Succeed',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Historic Swiss private banking. Blue represents Swiss financial tradition and discretion.'
            }
        },

        # Major Portuguese Banks
        {
            'name': 'Banco Comercial Português',
            'category': 'Banking',
            'founding_date': '1985-01-01',
            'country': 'Portugal',
            'parent_company': None,
            'stock_ticker': 'BCP',
            'market_cap': 5000000000,  # $5B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/09/BCP-Logo.png',
            'tagline': 'Your Bank for Life',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Portuguese banking leader. Blue represents Portuguese maritime heritage and reliability.'
            }
        }
    ]


def add_banking_expansion():
    """Add comprehensive European and German banking institutions."""
    researcher = BrandResearcher()
    banking_brands = get_banking_expansion()
    
    print(f"Adding {len(banking_brands)} major European and German banks...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(banking_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} ({brand_data['country']}) (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nBanking expansion completed!")
    
    # Generate banking-specific statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    
    # Count banking brands
    banking_brands_count = len([b for b in updated_brands if b['category'] == 'Banking'])
    
    print(f"\nBANKING DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    print(f"  Banking institutions: {banking_brands_count}")
    
    # Banking brands by country
    banking_countries = {}
    for brand in updated_brands:
        if brand['category'] == 'Banking':
            country = brand['country']
            banking_countries[country] = banking_countries.get(country, 0) + 1
    
    print(f"\nBanking institutions by country:")
    for country, count in sorted(banking_countries.items(), key=lambda x: x[1], reverse=True):
        print(f"  {country}: {count} banks")
    
    # Market cap analysis for banking
    banking_with_cap = [b for b in updated_brands if b['category'] == 'Banking' and b['market_cap']]
    if banking_with_cap:
        total_banking_cap = sum(b['market_cap'] for b in banking_with_cap)
        print(f"\nBanking market cap analysis:")
        print(f"  Banks with market cap data: {len(banking_with_cap)}")
        print(f"  Total banking market cap: ${total_banking_cap:,}")
        print(f"  Average banking market cap: ${total_banking_cap/len(banking_with_cap):,.0f}")


if __name__ == "__main__":
    add_banking_expansion()