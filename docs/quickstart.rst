.. _sec-quickstart:

Quick Start
===========

Once you have GELATO installed (see :ref:`sec-installation`), you can start it by running:

.. code-block:: console

   $ python gelato.py

You will be greeted with a welcome screen and a list of available modes:

.. code-block:: text

   1: Article
   2: Article (Challenge)
   3: Verben (Practice)
   4: Settings
   0: Exit

   Enter quiz mode (number):

Enter the number corresponding to the mode you want to try. Here is a quick overview:

- **Mode 1 -- Article**: Practice German noun articles (der/die/das). You can optionally preview the word database before starting. Wrong answers are repeated until you get them all right, and you receive a score at the end.

- **Mode 2 -- Article (Challenge)**: A survival variant of the article quiz. You start with a limited number of hearts (lives). Each wrong answer costs a heart. Run out of hearts and the game is over. High scores are saved to the scoreboard.

- **Mode 3 -- Verben (Practice)**: Practice German verb conjugations. You are given a verb and asked to fill in its forms (Prasens, Prateritum, Perfekt). Each answer is checked and marked right or wrong, with a score shown at the end.

- **Mode 4 -- Settings**: Opens the configuration file in your default text editor so you can change your name, UI language, default question count, and number of hearts.

To quit GELATO at any time, press ``Ctrl+C``.

For a detailed breakdown of each mode, see :ref:`sec-modes`.
For configuration options, see :ref:`sec-configuration`.
