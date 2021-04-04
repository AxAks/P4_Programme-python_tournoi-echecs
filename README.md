# P4_python_program_chess-tournament
***
This Python program is an offline management tool running in a terminal
for the organization of chess tournaments using the swiss-system.
***

## Chapters

1. [Presentation](#presentation)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Execution](#execution)
5. [Usage](#usage)
6. [Generation of a code review report](#generation_of_a_code_review_report)

a retirer !
un fichier README.md contenant des instructions claires sur la manière 
d'exécuter le programme, de l'utiliser et de générer un nouveau fichier flake8-html.
voir mise en page de P2 !!


extrait des consignes :



## 1. Presentation <a name="presentation"></a>


- _Installation des dépendances du projet dans l'environnement :_  
$ pip install -r requirements.txt

## 2. Prerequisites <a name="prerequisites"></a>
  #  (à relire !!)
This program runs under python 3.9 in a virtual environment.
Thus, it is usable on Windows, Mac and Linux-based operating systems
Insofar as the followings are installed:
- python 3.9 (including pip3)
- virtualenv

On Linux: 

_installation of python3.9:_
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.9


_installation of pip3:_
$ wget https://bootstrap.pypa.io/get-pip.py  
$ python3.9 get-pip.py  
$ pip --version  

_Installation of virtualenv :_  
$ sudo apt install virtualenv



On Mac: 
- install python 3.9 and pip 3
-> brew install python@3.9
  (pip3 comes along with it)
  
- install virtualenv
-> pip3 install virtualenv

- create virtual env:
virtualenv -p python3 'desired-path'

- activate virtualenv:
source <desired-path>/bin/activate


On Windows:
- Install python 3.9 for windows from python.org
  (pip3 comes along with it)
- if not, download the file get-pip.py with: 
  (get cURL pour windows ? or manual download from https://bootstrap.pypa.io/get-pip.py ?)
-> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
and install it 
-> py get-pip.py (execute get-pip.py => system-wide?)
- Install virtualenv
-> pip install virtualenv

  
## 3. Installation <a name="installation"></a>
  #  (à relire !!)
__Download the project:__
Via Git:
$ git clone https://github.com/AxAks/P4_Programme-python_tournoi-echecs.git

Via the Web :
- Visit the page : https://github.com/AxAks/P4_Programme-python_tournoi-echecs  
- Click on the button "Code"
- Download the project


On Windows:
in the project directory in a shell:
_create virtualenv:_
$ virtualenv 'venv_name' 
_activate the environment:_
$ C:\Users\'Username'\'venv_name'\Scripts\activate.bat
_install project requirements:_ 
$ pip install -r requirements.txt


On Linux/ Mac:
in the project directory in a shell:
_create the virtual environment:_
$ python3.9 -m virtualenv 'venv_name'
_activate the environment:_
$ source 'venv_name'/bin/activate
_install project requirements:_ 
$ pip install -r requirements.txt

à suivre ...

## 4. Execution <a name="execution"></a>
  #  (à relire !!)
from the terminal, in the root directory of the project:

_activate the environment:_
$ source 'venv_name'/bin/activate
_launch the program_:
$ python main.py  
-> The menu is then dislayed in the terminal  

... à suivre ...

## 5. Usage <a name="usage"></a>

Homepage Menu
- Players Menu
-- Add player
-- List all players 
--- sorted by last name
--- sorted by ranking
  
- Tournaments Menu
-- List all tournaments
-- select a tournament
-- List all players for a tournament
--- sorted by last name
--- sorted by "result" (during the tournament)
-- List all rounds for a tournament
-- List all matches for a tournament

-- Add tournament 
--- add players to tournament
-- resume tournament 
---- Add round to a tournament (during a tournament)
----- Add match to a round (during a tournament)


- Start a new tournament
  - add players (8)
  - generate pairs for game (1st round)
  - Enter rounds results (Round 1 : match 1, match 2, match 3, match 4)
  - new pairs for next rounds 
  - Results for next rounds

## 6. Generation of a code review report <a name="generation_of_a_code_review_report"></a>
à relire et rédiger...

Pour lancer  flake8_html:
in the root of the project 

variantes de:  
$ flake8 --format=html --htmldir=flake-report . -v  
htmldir = name of the directory to be created to store the report.  
-v = verbose (not necessary)  
see more options here:  
https://flake8.pycqa.org/en/latest/user/options.html  
note: setup.cfg file excluding files from the analysis 
and setting te limit to 119 characters per line  

to read the reports:  
- browse files to the 'flake-report' directory
- open the file index.html in a webbrowser