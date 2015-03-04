Install
=======

You'll need GDB compiled with python support, and the ``pdbinject`` package:

::

	easy_install pdbinject


OS X Notes
----------

The default GDB does not come compiled with Python support.

Homebrew fixes that:

::

	brew install gdb

.. note:: There's more steps, I gave up on figuring out how to make it work.


Usage
=====

::

	$ python example/loop.py &
	Process running with PID 6319

	$ sudo pdbinject 6319
	Remote PDB has been configured on port 4444

  		nc 127.0.0.1 4444

  	$ nc 127.0.0.1 4444
	--Return--
	> /home/ubuntu/pdbinject/pdbinject/debugger.py(16)run()->None
	-> debugger.set_trace()

Now have some fun:

::

	from guppy import hpy
	hp = hpy()
	heap = hp.heap()
	heap.get_rp()

To print the stacktrace across all the threads:

::

	import sys, traceback
	for thread_id, stack in sys._current_frames().iteritems(): print 'Thread id: %s\n%s' % (thread_id, ''.join(traceback.format_stack(stack)))
