# Logging Concept

'''<---------------------------------------------------------------------->'''

# every activity should be record
# information should be help full for future

'''<---------------------------------------------------------------------->'''

# The file can contain the information on which part of the code is executed 
# and what problems have been arisen

'''<--------------------------------------------------------------------->'''

# Each built-in level has been assigned its numeric value.

# NOTSET    ---     0
# DEBUG     ---     10
# INFO      ---     20
# WARNING   ---     30
# ERROR     ---     40
# CRITICAL  ---     50

'''<--------------------------------------------------------------------->'''

# if level will warning
# it will show msg up to warning >> error >> critical

# import logging

# logging.basicConfig(filename='log.txt', level=logging.WARNING)

# print('python logging demo')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('werning message')
# logging.error('error message')
# logging.critical('critical message')


'''<--------------------------------------------------------------------->'''
# if level will debug
# it will show all msg like debug >> info >> warning >> error >> critical


# import logging

# logging.basicConfig(filename='log.txt', level=logging.DEBUG)
# print('python logging demo')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('werning message')
# logging.error('error message')
# logging.critical('critical message')


'''<--------------------------------------------------------------------->'''


# import logging

# logging.basicConfig(filename='app1.txt', level=logging.INFO)
# logging.info('A new request came')

# try:
#     x = int(input('enter number : '))
#     y = int(input('enter number : '))
#     print(x/y)

# except ZeroDivisionError as msg:
#     print('divided by zero')
#     logging.exception(msg)

# except ValueError as msg:
#     print('value should be int')
#     logging.exception(msg)

# logging.info('Process will completed')

'''<--------------------------------------------------------------------->'''

# using the logging module to record the events in a file

#--->>>     # import module
            
            #-->> import logging

#--->>>     # Create and configure the logger. It can have several parameters. But importantly, 
            # pass the name of the file in which you want to record the events.
            
            #-->> logging.basicConfig(filename='loger.txt', format='%(asctime)s %(message)s', filemode='w')

#--->>>     # Here the format of the logger can also be set. By default, 
            # the file works in append mode but we can change that to write mode if required.

            #-->> filemode = 'w'

#--->>>     # Also, the level of the logger can be set which acts as the threshold for 
            # tracking based on the numeric values assigned to each level.

            #-->> Setting the threshold of logger to DEBUG

            #-->> logger.setLevel(logging.DEBUG)

#--->>>     # There are several attributes which can be passed as parameters.
            
            #-->> (filename='loger.txt', format='%(asctime)s %(message)s', filemode='w')

#--->>>     # The list of all those parameters is given in Python Library. 
            # The user can choose the required attribute according to the requirement.

            #-->> 

'''<--------------------------------------------------------------------->'''

# Logger.info(msg) : This will log a message with level INFO on this logger.

# Logger.warning(msg) : This will log a message with level WARNING on this logger.

# Logger.error(msg) : This will log a message with level ERROR on this logger.

# Logger.critical(msg) : This will log a message with level CRITICAL on this logger.

# Logger.log(lvl,msg) : This will Logs a message with integer level lvl on this logger.

# Logger.exception(msg) : This will log a message with level ERROR on this logger.

# Logger.setLevel(lvl) : This function sets the threshold of this logger to lvl. 
                        # This means that all the messages below this level will be ignored.

# Logger.addFilter(filt) : This adds a specific filter filt to the to this logger.

# Logger.removeFilter(filt) : This removes a specific filter filt to the to this logger.

# Logger.filter(record) : This method applies the logger’s filter to the record provided and 
                        # returns True if record is to be processed. Else, it will return False.

# Logger.addHandler(hdlr) : This adds a specific handler hdlr to the to this logger.

# Logger.removeHandler(hdlr) : This removes a specific handler hdlr to the to this logger.

# Logger.hasHandlers() : This checks if the logger has any handler configured or not.


'''<--------------------------------------------------------------------->'''

# import logging

# #Create and configure logger
# logging.basicConfig(filename='record.txt', filemode='w')

# #Creating an object
# logger = logging.getLogger()

# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

# logger.debug('this is debug')
# logger.info('this is info msg')
# logger.warning('this is warning msg')
# logger.error('this is error msg')
# logger.critical('this is crititcal msg')

'''<--------------------------------------------------------------------->'''


# import logging

# #Create and configure logger
# logging.basicConfig(filename='timerecord.txt', format='%(asctime)s %(message)s', filemode='w')

# #Creating an object
# logger = logging.getLogger()

# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

# logger.debug('this is debug2')
# logger.info('this is info msg')
# logger.warning('this is warning msg')
# logger.error('this is error msg')
# logger.critical('this is crititcal msg')


'''<--------------------------------------------------------------------->'''


name = 'marcog'
number = 42
print ('%s %d' % (name, number))

'''<--------------------------------------------------------------------->'''

'''<--------------------------------------------------------------------->'''

'''<--------------------------------------------------------------------->'''
