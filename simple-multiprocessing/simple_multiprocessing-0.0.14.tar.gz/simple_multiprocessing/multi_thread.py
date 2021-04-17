# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from threading import Thread

# Local
from ._multi_task import _MultiTask

# -------------------------------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------ class: MultiThread ------------------------------------------------------ #

class MultiThread(_MultiTask):

    def _proc_cls(self) -> type:
        return Thread


# -------------------------------------------------------------------------------------------------------------------------------- #