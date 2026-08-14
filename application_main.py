import sys
from libs import Utils, DataReader, DataManipulation
from libs.logger import Log4j

if (__name__ == "__main__"):

    if len(sys.argv) < 2:
        print("Specify environment details [LOCAL/SIT/PROD]")
        exit(0)

    env =  sys.argv[1]

    spark = Utils.get_spark_session(env)

    logger = Log4j(spark)

    logger.warn("Creating Spark Session")

    order_df = DataReader.read_order(spark,env)

    order_filtered = DataManipulation.filter_closed_order(order_df)

    customer_df = DataReader.read_customer(spark,env)

    cutomer_order_join = DataManipulation.join_orders_customers(order_df,customer_df)

    state_count = DataManipulation.count_order_state(cutomer_order_join)

    print ("Below are state wise customer count for closed order:") 
    state_count.show()

    logger.info("End of Main")

#    state_count.write \
#    .format("csv") \
#    .option("header","true") \
#    .mode("overwrite") \
#    .option("path","data/state_count") \
#    .save()
    
    