.. _sec-configuration:

Configuration
=============

GELATO is configured through a YAML file located at ``settings/settings.yml``.
You can edit it directly, or open it from within GELATO by selecting **mode 4 (Settings)**
from the main menu -- this launches your default text editor (set via the ``EDITOR``
environment variable; defaults to ``nano``).

Below is the full configuration reference.

Configuration File
------------------

.. code-block:: yaml

   general:
       name: User
       def_language: en

   artikel_normal:
       def_qs: null

   artikel_challenge:
       hearts: 3

General
-------

``general.name``
   Your display name, shown in the welcome banner. Maximum 10 characters
   (longer names are truncated). Set to ``null`` to hide the greeting.

   - **Type:** string or ``null``
   - **Default:** ``User``

``general.def_language``
   The UI language for all prompts and messages. This does **not** affect the
   quiz content (which is always in German).

   - **Type:** string
   - **Default:** ``en``
   - **Available values:**

     - ``en`` -- English
     - ``cn`` -- Chinese
     - ``katze`` -- Cat mode (all prompts replaced with meows)

   See :ref:`sec-languages` for details on language support.

Artikel (Normal Mode)
---------------------

``artikel_normal.def_qs``
   The default number of questions for Article (Normal) mode. If the value
   exceeds the number of nouns in the database, it is clamped to the maximum.

   - **Type:** positive integer or ``null``
   - **Default:** ``null`` (asks all available questions)

Artikel (Challenge Mode)
------------------------

``artikel_challenge.hearts``
   The number of hearts (lives) you start with in Article (Challenge) mode.
   Each incorrect answer costs one heart. The quiz ends when all hearts are lost.

   - **Type:** positive integer
   - **Default:** ``3``
   - **Range:** 1 -- 10 (values outside this range are clamped)
