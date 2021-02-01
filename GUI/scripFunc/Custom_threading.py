from threading import Thread
from typing import Any


def NewThread(com, Returning: bool, thread_ID, *arguments) -> Any:
    """
    Will create a new thread for a function/command.

    :param com: Command to be Executed
    :param Returning: True/False Will the command return anything?
    :param thread_ID: Name of thread
    :param arguments: Arguments to be sent to Command

    """
    
    class NewThreadWorker(Thread):
        def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *,
                     daemon=None):
            Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
            self.daemon = True
            self._return = None
        
        def run(self):
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        
        def joinThread(self):
            Thread.join(self)
            return self._return
    
    ntw = NewThreadWorker(target=com, name=thread_ID, args=(*arguments,))
    if Returning:
        ntw.start()
        return ntw.joinThread()
    else:
        ntw.start()


