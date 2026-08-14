import pytest
from libs.Utils import get_spark_session

@pytest.fixture
def spark():
    'This is used for creating spark session'
    spark_session = get_spark_session("LOCAL")
    yield spark_session
    spark_session.stop()

@pytest.fixture
def get_generated_data():
    'This is used for getting state wise count'
    spark = get_spark_session("LOCAL")

    state_schema = 'state string, count int'
    return spark.read \
    .format("csv") \
    .schema(state_schema) \
    .option("header","true") \
    .load("data/state_count/")