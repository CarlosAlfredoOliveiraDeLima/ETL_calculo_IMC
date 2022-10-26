from datetime import datetime

def log(message):
    timestamp_format = '%H:%M:%S__%d-%h-%Y'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open('logfile.txt', 'a', encoding='utf-8') as logging_file:
        logging_file.write(timestamp + ',' + message + '\n')
