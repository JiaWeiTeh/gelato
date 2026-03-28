.. _sec-contributing:

Contributing
============

Thank you for your interest in contributing to GELATO! This page describes the
project structure and how to set up a development environment.

Development Setup
-----------------

1. Clone the repository:

   .. code-block:: console

      $ git clone https://github.com/JiaWeiTeh/gelato.git
      $ cd gelato

2. Create and activate a virtual environment (recommended):

   .. code-block:: console

      $ python -m venv venv
      $ source venv/bin/activate     # Linux/macOS
      $ venv\Scripts\activate        # Windows

3. Install dependencies in development mode:

   .. code-block:: console

      $ pip install -e .

4. Run GELATO to verify everything works:

   .. code-block:: console

      $ python gelato.py

Dependencies
------------

Runtime dependencies (installed via ``pip install .``):

- ``numpy`` -- array operations, shuffling, scoring
- ``pandas`` -- Excel file loading, CSV reading, scoreboard display
- ``tabulate`` -- formatted table output in the terminal
- ``openpyxl`` -- Excel ``.xlsx`` file support (used by pandas)
- ``pyyaml`` -- YAML configuration file parsing

Documentation dependencies (for building the docs):

- ``sphinx``
- ``sphinx_rtd_theme``
- ``sphinx_copybutton``
- ``sphinxemoji``
- ``readthedocs-sphinx-search``

These are listed in ``docs/requirements.txt`` and are installed automatically
by ReadTheDocs.

Project Structure
-----------------

.. code-block:: text

   gelato/
   ├── gelato.py                   # Main entry point
   ├── setup.py                    # Package setup and entry point
   ├── requirements.txt            # Runtime dependencies
   │
   ├── artikel/                    # Article quiz module
   │   ├── artikel.py              #   Quiz runner (load, preview, loop)
   │   └── artikel_functions.py    #   Quiz logic (QnA, scoring, analysis)
   │
   ├── verben/                     # Verb conjugation module
   │   ├── verben.py               #   Quiz runner (load, preview, loop)
   │   └── verben_functions.py     #   Quiz logic (QnA, scoring)
   │
   ├── functions/                  # Shared utilities
   │   ├── common.py               #   Shared helpers (load_excel, randomiser, etc.)
   │   ├── header.py               #   Welcome banner and mode selection menu
   │   ├── footer.py               #   Win banner
   │   ├── query.py                #   Yes/no input helper
   │   └── terminal_prints.py      #   ANSI colour/style constants
   │
   ├── scoreboard/
   │   └── scoreboard.py           # High score tracking (top 3, CSV storage)
   │
   ├── settings/
   │   ├── settings.py             # YAML config loader and editor launcher
   │   └── settings.yml            # User configuration file
   │
   ├── language/
   │   └── dictionary.py           # UI translations (prompt_raw + build_prompt)
   │
   ├── data/                       # Word databases and generated files
   │   ├── artikel.xlsx            #   Article quiz source data (user-editable)
   │   ├── verben.xlsx             #   Verb quiz source data (user-editable)
   │   ├── daily_words.xlsx        #   Reserved for future use
   │   ├── *.csv                   #   Auto-generated at runtime (gitignored)
   │   └── *_scoreboard.csv        #   User scores (gitignored)
   │
   └── docs/                       # Sphinx documentation (this site)
       ├── conf.py
       ├── index.rst
       └── *.rst

How It All Fits Together
------------------------

.. code-block:: text

   gelato.py
     │
     ├── settings.get_param()          Load settings.yml
     ├── header.display()              Show welcome banner
     └── header.mode_selection()       Show menu, dispatch to:
           │
           ├── artikel.run()           Article quiz (Normal or Challenge)
           │     ├── load_file()         Excel → CSV via common.load_excel()
           │     ├── qna_section()       Run quiz, compute score
           │     └── scoreboard.*()      Update/show high scores (Challenge only)
           │
           ├── verben.run()            Verb quiz (Practice)
           │     ├── load_file()         Excel → CSV via common.load_excel()
           │     └── qna_section()       Run quiz, compute score
           │
           └── settings.edit_param()   Open settings.yml in $EDITOR

Key design notes:

- **Excel → CSV pipeline:** Each quiz module calls ``common.load_excel()`` which
  reads the ``.xlsx`` file and writes a ``.csv`` to ``data/``. The quiz logic then
  reads the CSV via ``numpy.genfromtxt`` for array-based operations.
- **Translation system:** ``language/dictionary.py`` exports a module-level ``prompt``
  dict that is initialised once at import time. All modules import ``prompt`` and use
  English keys as lookup keys.
- **No database:** All data is file-based (Excel for word data, CSV for scoreboards).
  There is no database dependency.

Building the Documentation
--------------------------

To build the docs locally:

.. code-block:: console

   $ pip install -r docs/requirements.txt
   $ cd docs
   $ make html

The built HTML will be in ``docs/_build/html/``. Open ``index.html`` to preview.

The documentation is also hosted on `ReadTheDocs <https://readthedocs.org/>`_ and
builds automatically on push.
