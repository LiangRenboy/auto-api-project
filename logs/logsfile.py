from loguru import logger


logger.add('run.log',
           filter='',
           level='INFO',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8'
           )