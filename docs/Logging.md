# Logging
For logging code files, use the following code
```
import logging as log
LOG_FILENAME = 'main.log'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
LOG_LEVEL = log.DEBUG
log.basicConfig(filename=LOG_FILENAME, format=LOG_FORMAT, level=LOG_LEVEL)
```