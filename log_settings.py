
ERROR_LOG_FILENAME = ".weather-errors.log"
ALL_LOG_FILENAME = ".weather-debug.log"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d " "%(levelname)s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(message)s",
        },
        "json": {  # The formatter name
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",  # The class to instantiate!
            # Json is more complex, but easier to read, display all attributes!
            "format": """
                asctime: %(asctime)s
                created: %(created)f
                filename: %(filename)s
                funcName: %(funcName)s
                levelname: %(levelname)s
                levelno: %(levelno)s
                lineno: %(lineno)d
                message: %(message)s
                module: %(module)s
                msec: %(msecs)d
                name: %(name)s
                pathname: %(pathname)s
                process: %(process)d
                processName: %(processName)s
                relativeCreated: %(relativeCreated)d
                thread: %(thread)d
                threadName: %(threadName)s
                exc_info: %(exc_info)s
            """,
            "datefmt": "%Y-%m-%d %H:%M:%S",  # How to display dates
        },
    },
    "handlers": {
        "logfile": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "filename": ERROR_LOG_FILENAME,
            "formatter": "default",
            "backupCount": 2,
        },
        "verbose_output": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            # "formatter": "json",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "all_logfile": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": ALL_LOG_FILENAME,
            "formatter": "default",
            "backupCount": 2,
        },
    },
    "loggers": {
        "weather": {
            "level": "INFO",
            "handlers": [
                "verbose_output",
            ],
        },
    },
    "root": {"level": "DEBUG", "handlers": [
        # "logfile",
        "verbose_output",
        "all_logfile",
    ]},
}
