TABLE="""CREATE TABLE your_table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    varchar_column VARCHAR(255),
    integer_column INT AUTO_INCREMENT,
    foreign_key_column INT,
    datetime_column DATETIME,
    status_column ENUM('active', 'inactive', 'pending'),
    CONSTRAINT fk_foreign_key FOREIGN KEY (foreign_key_column) REFERENCES referenced_table_name(referenced_column_name)
) AUTO_INCREMENT = 1000;"""

COUNTRY="""CREATE TABLE country (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255),
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive')
) AUTO_INCREMENT = 2000;"""

STATE="""CREATE TABLE state (
    id INT AUTO_INCREMENT PRIMARY KEY,
	country_id INT,
    state_name VARCHAR(255),
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive'),
	CONSTRAINT fk_country_id FOREIGN KEY (country_id) REFERENCES country(id)
) AUTO_INCREMENT = 3000;"""

AREA="""CREATE TABLE area (
    id INT AUTO_INCREMENT PRIMARY KEY,
	country_id INT,
	pincode INT,
    area_name VARCHAR(255),
	state_id INT,
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive'),
	CONSTRAINT fk_area_country_id FOREIGN KEY (country_id) REFERENCES country(id),
	CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES state(id)
) AUTO_INCREMENT = 4000;"""

USER_PROFILE="""CREATE TABLE user_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
	country_id INT,
	name VARCHAR(300),
	mobile_number VARCHAR(225),
	email varchar(300),
    password varchar(300),
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive'),
    CONSTRAINT fk_user_country_id FOREIGN KEY (country_id) REFERENCES country(id)
) AUTO_INCREMENT = 5000;"""


USER_ADDRESS_MANAGEMENT="""CREATE TABLE user_address_management(
    id INT AUTO_INCREMENT PRIMARY KEY,
	country_id INT,
	user_id INT,
    area_id INT,
	state_id int,
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive'),
	CONSTRAINT fk_add_country_id FOREIGN KEY (country_id) REFERENCES country(id),
	CONSTRAINT fk_add_state_id FOREIGN KEY (state_id) REFERENCES state(id),
    CONSTRAINT fk_add_area_id FOREIGN KEY (area_id) REFERENCES area(id)
) AUTO_INCREMENT = 6000;"""


PRODUCT_TYPE_CATEGORY="""CREATE TABLE product_type_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(255),
	description VARCHAR(300),
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive')
) AUTO_INCREMENT = 7000;"""


SUB_CATEGORY_PRODUCT="""CREATE TABLE sub_category_product(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_type_id INT,
    sub_category VARCHAR(255),
	description VARCHAR(300),
    created_by varchar(225),
    created_on DATETIME,
	modified_by varchar (225),
	modified_on datetime,
    status ENUM('active', 'inactive'),
    CONSTRAINT fk_category_product_id FOREIGN KEY (product_type_id) REFERENCES product_type_category(id)
) AUTO_INCREMENT = 8000;"""



PRICE_DECISION_FECTOR="""CREATE TABLE price_decision_factor(
    id INT AUTO_INCREMENT PRIMARY KEY,
    price_decision_factor ENUM('unit','kg','litres'),
    status ENUM('active', 'inactive'),
    created_by varchar(225)
) AUTO_INCREMENT = 9000;"""



CURRENCY="""CREATE TABLE currency(
    id INT AUTO_INCREMENT PRIMARY KEY,
    currency_type ENUM('dollar','INR'),
    status ENUM('active','inactive'),
    country_id INT,
    CONSTRAINT fk_currency_country_id FOREIGN KEY (country_id) REFERENCES country(id)
) AUTO_INCREMENT = 10000;"""



SELLER_CATEGORY="""CREATE TABLE seller_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    seller_category VARCHAR(100),
    description VARCHAR(300),
    seller_name VARCHAR(200),
    seller_country_id INT,
    seller_state_id INT,
    seller_area_id INT,
    status ENUM('active','inactive')
) AUTO_INCREMENT = 11000;"""


PRODUCT_PICTURE_CATEGORY="""CREATE TABLE product_picture_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    product_image_1 VARCHAR(300),
    product_image_2 VARCHAR(300),
    product_image_3 VARCHAR(300),
    status ENUM('active','inactive'),
    CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product_table(id)
) AUTO_INCREMENT = 12000;"""


