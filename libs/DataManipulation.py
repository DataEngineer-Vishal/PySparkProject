from pyspark.sql.functions import *

def filter_closed_order(order_df):
    return order_df.filter("order_status='CLOSED'")

def join_orders_customers(order_df,customer_df):
    return order_df.join(customer_df,"customer_id","inner")

def count_order_state(joined_df):
    return joined_df.groupBy("state").count()