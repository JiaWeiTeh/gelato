.. _sec-scoreboard:

Scoreboard
==========

The scoreboard tracks the top three high scores for the Article (Challenge) mode.
It is stored locally as a CSV file and displayed after each challenge game.

How It Works
------------

1. After completing (or losing) an Article (Challenge) game, your survival score
   is calculated: **questions answered correctly** (total answered minus wrong answers).
2. If your score is higher than any of the current top three, or fewer than three
   scores exist, you are prompted for a username.
3. The scoreboard is updated and the top three are displayed in a formatted table.

**Username rules:**

- Must not be empty.
- Maximum 10 characters (whitespace is trimmed).

Scoreboard Display
------------------

After each challenge game, the scoreboard is shown as a table:

.. code-block:: text

   Here are the top three high scores:
   ╒═════════╤════════╤══════════════╕
   │ Score   │ User   │ Date         │
   ╞═════════╪════════╪══════════════╡
   │ 42 pts  │ Anna   │ 15/03/2026   │
   ├─────────┼────────┼──────────────┤
   │ 38 pts  │ Max    │ 12/03/2026   │
   ├─────────┼────────┼──────────────┤
   │ 25 pts  │ Lena   │ 01/03/2026   │
   ╘═════════╧════════╧══════════════╛

File Location
-------------

Scoreboard data is stored in the ``data/`` directory:

- **Article (Challenge):** ``data/artikel_scoreboard.csv``

The file is created automatically on your first high score. It is a plain CSV
with three columns (no header row):

.. code-block:: text

   42 pts,Anna,15/03/2026
   38 pts,Max,12/03/2026
   25 pts,Lena,01/03/2026

These files are listed in ``.gitignore`` and are not tracked by version control,
so each user maintains their own local scoreboard.

Resetting the Scoreboard
------------------------

To reset the scoreboard, simply delete the corresponding CSV file:

.. code-block:: console

   $ rm data/artikel_scoreboard.csv

A new scoreboard will be created the next time you achieve a qualifying score.
