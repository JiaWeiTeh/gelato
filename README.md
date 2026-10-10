# GELATO

**GE**rman **L**earning **A**ssist **TO**ol: a small terminal quiz for practising German noun articles (der / die / das) and verb conjugations.

Full documentation: <https://gelato-language.readthedocs.io/>

## Requirements

- Python 3.9 or newer
- pip

## Install and run

```bash
git clone https://github.com/JiaWeiTeh/gelato.git
cd gelato
pip install -r requirements.txt
python gelato.py
```

Optional: run `pip install -e .` inside the folder to get a `gelato` command you can start from anywhere.

## Modes

| Option | Mode | What it does |
| --- | --- | --- |
| 1 | Article | Type der / die / das for each noun. Wrong answers are repeated until you get them right. |
| 2 | Article (Challenge) | Same quiz with a limited number of hearts. High scores go to a local scoreboard. |
| 3 | Verben (Practice) | Fill in Präsens, Präteritum and Perfekt for each verb. |
| 4 | Settings | Open the settings file in your editor. |

Press `Ctrl+C` at any time to quit.

## Customise

- **Words and verbs:** edit `data/artikel.xlsx` and `data/verben.xlsx`. See the [customisation guide](https://gelato-language.readthedocs.io/en/latest/customisation.html) for the column layout.
- **Name, language, hearts, default question count:** edit `settings/settings.yml`, or pick mode 4 in the menu.

Everything stays on your machine. Scoreboards and the CSV files generated from the Excel sheets are written to `data/` and are ignored by git.

## License

GELATO is free software under the [GNU GPL v3](LICENSE).
