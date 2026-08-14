import pytest
from libs.DataReader import read_customer, read_order
from libs.DataManipulation import filter_closed_order, count_order_state, join_orders_customers
from libs.ConfigReader import get_app_config

@pytest.mark.skip
def test_read_customer(spark):
    customer_count = read_customer(spark,"LOCAL").count()
    assert customer_count == 12435

@pytest.mark.skip
def test_read_order(spark):
    order_count = read_order(spark,"LOCAL").count()
    assert order_count == 68884

@pytest.mark.skip
def test_filter_closed(spark):
    order_df = read_order(spark,"LOCAL")
    order_closed = filter_closed_order(order_df).count()
    assert order_closed == 7556

@pytest.mark.transformation()
def test_app_config():
    app_data = get_app_config("LOCAL")
    assert app_data['customer.file.path'] == "data/customers.csv"

@pytest.mark.count()
def test_state_count(spark,get_generated_data):
    customer_df = read_customer(spark,"LOCAL")
    order_df = read_order(spark,"LOCAL")
    customer_order = join_orders_customers(order_df,customer_df)
    state_count = count_order_state(customer_order)

    assert state_count.orderBy("state").collect() == get_generated_data.orderBy("state").collect()

@pytest.mark.order_status()
@pytest.mark.parametrize("status,count" , [('CLOSED',7556),('PENDING_PAYMENT',15030)])
def test_order(spark, status, count):
    order_df = read_order(spark,"LOCAL").filter(f"order_status='{status}'").count()
    assert order_df ==  count