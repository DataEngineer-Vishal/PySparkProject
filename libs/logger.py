class Log4j(object):
   
    def __init__(self, spark):
        # get spark app details with which to prefix all messages

        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger("retail_analysis")
        #self.logger.setLevel(spark._jvm.org.apache.log4j.Level.DEBUG)
        
    def error(self, message):
        """Log an error.

        :param: Error message to write to log
        :return: None
        """
        self.logger.error(message)
        

    def warn(self, message):
        """Log a warning.

        :param: Warning message to write to log
        :return: None
        """
        self.logger.warn(message)
        

    def info(self, message):
        """Log information.

        :param: Information message to write to log
        :return: None
        """
        self.logger.info(message)
        