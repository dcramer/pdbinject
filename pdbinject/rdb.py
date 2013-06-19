from __future__ import absolute_import

import rpdb

from threading import Thread


class DebuggerThread(Thread):
    def __init__(self, port=4444):
        self.port = port
        Thread.__init__(self)

    def run(self):
        debugger = rpdb.Rpdb(self.port)
        debugger.set_trace()
