-- Installs
CREATE TABLE installs (
    install_id SERIAL PRIMARY KEY,
    install_time TIMESTAMP,
    marketing_id VARCHAR(100),
    channel VARCHAR(100),
    medium VARCHAR(100),
    campaign VARCHAR(100),
    keyword VARCHAR(100),
    ad_content VARCHAR(100),
    ad_group VARCHAR(100),
    landing_page VARCHAR(100),
    sex VARCHAR(100),
    alpha_2 VARCHAR(100),
    alpha_3 VARCHAR(100),
    flag VARCHAR(100),
    name VARCHAR(100),
    numeric INT,
    official_name VARCHAR(100)
);

-- Costs
CREATE TABLE costs (
    cost_id SERIAL PRIMARY KEY,
    ad_content VARCHAR(100),
    landing_page VARCHAR(100),
    location VARCHAR(100),
    channel VARCHAR(100),
    keyword VARCHAR(100),
    campaign VARCHAR(100),
    ad_group VARCHAR(100),
    medium VARCHAR(100),
    cost FLOAT
);

-- Orders
CREATE TABLE IF NOT EXISTS orders
(
    order_id              SERIAL PRIMARY KEY,
    event_time            TIMESTAMP,
    transaction_id        VARCHAR(255),
    type                  VARCHAR(255),
    origin_transaction_id VARCHAR(255),
    category              VARCHAR(255),
    payment_method        VARCHAR(255),
    fee                   FLOAT,
    tax                   FLOAT,
    iap_item_name         VARCHAR(255),
    iap_item_price        FLOAT,
    discount_code         VARCHAR(255),
    discount_amount       FLOAT
);

-- Events
CREATE TABLE IF NOT EXISTS events (
    event_id SERIAL PRIMARY KEY,
    user_id VARCHAR,
    event_time TIMESTAMP,
    alpha_2 VARCHAR,
    alpha_3 VARCHAR,
    flag VARCHAR,
    name VARCHAR,
    numeric INT,
    official_name VARCHAR,
    os VARCHAR,
    brand VARCHAR,
    model VARCHAR,
    model_number INT,
    specification TEXT,
    event_type VARCHAR,
    location VARCHAR,
    user_action_detail VARCHAR,
    session_number INT,
    localization_id VARCHAR,
    ga_session_id VARCHAR,
    value FLOAT,
    state FLOAT,
    engagement_time_msec FLOAT,
    current_progress VARCHAR,
    event_origin VARCHAR,
    place FLOAT,
    selection VARCHAR,
    analytics_storage VARCHAR,
    browser VARCHAR,
    install_store VARCHAR,
    user_params_os VARCHAR,
    user_params_brand VARCHAR,
    user_params_model VARCHAR,
    user_params_model_number INT,
    user_params_specification VARCHAR,
    user_params_transaction_id VARCHAR,
    user_params_campaign_name VARCHAR,
    user_params_source VARCHAR,
    user_params_medium VARCHAR,
    user_params_term VARCHAR,
    user_params_context VARCHAR,
    user_params_gclid VARCHAR,
    user_params_dclid INT,
    user_params_srsltid INT,
    user_params_is_active_user INT,
    user_params_marketing_id VARCHAR
);
