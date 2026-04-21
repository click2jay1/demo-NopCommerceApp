# import logging
#
# class LogGeneration:
#
#     @staticmethod
#     def loggen(test_name):
#         logging.basicConfig(filename=f".\\Logs\\automation_{test_name}.log",
#                             format='%(asctime)s.%(msecs)03d: [%(levelname)s]: %(message)s',
#                             datefmt='%y-%m-%d %H:%M:%S',
#                             level=logging.INFO
#                             )
#
#         logger = logging.getLogger()
#         return logger

import logging
import os

class LogGeneration:

    @staticmethod
    def loggen(test_name):
        os.makedirs("Logs", exist_ok=True)

        log_file = f".\\Logs\\automation_{test_name}.log"

        logger = logging.getLogger(test_name)
        logger.setLevel(logging.INFO)

        # Avoid duplicate handlers
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)

            formatter = logging.Formatter(
                '%(asctime)s.%(msecs)03d: [%(levelname)s]: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger