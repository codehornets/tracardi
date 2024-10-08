from sqlalchemy import Column, Integer, String, DateTime, Float, JSON, Boolean, PrimaryKeyConstraint, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DOUBLE

Base = declarative_base()

class EventTable(Base):
    __tablename__ = 'event'

    # Define fields according to Elasticsearch mapping
    id = Column(String(64))
    name = Column(String(255))

    metadata_aux = Column(JSON)

    metadata_time_insert = Column(DateTime)
    metadata_time_create = Column(DateTime)
    metadata_time_process_time = Column(Float)
    metadata_time_total_time = Column(Float)
    metadata_status = Column(String(32), default="NULL")
    metadata_channel = Column(String(255))
    metadata_ip = Column(String(255))
    metadata_processed_by_rules = Column(String(255))
    metadata_processed_by_flows = Column(String(255))
    metadata_processed_by_third_party = Column(String(255))
    metadata_profile_less = Column(Boolean)
    metadata_valid = Column(Boolean)
    metadata_warning = Column(Boolean)
    metadata_error = Column(Boolean)
    metadata_merge = Column(Boolean)
    metadata_instance_id = Column(String(40))
    metadata_debug = Column(Boolean)

    type = Column(String(255), default="NULL")
    request = Column(JSON)

    source_id = Column(String(64))
    device_name = Column(String(255))
    device_brand = Column(String(255))
    device_model = Column(String(255))
    device_ip = Column(String(18))
    device_type = Column(String(255))
    device_touch = Column(Boolean)
    device_resolution = Column(String(32))
    device_color_depth = Column(Integer)
    device_orientation = Column(String(32))

    device_geo_country_name = Column(String(255))
    device_geo_country_code = Column(String(10))
    device_geo_county = Column(String(64))
    device_geo_city = Column(String(64))
    device_geo_latitude = Column(Float)
    device_geo_longitude = Column(Float)
    device_geo_location = Column(JSON)
    device_geo_postal = Column(String(24))

    os_name = Column(String(64))
    os_version = Column(String(32))

    app_type = Column(String(255))
    app_bot = Column(Boolean)
    app_name = Column(String(255))
    app_version = Column(String(255))
    app_language = Column(String(32))
    app_resolution = Column(String(32))

    hit_name = Column(String(255))
    hit_url = Column(String(255))
    hit_referer = Column(String(255))
    hit_query = Column(String(255))
    hit_category = Column(String(64))
    hit_id = Column(String(32))

    utm_source = Column(String(64))
    utm_medium = Column(String(64))
    utm_campaign = Column(String(64))
    utm_term = Column(String(64))
    utm_content = Column(String(96))

    session_id = Column(String(64))
    session_start = Column(DateTime)
    session_duration = Column(Float)
    session_tz = Column(String(64))

    profile_id = Column(String(64))

    entity_id = Column(String(64))

    aux = Column(JSON)
    trash = Column(JSON)
    config = Column(JSON)
    context = Column(JSON)
    properties = Column(JSON)
    traits = Column(JSON)

    data_media_image = Column(String(255))
    data_media_webpage = Column(String(255))
    data_media_social_twitter = Column(String(255))
    data_media_social_facebook = Column(String(255))
    data_media_social_youtube = Column(String(255))
    data_media_social_instagram = Column(String(255))
    data_media_social_tiktok = Column(String(255))
    data_media_social_linkedin = Column(String(255))
    data_media_social_reddit = Column(String(255))
    data_media_social_other = Column(JSON)

    data_pii_firstname = Column(String(255))
    data_pii_lastname = Column(String(255))
    data_pii_display_name = Column(String(255))
    data_pii_birthday = Column(DateTime)
    data_pii_language_native = Column(String(255))
    data_pii_language_spoken = Column(String(255))
    data_pii_gender = Column(String(255))
    data_pii_education_level = Column(String(255))
    data_pii_civil_status = Column(String(255))
    data_pii_attributes_height = Column(Float)
    data_pii_attributes_weight = Column(Float)
    data_pii_attributes_shoe_number = Column(Float)

    data_identifier_id = Column(String(64))
    data_identifier_pk = Column(String(64))
    data_identifier_badge = Column(String(64))
    data_identifier_passport = Column(String(32))
    data_identifier_credit_card = Column(String(24))
    data_identifier_token = Column(String(96))
    data_identifier_coupons = Column(String(32))

    data_contact_email_main = Column(String(64))
    data_contact_email_private = Column(String(64))
    data_contact_email_business = Column(String(64))
    data_contact_phone_main = Column(String(32))
    data_contact_phone_business = Column(String(32))
    data_contact_phone_mobile = Column(String(32))
    data_contact_phone_whatsapp = Column(String(32))
    data_contact_app_whatsapp = Column(String(255))
    data_contact_app_discord = Column(String(255))
    data_contact_app_slack = Column(String(255))
    data_contact_app_twitter = Column(String(255))
    data_contact_app_telegram = Column(String(255))
    data_contact_app_wechat = Column(String(255))
    data_contact_app_viber = Column(String(255))
    data_contact_app_signal = Column(String(255))
    data_contact_app_other = Column(JSON)
    data_contact_address_town = Column(String(255))
    data_contact_address_county = Column(String(255))
    data_contact_address_country = Column(String(255))
    data_contact_address_postcode = Column(String(255))
    data_contact_address_street = Column(String(255))
    data_contact_address_other = Column(String(255))
    data_contact_confirmations = Column(String(255))

    data_job_position = Column(String(255))
    data_job_salary = Column(Float)
    data_job_type = Column(String(255))
    data_job_company_name = Column(String(255))
    data_job_company_size = Column(String(255))
    data_job_company_segment = Column(String(255))
    data_job_company_country = Column(String(255))
    data_job_department = Column(String(255))

    data_preferences_purchases = Column(String(255))
    data_preferences_colors = Column(String(255))
    data_preferences_sizes = Column(String(255))
    data_preferences_devices = Column(String(255))
    data_preferences_channels = Column(String(255))
    data_preferences_payments = Column(String(255))
    data_preferences_brands = Column(String(255))
    data_preferences_fragrances = Column(String(255))
    data_preferences_services = Column(String(255))
    data_preferences_other = Column(String(255))

    data_loyalty_codes = Column(String(255))
    data_loyalty_card_id = Column(String(64))
    data_loyalty_card_name = Column(String(255))
    data_loyalty_card_issuer = Column(String(255))
    data_loyalty_card_points = Column(Float)
    data_loyalty_card_expires = Column(DateTime)

    data_message_id = Column(String(36))
    data_message_conversation = Column(String(36))
    data_message_type = Column(String(32))
    data_message_text = Column(String(255))
    data_message_sender = Column(String(96))
    data_message_recipient = Column(String(96))
    data_message_status = Column(String(64))
    data_message_error_reason = Column(String(256))
    data_message_aux = Column(JSON)

    data_ec_order_id = Column(String(64))
    data_ec_order_status = Column(String(32))
    data_ec_order_receivable_value = Column(Float)
    data_ec_order_receivable_due_date = Column(DateTime)
    data_ec_order_receivable_currency = Column(String(255))
    data_ec_order_payable_value = Column(Float)
    data_ec_order_payable_due_date = Column(DateTime)
    data_ec_order_payable_currency = Column(String(255))
    data_ec_order_income_value = Column(Float)
    data_ec_order_income_due_date = Column(DateTime)
    data_ec_order_income_currency = Column(String(255))
    data_ec_order_cost_value = Column(Float)
    data_ec_order_cost_due_date = Column(DateTime)
    data_ec_order_cost_currency = Column(String(255))
    data_ec_order_affiliation = Column(String(32))

    data_ec_checkout_id = Column(String(64))
    data_ec_checkout_status = Column(String(32))
    data_ec_checkout_currency = Column(String(8))
    data_ec_checkout_value = Column(Float)

    data_ec_product_id = Column(String(64))
    data_ec_product_name = Column(String(255))
    data_ec_product_sku = Column(String(32))
    data_ec_product_category = Column(String(64))
    data_ec_product_brand = Column(String(96))
    data_ec_product_variant_name = Column(String(255))
    data_ec_product_variant_color = Column(String(48))
    data_ec_product_variant_size = Column(String(16))
    data_ec_product_price = Column(Float)
    data_ec_product_quantity = Column(Float)
    data_ec_product_position = Column(Integer)
    data_ec_product_review = Column(String(255))
    data_ec_product_rate = Column(Integer)

    data_payment_method = Column(String(255))
    data_payment_credit_card_number = Column(String(24))
    data_payment_credit_card_expires = Column(DateTime)
    data_payment_credit_card_holder = Column(String(64))

    data_journey_state = Column(String(32))
    data_journey_rate = Column(Float)

    data_marketing_coupon = Column(String(255))
    data_marketing_channel = Column(String(255))
    data_marketing_promotion_id = Column(String(64))
    data_marketing_promotion_name = Column(String(64))

    tags_values = Column(String(255))
    tags_count = Column(DOUBLE)

    journey_state = Column(String(32))

    production = Column(Boolean)  # Add this field for multi-tenancy

    # Primary key constraint
    __table_args__ = (
        PrimaryKeyConstraint('id', 'production'),
    )

