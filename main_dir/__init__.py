from .celery_config import debug_task as dbk  # Importing the debug_task from celery_config module and renaming it to dbk

# Defining the public API of the module by specifying the names to be exported when 'import *' is used
__all__ = ('dbk',)  # Only 'dbk' will be exported when importing * from this module
