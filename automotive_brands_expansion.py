#!/usr/bin/env python3
"""
Comprehensive Automotive Brands Expansion
Adding all major automotive brands with detailed information.
"""

from brand_research import BrandResearcher


def get_automotive_brands_data():
    """Return comprehensive automotive brands data."""
    return [
        # German Premium Brands
        {
            'name': 'Audi AG',
            'category': 'Automotive',
            'founding_date': '1909-07-16',
            'country': 'Germany',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': 'AUDVF',
            'market_cap': 65000000000,  # $65B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Audi-Logo.png',
            'tagline': 'Vorsprung durch Technik',
            'cultural_data': {
                'colors': 'Silver, Black, Red',
                'notes': 'Four rings represent union of four companies. Silver symbolizes premium quality and innovation.'
            },
            'founder_data': {
                'full_name': 'August Horch',
                'birth_date': '1868-10-12'
            }
        },
        {
            'name': 'Mercedes-Benz Group AG',
            'category': 'Automotive',
            'founding_date': '1926-06-28',
            'country': 'Germany',
            'parent_company': None,
            'stock_ticker': 'MBGAF',
            'market_cap': 75000000000,  # $75B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Mercedes-Benz-Logo.png',
            'tagline': 'The Best or Nothing',
            'cultural_data': {
                'colors': 'Silver, Black',
                'notes': 'Three-pointed star represents land, sea, and air mobility. Silver embodies luxury and precision.'
            },
            'founder_data': {
                'full_name': 'Gottlieb Daimler',
                'birth_date': '1834-03-17'
            }
        },
        {
            'name': 'Porsche AG',
            'category': 'Automotive',
            'founding_date': '1931-04-25',
            'country': 'Germany',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': 'POAHY',
            'market_cap': 85000000000,  # $85B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Porsche-Logo.png',
            'tagline': 'There is No Substitute',
            'cultural_data': {
                'colors': 'Black, Gold, Red',
                'notes': 'Stuttgart coat of arms with horse. Black and gold represent luxury and performance heritage.'
            },
            'founder_data': {
                'full_name': 'Ferdinand Porsche',
                'birth_date': '1875-09-03'
            }
        },
        {
            'name': 'Opel Automobile GmbH',
            'category': 'Automotive',
            'founding_date': '1862-01-21',
            'country': 'Germany',
            'parent_company': 'Stellantis',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Opel-Logo.png',
            'tagline': 'We Live Opel',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Lightning bolt represents speed and innovation. Originally a sewing machine manufacturer.'
            },
            'founder_data': {
                'full_name': 'Adam Opel',
                'birth_date': '1837-05-09'
            }
        },

        # American Icons
        {
            'name': 'Ford Motor Company',
            'category': 'Automotive',
            'founding_date': '1903-06-16',
            'country': 'United States',
            'parent_company': None,
            'stock_ticker': 'F',
            'market_cap': 50000000000,  # $50B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Ford-Logo.png',
            'tagline': 'Built Ford Tough',
            'cultural_data': {
                'colors': 'Blue, White',
                'notes': 'Oval logo represents reliability and American automotive heritage. Blue conveys trust and dependability.'
            },
            'founder_data': {
                'full_name': 'Henry Ford',
                'birth_date': '1863-07-30'
            }
        },
        {
            'name': 'General Motors (Chevrolet)',
            'category': 'Automotive',
            'founding_date': '1911-11-03',
            'country': 'United States',
            'parent_company': 'General Motors',
            'stock_ticker': 'GM',
            'market_cap': 60000000000,  # $60B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Chevrolet-Logo.png',
            'tagline': 'Find New Roads',
            'cultural_data': {
                'colors': 'Gold, Black',
                'notes': 'Bowtie logo represents elegance and American automotive innovation. Gold symbolizes excellence.'
            },
            'founder_data': {
                'full_name': 'Louis Chevrolet',
                'birth_date': '1878-12-25'
            }
        },
        {
            'name': 'Jeep',
            'category': 'Automotive',
            'founding_date': '1941-07-15',
            'country': 'United States',
            'parent_company': 'Stellantis',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Jeep-Logo.png',
            'tagline': 'Go Anywhere. Do Anything.',
            'cultural_data': {
                'colors': 'Black, Red',
                'notes': 'Seven-slot grille represents military heritage and off-road capability. Born from WWII utility vehicle.'
            }
        },
        {
            'name': 'Cadillac Motor Car Division',
            'category': 'Automotive',
            'founding_date': '1902-08-22',
            'country': 'United States',
            'parent_company': 'General Motors',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Cadillac-Logo.png',
            'tagline': 'Dare Greatly',
            'cultural_data': {
                'colors': 'Black, Gold, Silver',
                'notes': 'Coat of arms represents luxury and American aristocracy. Gold and silver embody premium craftsmanship.'
            },
            'founder_data': {
                'full_name': 'Henry Leland',
                'birth_date': '1843-02-16'
            }
        },

        # French Automotive
        {
            'name': 'Peugeot S.A.',
            'category': 'Automotive',
            'founding_date': '1810-01-01',
            'country': 'France',
            'parent_company': 'Stellantis',
            'stock_ticker': 'PEUGF',
            'market_cap': 40000000000,  # $40B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Peugeot-Logo.png',
            'tagline': 'Motion & e-Motion',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Lion logo represents strength and French automotive heritage. Originally a coffee mill manufacturer.'
            },
            'founder_data': {
                'full_name': 'Armand Peugeot',
                'birth_date': '1849-09-26'
            }
        },
        {
            'name': 'Renault S.A.',
            'category': 'Automotive',
            'founding_date': '1899-02-25',
            'country': 'France',
            'parent_company': None,
            'stock_ticker': 'RNLSY',
            'market_cap': 30000000000,  # $30B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Renault-Logo.png',
            'tagline': 'Passion for Life',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Diamond logo represents innovation and French automotive design. Yellow symbolizes energy and optimism.'
            },
            'founder_data': {
                'full_name': 'Louis Renault',
                'birth_date': '1877-02-12'
            }
        },
        {
            'name': 'Citroën',
            'category': 'Automotive',
            'founding_date': '1919-06-07',
            'country': 'France',
            'parent_company': 'Stellantis',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Citroen-Logo.png',
            'tagline': 'Inspired by You',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'Double chevron represents gear teeth, referencing founder\'s gear manufacturing background.'
            },
            'founder_data': {
                'full_name': 'André Citroën',
                'birth_date': '1878-02-05'
            }
        },

        # Italian Excellence
        {
            'name': 'Ferrari N.V.',
            'category': 'Automotive',
            'founding_date': '1939-09-13',
            'country': 'Italy',
            'parent_company': None,
            'stock_ticker': 'RACE',
            'market_cap': 75000000000,  # $75B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Ferrari-Logo.png',
            'tagline': 'We are the Competition',
            'cultural_data': {
                'colors': 'Red, Yellow, Black',
                'notes': 'Prancing horse represents speed and Italian racing heritage. Red is traditional Italian racing color.'
            },
            'founder_data': {
                'full_name': 'Enzo Ferrari',
                'birth_date': '1898-02-18'
            }
        },
        {
            'name': 'Fiat Chrysler (Stellantis)',
            'category': 'Automotive',
            'founding_date': '1899-07-11',
            'country': 'Italy',
            'parent_company': 'Stellantis',
            'stock_ticker': 'STLA',
            'market_cap': 55000000000,  # $55B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Fiat-Logo.png',
            'tagline': 'Driven by Passion',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'FIAT stands for Fabbrica Italiana Automobili Torino. Red represents Italian passion and heritage.'
            },
            'founder_data': {
                'full_name': 'Giovanni Agnelli',
                'birth_date': '1866-08-13'
            }
        },
        {
            'name': 'Lamborghini S.p.A.',
            'category': 'Automotive',
            'founding_date': '1963-10-30',
            'country': 'Italy',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Lamborghini-Logo.png',
            'tagline': 'Expect the Unexpected',
            'cultural_data': {
                'colors': 'Yellow, Black',
                'notes': 'Raging bull represents power and founder\'s zodiac sign (Taurus). Yellow symbolizes energy and speed.'
            },
            'founder_data': {
                'full_name': 'Ferruccio Lamborghini',
                'birth_date': '1916-04-28'
            }
        },
        {
            'name': 'Maserati S.p.A.',
            'category': 'Automotive',
            'founding_date': '1914-12-01',
            'country': 'Italy',
            'parent_company': 'Stellantis',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Maserati-Logo.png',
            'tagline': 'Excellence Through Passion',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Trident logo represents Neptune\'s strength. Founded by Maserati brothers in Bologna.'
            },
            'founder_data': {
                'full_name': 'Alfieri Maserati',
                'birth_date': '1887-12-24'
            }
        },
        {
            'name': 'Alfa Romeo Automobiles S.p.A.',
            'category': 'Automotive',
            'founding_date': '1910-06-24',
            'country': 'Italy',
            'parent_company': 'Stellantis',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Alfa-Romeo-Logo.png',
            'tagline': 'La meccanica delle emozioni',
            'cultural_data': {
                'colors': 'Red, White, Green',
                'notes': 'Logo combines Milan coat of arms and Visconti serpent. Italian flag colors represent heritage.'
            },
            'founder_data': {
                'full_name': 'Nicola Romeo',
                'birth_date': '1876-04-28'
            }
        },

        # British Heritage
        {
            'name': 'Jaguar Land Rover',
            'category': 'Automotive',
            'founding_date': '1935-09-04',
            'country': 'United Kingdom',
            'parent_company': 'Tata Motors',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Jaguar-Logo.png',
            'tagline': 'Grace, Space, Pace',
            'cultural_data': {
                'colors': 'Green, Silver',
                'notes': 'Leaping jaguar represents grace and power. British luxury and performance heritage.'
            },
            'founder_data': {
                'full_name': 'William Lyons',
                'birth_date': '1901-09-04'
            }
        },
        {
            'name': 'Land Rover',
            'category': 'Automotive',
            'founding_date': '1948-04-30',
            'country': 'United Kingdom',
            'parent_company': 'Tata Motors',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Land-Rover-Logo.png',
            'tagline': 'Above and Beyond',
            'cultural_data': {
                'colors': 'Green, Silver',
                'notes': 'Oval logo represents global capability. Green symbolizes connection to nature and off-road heritage.'
            }
        },
        {
            'name': 'Rolls-Royce Motor Cars',
            'category': 'Automotive',
            'founding_date': '1906-03-15',
            'country': 'United Kingdom',
            'parent_company': 'BMW Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Rolls-Royce-Logo.png',
            'tagline': 'Strive for Perfection',
            'cultural_data': {
                'colors': 'Black, Silver, Gold',
                'notes': 'Spirit of Ecstasy represents ultimate luxury. RR monogram symbolizes British automotive excellence.'
            },
            'founder_data': {
                'full_name': 'Charles Rolls',
                'birth_date': '1877-08-27'
            }
        },
        {
            'name': 'Bentley Motors',
            'category': 'Automotive',
            'founding_date': '1919-01-18',
            'country': 'United Kingdom',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Bentley-Logo.png',
            'tagline': 'Be Extraordinary',
            'cultural_data': {
                'colors': 'Green, Silver',
                'notes': 'Winged B represents speed and luxury. British racing green symbolizes heritage and performance.'
            },
            'founder_data': {
                'full_name': 'Walter Owen Bentley',
                'birth_date': '1888-09-16'
            }
        },
        {
            'name': 'Aston Martin Lagonda',
            'category': 'Automotive',
            'founding_date': '1913-01-15',
            'country': 'United Kingdom',
            'parent_company': None,
            'stock_ticker': 'AML',
            'market_cap': 2000000000,  # $2B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Aston-Martin-Logo.png',
            'tagline': 'Power, Beauty and Soul',
            'cultural_data': {
                'colors': 'Green, Silver',
                'notes': 'Wings represent speed and freedom. British racing heritage and James Bond association.'
            },
            'founder_data': {
                'full_name': 'Lionel Martin',
                'birth_date': '1878-08-20'
            }
        },
        {
            'name': 'MINI',
            'category': 'Automotive',
            'founding_date': '1959-08-26',
            'country': 'United Kingdom',
            'parent_company': 'BMW Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Mini-Logo.png',
            'tagline': 'Not Normal',
            'cultural_data': {
                'colors': 'Black, Silver',
                'notes': 'Wings represent freedom and British heritage. Circular design emphasizes the iconic round shape theme.'
            },
            'founder_data': {
                'full_name': 'Alec Issigonis',
                'birth_date': '1906-11-18'
            }
        },

        # Japanese Excellence
        {
            'name': 'Mazda Motor Corporation',
            'category': 'Automotive',
            'founding_date': '1920-01-30',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'MZDAY',
            'market_cap': 20000000000,  # $20B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Mazda-Logo.png',
            'tagline': 'Zoom-Zoom',
            'cultural_data': {
                'colors': 'Silver, Red',
                'notes': 'Flying M represents wings and continuous motion. Named after Ahura Mazda, Zoroastrian god of wisdom.'
            },
            'founder_data': {
                'full_name': 'Jujiro Matsuda',
                'birth_date': '1875-08-02'
            }
        },
        {
            'name': 'Mitsubishi Motors Corporation',
            'category': 'Automotive',
            'founding_date': '1970-04-22',
            'country': 'Japan',
            'parent_company': 'Nissan Motor',
            'stock_ticker': 'MMTOF',
            'market_cap': 8000000000,  # $8B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Mitsubishi-Logo.png',
            'tagline': 'Drive Your Ambition',
            'cultural_data': {
                'colors': 'Red, Silver',
                'notes': 'Three diamonds represent reliability, integrity, and success. Part of Mitsubishi zaibatsu heritage.'
            }
        },
        {
            'name': 'Nissan Motor Corporation',
            'category': 'Automotive',
            'founding_date': '1933-12-26',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'NSANY',
            'market_cap': 25000000000,  # $25B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Nissan-Logo.png',
            'tagline': 'Innovation that Excites',
            'cultural_data': {
                'colors': 'Silver, Black, Red',
                'notes': 'Circle represents sun and Japanese heritage. Silver embodies innovation and modern technology.'
            },
            'founder_data': {
                'full_name': 'Yoshisuke Aikawa',
                'birth_date': '1880-11-06'
            }
        },
        {
            'name': 'Subaru Corporation',
            'category': 'Automotive',
            'founding_date': '1953-07-15',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'FUJHY',
            'market_cap': 15000000000,  # $15B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Subaru-Logo.png',
            'tagline': 'Love. It\'s What Makes Subaru a Subaru.',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Six stars represent Pleiades constellation. Subaru means "unite" in Japanese.'
            }
        },
        {
            'name': 'Suzuki Motor Corporation',
            'category': 'Automotive',
            'founding_date': '1909-10-01',
            'country': 'Japan',
            'parent_company': None,
            'stock_ticker': 'SZKMY',
            'market_cap': 18000000000,  # $18B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Suzuki-Logo.png',
            'tagline': 'Way of Life',
            'cultural_data': {
                'colors': 'Red, White',
                'notes': 'S logo represents simplicity and strength. Originally a loom manufacturer.'
            },
            'founder_data': {
                'full_name': 'Michio Suzuki',
                'birth_date': '1887-08-10'
            }
        },
        {
            'name': 'Lexus',
            'category': 'Automotive',
            'founding_date': '1989-08-01',
            'country': 'Japan',
            'parent_company': 'Toyota Motor Corporation',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Lexus-Logo.png',
            'tagline': 'Experience Amazing',
            'cultural_data': {
                'colors': 'Silver, Black',
                'notes': 'L logo represents luxury and precision. Premium brand representing Japanese craftsmanship excellence.'
            }
        },

        # Korean Innovation
        {
            'name': 'Kia Corporation',
            'category': 'Automotive',
            'founding_date': '1944-12-01',
            'country': 'South Korea',
            'parent_company': 'Hyundai Motor Group',
            'stock_ticker': 'KIMTF',
            'market_cap': 22000000000,  # $22B approx
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Kia-Logo.png',
            'tagline': 'Movement that Inspires',
            'cultural_data': {
                'colors': 'Red, Black',
                'notes': 'Oval logo represents global reach. Kia means "rising from Asia" in Korean.'
            }
        },

        # Swedish Engineering
        {
            'name': 'Volvo Cars',
            'category': 'Automotive',
            'founding_date': '1927-04-14',
            'country': 'Sweden',
            'parent_company': 'Geely',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Volvo-Logo.png',
            'tagline': 'For Life',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Iron symbol represents Swedish steel strength and safety heritage. Blue symbolizes trust and reliability.'
            },
            'founder_data': {
                'full_name': 'Assar Gabrielsson',
                'birth_date': '1891-08-13'
            }
        },
        {
            'name': 'Saab Automobile',
            'category': 'Automotive',
            'founding_date': '1945-12-01',
            'country': 'Sweden',
            'parent_company': None,
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Saab-Logo.png',
            'tagline': 'Born from Jets',
            'cultural_data': {
                'colors': 'Blue, Silver',
                'notes': 'Griffin logo represents Swedish heritage. Aviation background influences automotive innovation.'
            }
        },

        # Czech Engineering
        {
            'name': 'Škoda Auto',
            'category': 'Automotive',
            'founding_date': '1895-12-18',
            'country': 'Czech Republic',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Skoda-Logo.png',
            'tagline': 'Simply Clever',
            'cultural_data': {
                'colors': 'Green, White',
                'notes': 'Winged arrow represents speed and progress. Green symbolizes environmental consciousness.'
            },
            'founder_data': {
                'full_name': 'Václav Laurin',
                'birth_date': '1865-10-27'
            }
        },

        # Spanish Automotive
        {
            'name': 'SEAT S.A.',
            'category': 'Automotive',
            'founding_date': '1950-05-09',
            'country': 'Spain',
            'parent_company': 'Volkswagen Group',
            'stock_ticker': None,
            'market_cap': None,
            'logo_url': 'https://logos-world.net/wp-content/uploads/2020/04/Seat-Logo.png',
            'tagline': 'Enjoy the Unexpected',
            'cultural_data': {
                'colors': 'Red, Silver',
                'notes': 'Logo represents Spanish passion and Mediterranean spirit. Red symbolizes energy and emotion.'
            }
        }
    ]


