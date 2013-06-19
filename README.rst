Install
=======

You'll need GDB compiled with python support, and the ``pdbinject`` package:

::

	easy_install install pdbinject


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
