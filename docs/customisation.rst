.. _sec-customisation:

Customisation
=============

GELATO loads its quiz data from Excel (``.xlsx``) files stored in the ``data/`` directory.
You can edit these files to add, remove, or modify words and verbs. At startup, each
Excel file is automatically converted to a CSV for internal use -- you only ever need
to edit the ``.xlsx`` files.

.. _sec-customisation-artikel:

Article Database (``artikel.xlsx``)
-----------------------------------

This file powers the Article (Normal) and Article (Challenge) quiz modes.

**Location:** ``data/artikel.xlsx``

**Columns:**

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Column
     - Example
     - Description
   * - ``Artikel``
     - ``das``
     - The correct German article (``der``, ``die``, or ``das``).
   * - ``Noun``
     - ``Kind``
     - The German noun (capitalised, without article).
   * - ``Meaning``
     - ``Child``
     - English translation of the noun.
   * - ``Tag``
     - ``Familie``
     - A category tag for the noun (e.g. ``Familie``, ``Essen``, ``Reise``).
       Used for display in the dictionary preview.

**Example rows:**

.. code-block:: text

   Artikel  | Noun       | Meaning   | Tag
   ---------+------------+-----------+---------
   das      | Kind       | Child     | Familie
   die      | Kinder     | Children  | Familie
   der      | Bruder     | Brother   | Familie
   die      | Schwester  | Sister    | Familie

**Tips:**

- The ``Artikel`` column is the **answer** the user must type. Make sure it is
  exactly ``der``, ``die``, or ``das`` (lowercase).
- The ``Tag`` column is only used in the dictionary preview table. You can use
  any category name you like.
- You can have as many rows as you want. The quiz will use all of them (or a
  user-selected subset in Normal mode).

.. _sec-customisation-verben:

Verb Database (``verben.xlsx``)
-------------------------------

This file powers the Verben (Practice) quiz mode.

**Location:** ``data/verben.xlsx``

**Columns:**

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Column
     - Example
     - Description
   * - ``Infinitiv``
     - ``abfahren:depart``
     - The verb infinitive and its English meaning, separated by a colon (``:``).
   * - ``Prasens (er/sie/es)``
     - ``fahrt ab``
     - Present tense conjugation (3rd person singular).
   * - ``Prateritum``
     - ``fuhr ab``
     - Simple past tense.
   * - ``Perfekt``
     - ``ist abgefahren``
     - Present perfect form (with auxiliary verb).
   * - ``Beispielsatz``
     - ``Der Bus fahrt um 09.12 Uhr ab.``
     - An example sentence using the verb. This field is shown for reference
       but is **not scored** during the quiz.

**Example rows:**

.. code-block:: text

   Infinitiv          | Prasens   | Prateritum | Perfekt          | Beispielsatz
   -------------------+-----------+------------+------------------+----------------------------
   abfahren:depart    | fahrt ab  | fuhr ab    | ist abgefahren   | Der Bus fahrt um 09.12 Uhr ab.
   abfliegen:lift off | fliegt ab | flog ab    | ist abgeflogen   | Das Flugzeug ist ...
   abgeben:hand in    | gibt ab   | gab ab     | hat abgegeben    | Wir gaben Flaschen ...

**Important:**

- The ``Infinitiv`` column **must** contain a colon separating the verb from its
  meaning (e.g. ``gehen:to go``). This is how GELATO splits the display.
- Example sentences may contain commas -- GELATO handles this correctly.
- All conjugation fields are checked case-insensitively during the quiz.

.. _sec-customisation-adding:

Adding a New Word Database
--------------------------

Currently, GELATO supports two built-in quiz types (articles and verbs). To add
more words, simply edit the corresponding ``.xlsx`` file in the ``data/`` directory.

The generated ``.csv`` files in ``data/`` are rebuilt automatically each time you
start a quiz -- you do not need to create or edit them manually.
