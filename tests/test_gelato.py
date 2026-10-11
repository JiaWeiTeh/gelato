#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:49:12 2026

@author: Jia Wei Teh

Tests for GELATO. Run with: pytest
"""

import ast
import importlib
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parent.parent
CODE = [ROOT / 'gelato.py'] + [p for folder in ['artikel', 'functions', 'language', 'scoreboard', 'settings', 'verben'] for p in (ROOT / folder).glob('*.py')]

# a config like the one from settings.yml
config = SimpleNamespace(general=SimpleNamespace(name='User', def_language='en'),
                         artikel_normal=SimpleNamespace(def_qs=None),
                         artikel_challenge=SimpleNamespace(hearts=3))


def feed(monkeypatch, answers):
    # pretend the user types these answers, one after the other
    answers = iter(answers)
    monkeypatch.setattr('builtins.input', lambda question='': next(answers))


def article_answers(correct, wrong=(), name='Tester'):
    # answer the article quiz by reading the noun from the question
    def fake_input(question=''):
        if 'username' in question:
            return name
        noun = re.search(r'(\S+): $', question).group(1)
        return 'xxx' if noun in wrong else correct[noun]
    return fake_input


# ---------------- word lists and settings ----------------

def test_word_lists_load():
    from functions.common import load_excel
    artikel = load_excel('artikel.xlsx')
    assert list(artikel.columns)[:2] == ['Artikel', 'Noun']
    assert set(artikel['Artikel']) <= {'der', 'die', 'das'}
    assert (artikel['Noun'] != '').all()
    verben = load_excel('verben.xlsx')
    assert verben.shape[1] == 5


def test_excel_with_commas_and_empty_cells(tmp_path, monkeypatch):
    import functions.common as common
    data = pd.DataFrame([['das', 'Kind', 'Child, kid', None], [' die ', 'Lampe', 'Lamp', 'Haus']],
                        columns=['Artikel', 'Noun ', 'Meaning', 'Tag'])
    data.to_excel(tmp_path / 'test.xlsx', index=False)
    monkeypatch.setattr(common, 'DATA_DIR', tmp_path)
    loaded = common.load_excel('test.xlsx')
    assert list(loaded.columns) == ['Artikel', 'Noun', 'Meaning', 'Tag']
    assert loaded.iloc[0].tolist() == ['das', 'Kind', 'Child, kid', '']
    assert loaded.iloc[1, 0] == 'die'


def test_settings_fall_back_to_defaults(tmp_path, monkeypatch):
    import settings.settings as settings
    settings_file = tmp_path / 'settings.yml'
    monkeypatch.setattr(settings, 'settings_path', settings_file)

    settings_file.write_text('', encoding='utf-8')
    c = settings.get_param()
    assert (c.general.name, c.general.def_language, c.artikel_normal.def_qs, c.artikel_challenge.hearts) == ('User', 'en', None, 3)

    settings_file.write_text('general:\n    name: 12345\nartikel_normal:\n    def_qs: max\nartikel_challenge:\n    hearts: lots\n', encoding='utf-8')
    c = settings.get_param()
    assert (c.general.name, c.artikel_normal.def_qs, c.artikel_challenge.hearts) == ('12345', None, 3)

    settings_file.write_text('general:\n    name: null\nartikel_normal:\n    def_qs: 5\n', encoding='utf-8')
    c = settings.get_param()
    assert (c.general.name, c.artikel_normal.def_qs) == (None, 5)


# ---------------- translations ----------------

def test_every_prompt_used_in_the_code_exists():
    from language.dictionary import prompt_raw
    missing = []
    for path in CODE:
        for node in ast.walk(ast.parse(path.read_text(encoding='utf-8'))):
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                name = node.value.id if isinstance(node.value, ast.Name) else getattr(node.value, 'attr', None)
                if name == 'prompt' and node.slice.value not in prompt_raw:
                    missing.append((path.name, node.slice.value))
    assert missing == []


def test_translations_keep_their_placeholders():
    from language.dictionary import prompt_raw
    for key, translations in prompt_raw.items():
        for language, text in translations.items():
            assert text.count('%s') == key.count('%s'), (key, language)


def test_katze_mode_can_fill_in_numbers(monkeypatch):
    import settings.settings as settings
    import language.dictionary as dictionary
    katze = SimpleNamespace(general=SimpleNamespace(name='User', def_language='katze'))
    monkeypatch.setattr(settings, 'get_param', lambda: katze)
    try:
        importlib.reload(dictionary)
        for key, text in dictionary.prompt.items():
            assert 'Meo' in text
            text % tuple(['1'] * key.count('%s'))
    finally:
        monkeypatch.undo()
        importlib.reload(dictionary)


# ---------------- quiz logic ----------------

def test_number_of_questions(monkeypatch):
    from functions.common import set_number
    feed(monkeypatch, [''])
    assert set_number(10) == 10
    feed(monkeypatch, [''])
    assert set_number(10, 4) == 4
    feed(monkeypatch, ['999'])
    assert set_number(10) == 10
    feed(monkeypatch, ['abc', '-1', '3'])
    assert set_number(10) == 3


def test_survival_counts_every_question(monkeypatch):
    from artikel import artikel_functions
    questions = np.array(['Kind', 'Lampe', 'Buch'])
    answers = np.array(['das', 'die', 'das'])
    monkeypatch.setattr('builtins.input', article_answers(dict(zip(questions, answers))))
    _, wrong, hearts, answered = artikel_functions.ask_question_survival(questions, answers, [], [], 3, 3)
    assert (len(wrong), hearts, answered) == (0, 3, 3)
    monkeypatch.setattr('builtins.input', article_answers(dict(zip(questions, answers)), wrong=set(questions)))
    _, wrong, hearts, answered = artikel_functions.ask_question_survival(questions, answers, [], [], 2, 2)
    assert (len(wrong), hearts, answered) == (2, 0, 2)


def test_challenge_win_still_shows_mistakes(tmp_path, monkeypatch, capsys):
    from artikel import artikel_functions
    from scoreboard import scoreboard
    words = pd.DataFrame([['das', 'Kind', 'Child', ''], ['die', 'Lampe', 'Lamp', ''], ['das', 'Buch', 'Book', '']],
                         columns=['Artikel', 'Noun', 'Meaning', 'Tag'])
    monkeypatch.setattr(artikel_functions, 'load_file', lambda: words)
    monkeypatch.setattr(scoreboard, 'DATA_DIR', tmp_path)
    monkeypatch.setattr('builtins.input', article_answers({'Kind': 'das', 'Lampe': 'die', 'Buch': 'das'}, wrong={'Lampe'}))
    artikel_functions.qna_section(config, survival=True)
    out = capsys.readouterr().out
    assert 'Here are the correct answers' in out
    assert 'Lampe' in out and '[Lamp]' in out


def test_verbs_keep_eszett_and_work_without_meaning(monkeypatch, capsys):
    from verben import verben_functions
    verbs = pd.DataFrame([['abschließen:close', 'schließt ab', 'schloss ab', 'hat abgeschlossen', 'Hast du abgeschlossen?'],
                          ['gehen', 'geht', 'ging', 'ist gegangen', 'Ich gehe, du gehst.']],
                         columns=['Infinitiv', 'Präsens (er/sie/es)', 'Präteritum', 'Perfekt', 'Beispielsatz'])
    monkeypatch.setattr(verben_functions, 'load_file', lambda: verbs)
    feed(monkeypatch, [''] + ['x'] * 8)
    verben_functions.qna_section(config, survival=True)
    out = capsys.readouterr().out
    assert 'abschließen' in out and 'ABSCHLIESSEN' not in out
    assert 'gehen' in out and 'Ich gehe, du gehst.' in out
    assert 'You scored 0 (0%).' in out


# ---------------- scoreboard ----------------

def test_scoreboard(tmp_path, monkeypatch, capsys):
    from scoreboard import scoreboard
    monkeypatch.setattr(scoreboard, 'DATA_DIR', tmp_path)
    scoreboard.show_scoreboard()
    assert 'No high scores yet.' in capsys.readouterr().out
    feed(monkeypatch, ['  ', 'Jürgen', 'Anna', 'Max', 'Lena'])
    # a score of 0 is not saved
    scoreboard.update_scoreboard(0)
    assert not (tmp_path / 'artikel_scoreboard.csv').exists()
    for score in [5, 12, 3, 8]:
        scoreboard.update_scoreboard(score)
    today = date.today().strftime('%d/%m/%Y')
    # no empty lines in between (this used to happen on Windows)
    lines = (tmp_path / 'artikel_scoreboard.csv').read_text(encoding='utf-8').splitlines()
    assert lines == [f'12 pts,Anna,{today}', f'8 pts,Lena,{today}', f'5 pts,Jürgen,{today}']


# ---------------- menu ----------------

def test_menu_asks_again_after_a_typo(monkeypatch, capsys):
    from functions import header
    monkeypatch.setattr(header.time, 'sleep', lambda seconds: None)
    feed(monkeypatch, ['7', '0'])
    with pytest.raises(SystemExit) as finished:
        header.mode_selection(config)
    assert finished.value.code in (None, 0)
    assert 'Please try again' in capsys.readouterr().out


def test_menu_comes_back_after_a_quiz(monkeypatch, capsys):
    from functions import header
    from verben import verben_functions
    verbs = pd.DataFrame([['gehen:to go', 'geht', 'ging', 'ist gegangen', 'Ich gehe.']],
                         columns=['Infinitiv', 'Präsens (er/sie/es)', 'Präteritum', 'Perfekt', 'Beispielsatz'])
    monkeypatch.setattr(verben_functions, 'load_file', lambda: verbs)
    monkeypatch.setattr(header.time, 'sleep', lambda seconds: None)
    # mode 3, no preview, 1 verb, 4 answers, no redo, then exit
    feed(monkeypatch, ['3', 'n', '1', 'geht', 'ging', 'ist gegangen', 'x', 'n', '0'])
    with pytest.raises(SystemExit):
        header.mode_selection(config)
    out = capsys.readouterr().out
    assert 'You scored 3 (100%).' in out
    # the menu is shown again after the quiz
    assert out.count('0: Exit') == 2


def test_runs_from_another_folder_and_exits_cleanly(tmp_path):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    result = subprocess.run([sys.executable, str(ROOT / 'gelato.py')], input='0\n', capture_output=True,
                            text=True, encoding='utf-8', cwd=tmp_path, env=env, timeout=120)
    assert result.returncode == 0, result.stderr
    assert 'GELATO' in result.stdout
