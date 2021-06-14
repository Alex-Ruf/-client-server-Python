import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log=TimedRotatingFileHandler('log/client_log_config.log', when='midnight')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
log.setFormatter(formatter)

log.setLevel(logging.DEBUG)
logger.addHandler(log)


def errore(info):
    logger.error(info)

def info(info):
    logger.info(info)

def main(info):
    logger.debug(info)


if __name__ == '__main__':
    main()