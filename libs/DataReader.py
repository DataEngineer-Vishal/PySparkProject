from libs import ConfigReader

def get_customer_schema():
    customer_schema = 'customer_id int, customer_fname string, customer_lname string, ' \
    'username string, password string, address string, city string, state string, pincode string'

    return customer_schema

def read_customer(spark,env):
    conf = ConfigReader.get_app_config(env)
    customer_file = conf["customer.file.path"]

    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_customer_schema()) \
    .load(customer_file)


def get_order_schema():
    order_schema = 'order_id int, order_date date, customer_id int, order_status string'
    return order_schema

def read_order(spark,env):
    conf = ConfigReader.get_app_config(env)
    order_file = conf["order.file.path"]

    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(get_order_schema()) \
    .load(order_file)