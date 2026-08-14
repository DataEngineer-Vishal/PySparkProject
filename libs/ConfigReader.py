import configparser
from pyspark import SparkConf

def get_app_config(env):
    config = configparser.ConfigParser()
    config.read("configs/application.conf")

    conf_data = {}
    for (key,value) in config.items(env):
        conf_data[key] = value
    
    return conf_data


def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("configs/pyspark.conf")

    pyspark_data = SparkConf()

    for (key,value) in config.items(env):
        pyspark_data.set(key,value)

    return pyspark_data