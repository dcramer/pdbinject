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


Usage
=====

::

	$ python loop.py &
	Process running with PID 6319

	$ pdbinject 6319
