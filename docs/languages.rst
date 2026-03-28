.. _sec-languages:

Languages
=========

GELATO's UI language controls all prompts, labels, and messages shown during quizzes.
The quiz content itself (German nouns, verbs, articles) is always in German -- the
language setting only affects the **interface**.

To change the UI language, set ``general.def_language`` in ``settings/settings.yml``
(see :ref:`sec-configuration`).

Supported Languages
-------------------

.. list-table::
   :header-rows: 1
   :widths: 15 20 65

   * - Code
     - Language
     - Notes
   * - ``en``
     - English
     - Default. All prompts are displayed in English.
   * - ``cn``
     - Chinese
     - Full translation of all prompts and labels.
   * - ``katze``
     - Cat mode
     - Every prompt is replaced with randomly generated "meow" strings
       of varying length, punctuated with ``?``, ``.``, ``!``, or ``??``.
       Intended as an easter egg.

Any other language code (e.g. ``fr``, ``it``, ``es``) will fall back to the
English text for any prompt that does not have a translation defined.

How Translations Work
---------------------

All UI strings are defined in ``language/dictionary.py``. The file contains a
dictionary called ``prompt_raw`` where each key is the English prompt text and
each value is a dictionary of translations keyed by language code:

.. code-block:: python

   prompt_raw = {
       'Hello': {
           'cn': '哈啰',
           'fr': 'Bonjour',
       },
       'Welcome to': {
           'cn': '欢迎使用',
       },
       # ... more prompts ...
   }

At startup, GELATO reads the configured language from ``settings.yml`` and builds
a flat lookup dictionary using ``build_prompt()``:

- **English (``en``):** Each key maps to itself (the English text *is* the key).
- **Cat mode (``katze``):** Each key maps to a random meow string.
- **Other languages:** Each key maps to its translation if available, otherwise
  falls back to the English key.

Adding a New Language
---------------------

To add support for a new language (e.g. French, ``fr``):

1. Open ``language/dictionary.py``.
2. For each entry in ``prompt_raw``, add your translation under a new language key:

   .. code-block:: python

      'Hello': {
          'cn': '哈啰',
          'fr': 'Bonjour',    # <-- add this
      },

3. You do not need to translate every prompt. Any missing translation will
   automatically fall back to the English text.
4. Set ``def_language: fr`` in ``settings/settings.yml`` to activate it.

No code changes are needed beyond adding the translation strings -- the
``build_prompt()`` function handles arbitrary language codes automatically.