class ProfileTable(Base):
    __tablename__ = 'profile'

    # Primary Key
    id = Column(String(64))

    # Other fields
    ids = Column(String(255))  # Array of ids
    metadata_status = Column(String(32), default="NULL")
    metadata_aux = Column(JSON)
    metadata_system = Column(JSON)
    metadata_time_insert = Column(DateTime)
    metadata_time_create = Column(DateTime)
    metadata_time_update = Column(DateTime)
    metadata_time_segmentation = Column(DateTime)
    metadata_time_visit_last = Column(DateTime)
    metadata_time_visit_current = Column(DateTime)
    metadata_time_visit_count = Column(Integer)
    metadata_time_visit_tz = Column(String(255))
    metadata_fields = Column(JSON)

    data_anonymous = Column(Boolean)
    data_media_image = Column(String(255))
    data_media_webpage = Column(String(255))
    data_media_social_twitter = Column(String(255))
    data_media_social_facebook = Column(String(255))
    data_media_social_youtube = Column(String(255))
    data_media_social_instagram = Column(String(255))
    data_media_social_tiktok = Column(String(255))
    data_media_social_linkedin = Column(String(255))
    data_media_social_reddit = Column(String(255))
    data_media_social_other = Column(JSON)

    data_pii_firstname = Column(String(255))
    data_pii_lastname = Column(String(255))
    data_pii_display_name = Column(String(255))
    data_pii_birthday = Column(DateTime)
    data_pii_language_native = Column(String(255))
    data_pii_language_spoken = Column(String(255))
    data_pii_gender = Column(String(255))
    data_pii_education_level = Column(String(255))
    data_pii_civil_status = Column(String(255))
    data_pii_attributes_height = Column(Float)
    data_pii_attributes_weight = Column(Float)
    data_pii_attributes_shoe_number = Column(Float)

    data_identifier_id = Column(String(64))
    data_identifier_pk = Column(String(64))
    data_identifier_badge = Column(String(64))
    data_identifier_passport = Column(String(32))
    data_identifier_credit_card = Column(String(24))
    data_identifier_token = Column(String(96))
    data_identifier_coupons = Column(String(32))

    data_contact_email_main = Column(String(64))
    data_contact_email_private = Column(String(64))
    data_contact_email_business = Column(String(64))
    data_contact_phone_main = Column(String(32))
    data_contact_phone_business = Column(String(32))
    data_contact_phone_mobile = Column(String(32))
    data_contact_phone_whatsapp = Column(String(32))
    data_contact_app_whatsapp = Column(String(255))
    data_contact_app_discord = Column(String(255))
    data_contact_app_slack = Column(String(255))
    data_contact_app_twitter = Column(String(255))
    data_contact_app_telegram = Column(String(255))
    data_contact_app_wechat = Column(String(255))
    data_contact_app_viber = Column(String(255))
    data_contact_app_signal = Column(String(255))
    data_contact_app_other = Column(JSON)
    data_contact_address_town = Column(String(255))
    data_contact_address_county = Column(String(255))
    data_contact_address_country = Column(String(255))
    data_contact_address_postcode = Column(String(255))
    data_contact_address_street = Column(String(255))
    data_contact_address_other = Column(String(255))
    data_contact_confirmations = Column(String(255))

    data_job_position = Column(String(255))
    data_job_salary = Column(Float)
    data_job_type = Column(String(255))
    data_job_company_name = Column(String(255))
    data_job_company_size = Column(String(255))
    data_job_company_segment = Column(String(255))
    data_job_company_country = Column(String(255))
    data_job_department = Column(String(255))

    data_preferences_purchases = Column(String(255))
    data_preferences_colors = Column(String(255))
    data_preferences_sizes = Column(String(255))
    data_preferences_devices = Column(String(255))
    data_preferences_channels = Column(String(255))
    data_preferences_payments = Column(String(255))
    data_preferences_brands = Column(String(255))
    data_preferences_fragrances = Column(String(255))
    data_preferences_services = Column(String(255))
    data_preferences_other = Column(String(255))

    data_devices_push = Column(String(40))
    data_devices_other = Column(String(40))
    data_devices_last_geo_country_name = Column(String(64))
    data_devices_last_geo_country_code = Column(String(10))
    data_devices_last_geo_county = Column(String(64))
    data_devices_last_geo_city = Column(String(64))
    data_devices_last_geo_latitude = Column(Float)
    data_devices_last_geo_longitude = Column(Float)
    data_devices_last_geo_location = Column(JSON)
    data_devices_last_geo_postal = Column(String(24))

    data_metrics_ltv = Column(Float)
    data_metrics_ltcosc = Column(Integer)
    data_metrics_ltcocc = Column(Integer)
    data_metrics_ltcop = Column(Float)
    data_metrics_ltcosv = Column(Float)
    data_metrics_ltoccv = Column(Float)
    data_metrics_next = Column(DateTime)
    data_metrics_custom = Column(JSON)

    data_loyalty_codes = Column(String(255))
    data_loyalty_card_id = Column(String(64))
    data_loyalty_card_name = Column(String(255))
    data_loyalty_card_issuer = Column(String(255))
    data_loyalty_card_points = Column(Float)
    data_loyalty_card_expires = Column(DateTime)

    stats = Column(JSON)
    traits = Column(JSON)
    collections = Column(JSON)
    segments = Column(String(64))
    consents = Column(JSON)
    active = Column(Boolean)
    interests = Column(JSON)
    aux = Column(JSON)
    trash = Column(JSON)
    misc = Column(JSON)

    production = Column(Boolean)  # Add this field for multi-tenancy

    __table_args__ = (
        PrimaryKeyConstraint('id', 'production'),
    )
