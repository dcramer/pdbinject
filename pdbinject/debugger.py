from __future__ import absolute_import

import pdb
import rpdb

from threading import Thread


class DebuggerThread(Thread):
    def run(self):
        pdb.set_trace()


class RemoteDebuggerThread(Thread):
    def __init__(self, address='127.0.0.1', port=4444):
        self.address = address
        self.port = port
        Thread.__init__(self)

    def run(self):
        debugger = rpdb.Rpdb(address=self.address, port=self.port)
        debugger.set_trace()
