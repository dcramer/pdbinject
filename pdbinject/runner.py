from __future__ import absolute_import

import os
import subprocess


def inject(pid, verbose=False, gdb_prefix='', rpdb_port=4444):
    """Executes a file in a running Python process."""
    gdb_cmds = [
        'PyGILState_Ensure()',
        'PyRun_SimpleString("'
            'import sys; sys.path.insert(0, \\"%s\\");'
            'from pdbinject.rdb import DebuggerThread;'
            'thread = DebuggerThread(port=%d);'
            'thread.daemon = True;'
            'thread.start();'
        '")' % (
            os.path.join(os.path.dirname(__file__), os.pardir),
            rpdb_port,
        ),
        'PyGILState_Release($1)',
    ]
    p = subprocess.Popen(
        '%sgdb -p %d -batch %s' % (
            gdb_prefix, pid,
            ' '.join(["-eval-command='call %s'" % cmd for cmd in gdb_cmds])),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = p.communicate()
    if verbose:
        print(out)
        print(err)

    if p.returncode == 0:
        print("Remote PDB has been configured on port %s" % (rpdb_port,))
        print("")
        print("  nc 127.0.0.1 %s" % (rpdb_port,))


def main():
    import sys
    assert len(sys.argv) == 2, 'Usage: pdbinject <pid>'
    inject(int(sys.argv[1]), verbose=True)


if __name__ == '__main__':
    main()