def add_automotive_brands():
    """Add comprehensive automotive brands to the database."""
    researcher = BrandResearcher()
    automotive_brands = get_automotive_brands_data()
    
    print(f"Adding {len(automotive_brands)} major automotive brands...")
    
    # Get current count for numbering
    from database_query import BrandAnalyzer
    analyzer = BrandAnalyzer()
    current_brands = analyzer.get_all_brands()
    start_id = len(current_brands) + 1
    
    for i, brand_data in enumerate(automotive_brands, start_id):
        try:
            brand_id = researcher.process_brand(brand_data)
            print(f"{i:2d}. ✓ {brand_data['name']} (ID: {brand_id})")
        except Exception as e:
            print(f"{i:2d}. ✗ {brand_data['name']} - Error: {e}")
    
    print(f"\nAutomotive brands expansion completed!")
    
    # Generate updated statistics
    updated_brands = analyzer.get_all_brands()
    total_brands = len(updated_brands)
    automotive_count = len([b for b in updated_brands if b['category'] == 'Automotive'])
    
    print(f"\nUPDATED DATABASE STATISTICS:")
    print(f"  Total brands: {total_brands}")
    print(f"  Automotive brands: {automotive_count}")
    
    # Calculate total automotive market cap
    automotive_market_cap = sum(
        brand.get('market_cap', 0) for brand in updated_brands 
        if brand['category'] == 'Automotive' and brand.get('market_cap')
    )
    print(f"  Total automotive market cap: ${automotive_market_cap:,}")


if __name__ == "__main__":
    add_automotive_brands()