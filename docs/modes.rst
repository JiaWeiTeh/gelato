.. _sec-modes:

Quiz Modes
==========

GELATO offers three quiz modes, accessible from the main menu. All modes begin by loading
the word database from the corresponding Excel file, and optionally letting you preview
the dictionary before the quiz starts.

At the end of every quiz, you are asked whether you would like to redo the exercise.

.. _sec-modes-artikel:

Article (Normal)
----------------

**Menu option:** ``1``

Practice assigning the correct German article (``der``, ``die``, or ``das``) to nouns.

**How it works:**

1. You are asked how many questions you would like (or press Enter for the maximum).
2. Nouns are presented in random order. For each noun, type the correct article.
3. Correct answers are silently accepted; incorrect answers are marked ``(Incorrect)``.
4. After all questions, any nouns you got wrong are **repeated** in a new round
   (re-shuffled). This continues until every noun has been answered correctly.
5. Your score is calculated based on the **first attempt only** and displayed as a
   count and percentage.
6. If you scored less than 100%, an analysis table is shown listing each wrong
   noun with its correct article and translation.
7. A perfect score triggers a congratulatory "you win" banner.

**Example flow:**

.. code-block:: text

   Apfel: der             <-- correct, moves on
   Lampe: der (Incorrect) <-- wrong, recorded
   Buch: das              <-- correct, moves on

   You scored 2 (66%).
   Here are the correct answers for the part(s) where you've made mistake(s):
   die  Lampe               [lamp]

   -- Round 2: only "Lampe" is asked again --
   Lampe: die               <-- correct this time, quiz ends

.. _sec-modes-challenge:

Article (Challenge)
-------------------

**Menu option:** ``2``

A survival variant of the article quiz. You start with a fixed number of hearts
(lives) and try to answer as many questions as possible.

**How it works:**

1. All nouns in the database are presented (no question-count selection).
2. Each noun is shown with a hearts display (e.g. ``♥ ♥ ♥``).
3. A correct answer moves to the next noun. An incorrect answer costs one heart
   and is marked ``(Incorrect)``.
4. The quiz ends when you either **run out of hearts** or **complete all nouns**.
5. Your survival score is calculated as: questions answered minus wrong answers.

**If you complete all nouns with hearts remaining:**

- A "you win" banner is displayed.
- Your score is shown and submitted to the scoreboard.

**If you run out of hearts:**

- Your score is shown and submitted to the scoreboard.
- An analysis table lists every noun you got wrong, with the correct article
  and translation.

**Hearts display:**

.. code-block:: text

   ♥ ♥ ♥    Apfel: der        <-- correct
   ♥ ♥ ♥    Lampe: der        <-- wrong
   ♡ ♥ ♥    Buch: das         <-- correct (one heart lost)

The number of hearts is configured in ``settings.yml`` (see :ref:`sec-configuration`).
The default is 3, with a maximum of 10.

**Scoreboard:**

High scores are saved to a local CSV file. The top three scores are displayed after
each game. If your score qualifies, you are prompted for a username (max 10 characters).
See :ref:`sec-scoreboard` for details.

.. _sec-modes-verben:

Verben (Practice)
-----------------

**Menu option:** ``3``

Practice German verb conjugations by filling in different verb forms.

**How it works:**

1. You are asked how many verbs you would like to practise (or press Enter for all).
2. For each verb, the infinitive and its meaning are displayed in bold.
3. You are then prompted to fill in each conjugation form:

   - **Prasens** (present tense)
   - **Prateritum** (simple past)
   - **Perfekt** (present perfect)
   - **Beispielsatz** (example sentence) -- shown for reference, not scored

4. After you type each answer, the correct answer is revealed next to yours,
   along with a mark:

   - |checkmark| -- your answer matched (case-insensitive, whitespace-trimmed)
   - |crossmark| -- your answer did not match

5. At the end, your score is displayed as a count and percentage of correct
   conjugation fields (example sentences are excluded from scoring).

**Example flow:**

.. code-block:: text

   Your verb is: GEHEN (to go)
   ➳ Prasens: geht [geht] ✓
   ➳ Prateritum: gang [ging] ✗
   ➳ Perfekt: ist gegangen [ist gegangen] ✓
   ➳ Beispielsatz: I go to school
     [Ich gehe in die Schule.]

   You scored 2 (66%).

.. |checkmark| unicode:: U+2713
.. |crossmark| unicode:: U+2717
