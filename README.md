# Tech Talk Live 2019: Data Wrangling with Python
## May 8, 2019

Here are example files for learning Python and employing it for common data manipulation tasks.

[View the slides from the presentation.](https://www.bowmanjd.com/ttl/python-data)

To interact with the code in this repository, you may use:
- [the associated repl at repl.it](https://repl.it/@jonathanbowman/ttl2019)
- Run it in your own environment (see next)

### Setup on your system

New to the command-line or Python in your environment (be it Windows, Mac, Linux...)? You might [read a helpful getting started guide](https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly).

Once you are at the command-line, make sure `python --version` outputs something 3.6 or above. If not, try `python3 --version` `python3.7 --version` or, on Windows, `py -3 --version`. Then, anywhere in the instructions you see `python`, replace it with whatever worked for you (`python3` most likely). If none of this works, you might not have Python installed correctly, and can refer to the [slides](https://www.bowmanjd.com/ttl/python-data) or the previously mentioned [getting started guide](https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly).

Now you can install the few required packages for interacting with the sample Python code. These are listed in `requirements.txt` and can be installed/upgraded with `python -m pip install -Ur requirements.txt` (again, you may need to use `python3` instead if your system's `python` launches version 2.7.)

If you are concerned about cluttering up your Python environment (as you should be), you create a virtual environment in this directory with `python -m venv venv` then activate it using one of the following:

#### On Windows
- cmd.exe: `.\venv\Scripts\activate.bat`
- PowerShell: `.\venv\Scripts\Activate.ps1`

#### Everything else
- bash or zsh: `source ./venv/bin/activate`
- fish: `. ./venv/bin/activate.fish`
- csh/tcsh: `source ./venv/bin/activate.csh`

Then run `pip install -Ur requirements.txt`
