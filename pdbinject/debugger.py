from __future__ import absolute_import

from .rpdb import Rpdb

from threading import Thread


class RemoteDebuggerThread(Thread):
    def __init__(self, addr='127.0.0.1', port=4444):
        self.addr = addr
        self.port = port
        Thread.__init__(self)

    def run(self):
        debugger = Rpdb(addr=self.addr, port=self.port)
        debugger.set_trace()
