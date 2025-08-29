-- Global Brands Database Schema
-- Comprehensive database for major global brands with astrological and numerological data

CREATE TABLE brands (
    id              SERIAL PRIMARY KEY,
    name            VARCHAR(255) NOT NULL,
    category        VARCHAR(100),
    founding_date   DATE,
    country         VARCHAR(100),
    parent_company  VARCHAR(255),
    stock_ticker    VARCHAR(20),
    market_cap      BIGINT,
    logo_url        TEXT,
    tagline         TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE brand_astro_data (
    id                  SERIAL PRIMARY KEY,
    brand_id            INT REFERENCES brands(id) ON DELETE CASCADE,
    western_zodiac      VARCHAR(50),
    chinese_animal      VARCHAR(50),
    chinese_element     VARCHAR(50),
    life_path_number    INT,
    expression_number   INT,
    chaldean_number     INT
);

CREATE TABLE brand_cultural_data (
    id          SERIAL PRIMARY KEY,
    brand_id    INT REFERENCES brands(id) ON DELETE CASCADE,
    colors      VARCHAR(255),
    notes       TEXT
);

CREATE TABLE founders (
    id              SERIAL PRIMARY KEY,
    brand_id        INT REFERENCES brands(id) ON DELETE CASCADE,
    full_name       VARCHAR(255),
    birth_date      DATE,
    western_zodiac  VARCHAR(50),
    chinese_animal  VARCHAR(50),
    chinese_element VARCHAR(50),
    life_path_number INT,
    expression_number INT
);

-- Indexes for better performance
CREATE INDEX idx_brands_category ON brands(category);
CREATE INDEX idx_brands_country ON brands(country);
CREATE INDEX idx_brands_founding_date ON brands(founding_date);
CREATE INDEX idx_brand_astro_data_brand_id ON brand_astro_data(brand_id);
CREATE INDEX idx_brand_cultural_data_brand_id ON brand_cultural_data(brand_id);
CREATE INDEX idx_founders_brand_id ON founders(brand_id);