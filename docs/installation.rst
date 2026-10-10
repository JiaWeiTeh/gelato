.. _sec-installation:

Installation
============

Requirements
------------

- Python 3.9 or later
- pip (Python package manager)

GELATO depends on the following packages:

- ``numpy``
- ``pandas``
- ``tabulate``
- ``openpyxl``
- ``pyyaml``

Download
--------

GELATO is available at `https://github.com/JiaWeiTeh/gelato <https://github.com/JiaWeiTeh/gelato>`_.
The easiest way to get a copy is via `git <https://git-scm.com/>`_:

.. code-block:: console

   $ git clone https://github.com/JiaWeiTeh/gelato.git
   $ cd gelato

Alternatively, download the ZIP from the GitHub page ("Code" > "Download ZIP") and unpack it.

Install
-------

Install the dependencies with pip (a virtual environment is recommended):

.. code-block:: console

   $ pip install -r requirements.txt

Optionally, install GELATO itself in editable mode. This adds a ``gelato``
command that you can run from any directory:

.. code-block:: console

   $ pip install -e .

GELATO reads its word lists and settings from the project folder, so keep the
folder where it is after installing.

Run
---

From the project folder:

.. code-block:: console

   $ python gelato.py

Or, if you installed it with ``pip install -e .``:

.. code-block:: console

   $ gelato
