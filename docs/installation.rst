.. _sec-installation:

Installation
============

Requirements
------------

- Python 3.8 or later
- pip (Python package manager)

GELATO depends on the following packages (installed automatically via ``pip``):

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

Install
-------

Install GELATO and its dependencies with pip:

.. code-block:: console

   $ pip install .

Or, if you prefer to install in development mode (editable):

.. code-block:: console

   $ pip install -e .

You can also install dependencies directly without installing the package:

.. code-block:: console

   $ pip install -r requirements.txt

Run
---

After installation, run GELATO from the project root:

.. code-block:: console

   $ python gelato.py

Or, if installed via ``pip install``:

.. code-block:: console

   $ gelato
