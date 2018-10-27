.. highlight:: shell

============
Installation
============

Use directly
------------
Clone the repository

.. code-block::console

    $ git clone git://github.com/qytz/finchan_exts

Edit you finchan configuration, change the item below::

    ext_manager:
        ext_path: ~/finchan_exts

Change the ext_path item to you dirctory, then use the `extensions` with `finchan <https://github.com/qytz/finchan>`_.


Stable release
--------------

To install finchan, run this command in your terminal:

.. code-block:: console

    $ pip install finchan

This is the preferred method to install finchan, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for finchan can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/qytz/finchan

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/qytz/finchan/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

.. _Github repo: https://github.com/qytz/finchan_exts
.. _tarball: https://github.com/qytz/finchan_exts/tarball/master
