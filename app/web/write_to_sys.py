"""
async module for logging platform data
"""

import asyncio
# arrow is a better solution for datetime in python
from arrow import utcnow


async def default_to_uk_time(region: str='', custom_format: str='') -> str:
    '''
    format datetime object to string
    accepts 2 possible arguments
    datetime defaults to London time
    rtype -> str
    '''
    def utc_time():
        return utcnow()

    def local_time():
        if region is '':
            return utc_time().to('Europe/London')
        else:
            return utc_time().to(region)

    def formatted_local_time():
        if custom_format is '':
            return local_time().format("MMM DD YYYY HH:mm:ss")
        else:
            return local_time().format(custom_format)

    return formatted_local_time()


async def send_alert(members_on_duty):
    '''
    TODO: send error log alerts to members on duty
    '''
    # placeholder function
    pass


async def day_of_log_file() -> str:
    '''
    generates the log file based on date
    stores log file under the local log directory
    default format: "MMM DD YYYY"
    accepts NO arguments
    rtype -> str
    '''
    region = ''
    day_format = "MMM DD YYYY"
    return f'../logs/{await default_to_uk_time(region, day_format)}.log'


async def time_of_log() -> str:
    '''
    generates the log entry time for each entry
    default format: "MMM DD YYYY HH:mm:ss"
    accepts NO arguments
    rtype -> str
    '''
    return await default_to_uk_time()


async def log_to_file(content):
    '''
    generates the log file
    accepts ONE argument
    example:
    Oct 28 2018 17:01:22 file.py[2011] func: [INFO]: We have some info
    rtype -> None
    '''
    with open(await day_of_log_file(), 'a') as f:
        f.write(f'{await time_of_log()}\t')
        f.write(f'{content.file_name}')
        f.write(f'[{content.pid}] ')
        f.write(f'{content.func}\t')
        f.write(f'[{content.process}]: ')
        f.write(f'{content.log}')
    f.close()


async def retrieve_current_log(log_date: str='') -> str:
    '''
    retrieve a log file
    defaults to the current date
    accepts ONE argument
    rtype -> None
    '''
    log_file_contents = ''

    if log_date is '':
        log_dir = await day_of_log_file()
    else:
        log_dir = f'../logs/{log_date}.log'

    with open(log_dir, 'r') as f:
        log_file_contents = f.read()
    f.close()

    return log_file_contents