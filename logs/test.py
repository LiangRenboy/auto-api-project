from logs.logsfile import logger

logger.warning('ws')


@logger.catch()
def add(a, b):
    return a + b


print(add(1, 't'))


logger.error('error!!!')

