from loguru import logger
import os


info_logs = os.path.dirname(__file__) + '\\info.log'
error_logs = os.path.dirname(__file__) + '\\error.log'
logger.add(info_logs,
           filter=lambda x: x['level'].name > 'ERROR',
           level='INFO',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
logger.add(error_logs,
           filter='',
           level='ERROR',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