PRODUCT_TABLE="""CREATE TABLE product_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    price_decision_factor_id INT,
    sub_category_product_id INT,
    seller_id INT,
    product_varient_id INT,
    product_name VARCHAR(250),
    description VARCHAR(250),
    price FLOAT,
    skv_code VARCHAR(250),
    availability_count INT,
    percentage_discount FLOAT,
    special_offer_price FLOAT,
    special_offer_minimum_quality FLOAT,
    special_offer_discount_factor FLOAT,
    CONSTRAINT fk_price_decision_factor FOREIGN KEY (price_decision_factor_id) REFERENCES price_decision_factor(id),
    CONSTRAINT fk_sub_category_product FOREIGN KEY (sub_category_product_id) REFERENCES sub_category_product(id),
    CONSTRAINT fk_product_varient_id FOREIGN KEY (product_varient_id) REFERENCES varient_category(id),
    CONSTRAINT fk_product_seller_category FOREIGN KEY (seller_id) REFERENCES seller_category(id)
)AUTO_INCREMENT = 13000;"""

VARIENT_CATEGORY="""CREATE TABLE varient_category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    varient_name VARCHAR(250),
    varient_description VARCHAR(250)
)AUTO_INCREMENT = 400;"""


USER_ORDER_MANAGEMENT="""CREATE TABLE user_order_management(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    ordered_on DATETIME,
    delivered_on DATETIME,
    address_id INT,
    ordered_status ENUM('delivered','in_transit','packing','returned','refunded'),
    CONSTRAINT fk_order_manage_user_id FOREIGN KEY (user_id) REFERENCES user_profile(id),
    CONSTRAINT fk_order_product_id FOREIGN KEY (product_id) REFERENCES product_table(id),
    CONSTRAINT fk_user_address_management FOREIGN KEY (address_id) REFERENCES user_address_management(id)
)AUTO_INCREMENT = 15000;"""


USER_CART_MANAGEMENT="""CREATE TABLE user_cart_management(
    user_id INT,
    product_id INT,
    quantity INT,
    CONSTRAINT fk_cart_user_id FOREIGN KEY (user_id) REFERENCES user_profile(id),
    CONSTRAINT fk_cart_product_id FOREIGN KEY (product_id) REFERENCES product_table(id)
)AUTO_INCREMENT = 16000;"""


def insert_query_marker(table_name,info_dict):
    columns=", ".join(info_dict.keys())
    values=", ".join(info_dict.values())
    tuple_fields=(table_name,columns,values)
    INSERT_QUERY = "INSERT INTO %s (%s) VALUES (%s)" % tuple_fields
    return INSERT_QUERY




FETCH_SELECT_USERS = "select * from user_profile where email='%s'"

FETCH_SELECT_PRODUCT = "select * from product_table as pt,varient_category as vc,seller_category as sc,price_decision_factor as pdf where  pt.seller_id =  sc.id  and pt.product_varient_id = vc.id and pt.seller_id = sc.id and pt.price_decision_factor_id = pdf.id and pt.availability_count > 0"

FETCH_AVAILABILITY_COUNT = "select availability_count from product_table where id = '%s'"

UPDATE_PRODUCT_COUNT = "update product_table set availability_count='%s' where id='%s'"

FETCH_CART = "select * from user_cart_management where user_id = '%s' and product_id = '%s'"

UPDATE_CART = "update user_cart_management set quantity=%s where user_id=%s and product_id=%s"

FETCH_LOGIN_USERS  = "SELECT * FROM user_profile where email='%s'"

FETCH_USER_CART_DETAILS = "select * from user_cart_management where user_id='%s'"

DELETE_USER_CART_DETAILS = "delete from user_cart_management where user_id='%s' and  product_id='%s'"

FETCH_CURRENCY_DETAILS = "select * from currency where country_id=%s"

FETCH_COUNTRY_DETAILS = "select * from country"

FETCH_STATE_DETAILS = "select * from state where country_id=%s"

FETCH_AREA_DETAILS = "select * from area where country_id=%s and state_id=%s"

FETCH_PRODUCT_DETAILS = "select * from product_table where id=%s"

FETCH_USER_ADDRESS_DETAILS = "select * from user_address_management u, country c, state s, area a where c.id = s.country_id and s.id = a.state_id and c.id=u.country_id and s.id = u.state_id and a.id = u.area_id and u.user_id='%s'"

FETCH_USER_order_DETAILS = "select * from user_order_management where user_id='%s'"

FETCH_USER_Picture_DETAILS = "select * from product_picture_category where product_id='%s'"

