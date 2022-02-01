import coloredlogs
import logging


def init_logger():
    """
    A simple function which initializes the custom colored logger.

        """
    # Create a logger object.
    logger = logging.getLogger(__name__)

    # By default the install() function installs a handler on the root logger,
    # this means that log messages from your code and log messages from the
    # libraries that you use will all show up on the terminal.
    coloredlogs.install(level='DEBUG')

    # If you don't want to see log messages from libraries, you can pass a
    # specific logger object to the install() function. In this case only log
    # messages originating from that logger will show up on the terminal.
    coloredlogs.install(level='DEBUG', logger=logger)

    coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'hostname': {'color': 'magenta'},
                                        'levelname': {'bold': True, 'color': 'blue'}, 'name': {'color': 'blue'},
                                        'programname': {'color': 'cyan'}, 'username': {'color': 'yellow'},
                                        'fileName': {'color': 'yellow'}, 'funcName': {'color': 'cyan'}}

    coloredlogs.install(fmt='[%(asctime)s] [%(hostname)s] [%(filename)s] [%(funcName)s()] [Line %(lineno)d] [%('
                            'levelname)s] - %(message)s')
    return logger
