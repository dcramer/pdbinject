#!/usr/bin/env python

from __future__ import absolute_import, print_function

import os
import sys
import subprocess
import tempfile
import textwrap
import optparse


def inject(pid, debugger,
    rpdb_addr='127.0.0.1',
    rpdb_port=4444):
    """Executes a file in a running Python process."""
    # TODO: rpdb stuff

    with tempfile.NamedTemporaryFile() as f:
        s = textwrap.dedent("""\
        import time, sys;
        sys.path.append('%(path)s');
        from pdbinject.debugger import RemoteDebuggerThread;
        thread = RemoteDebuggerThread('%(rpdb_addr)s', %(rdpb_port)d);
        thread.start();
        time.sleep(1);
        """ % dict(
            path=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
            rpdb_addr=rpdb_addr,
            rdpb_port=rpdb_port,
        ))

        if debugger == 'gdb':
            print('call PyGILState_Ensure()', file=f)
            print('call PyRun_SimpleString("%s")' % s.replace('\n','').replace('"', '\\"'), file=f)
            print('call PyGILState_Release($1)', file=f)

            args = ['gdb', '-p', str(pid), '--batch', '--command', f.name]
        elif debugger == 'lldb':
            print('call (PyGILState_STATE)PyGILState_Ensure()', file=f)
            print('call (int)PyRun_SimpleString("%s")' % s.replace('\n','').replace('"', '\\"'), file=f)
            print('call (void)PyGILState_Release($0)', file=f)
            print('exit', file=f)

            args = ['lldb', '-p', str(pid), '-s', f.name]
        else:
            raise ValueError('unknown debugger')

        f.flush()

        with open(os.devnull) as stdin:
            subprocess.check_call(args,
                close_fds=True,
                stdin=stdin)

        print("Remote PDB has been configured on port %s" % rpdb_port)
        print("")
        print("  nc %s %s" % (rpdb_addr, rpdb_port,))


def main():
    parser = optparse.OptionParser('usage: %prog [options] pid')
    parser.add_option('--address',
            default='127.0.0.1',
            help='address to launch the server on')
    parser.add_option('-p', '--port',
            default=4444,
            type='int',
            help='port to launch pdb on')

    if os.uname()[0] == 'Darwin':
      default_debugger = 'lldb'
    else:
      default_debugger = 'gdb'

    parser.add_option('-d', '--debugger',
            default=default_debugger,
            choices=('gdb', 'lldb'),
            help='which debugger to use to attach to the process (gdb on linux, lldb on OS X)')

    options, args = parser.parse_args()

    if len(args) != 1:
        print('pid not specified', file=sys.stderr)
        return 1

    try:
        pid = int(args[0])
    except TypeError:
        print('pid must be an integer', file=sys.stderr)
        return 1

    inject(pid, options.debugger,
        rpdb_addr=options.address,
        rpdb_port=options.port)

    return 0


if __name__ == '__main__':
    sys.exit(main())
