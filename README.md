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

un fichier README.md contenant des instructions claires sur la manière 
d'exécuter le programme, de l'utiliser et de générer un nouveau fichier flake8-html.
voir mise en page de P2 !!


## 1. Presentation <a name="presentation"></a>


## 2. Prerequisites <a name="prerequisites"></a>

This program runs under python 3.9 in a virtual environment.
Thus, it is usable on Windows, Unix-based operating systems
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
- if not, download the file get-pip.py from https://bootstrap.pypa.io/get-pip.py    
  and install it     
-> py get-pip.py     
- Install virtualenv     
-> pip install virtualenv    
  
## 3. Installation <a name="installation"></a>

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


## 4. Execution <a name="execution"></a>
from the terminal, in the root directory of the project:

_activate the environment:_    
$ source 'venv_name'/bin/activate        
_launch the program_:       
$ python main.py          
-> The home menu is then dislayed in the terminal          


## 5. Usage <a name="usage"></a>

Homepage Menu:   
-> Navigate through the menu with digits to select a menu option.
0: Quit the program (saves state before exiting) 
1: Back to Home Menu
2: Back to previous screen
3: Load database
4: Save to database

From Home Menu
- Manage Players or registered Tournaments:      
-> enables to display reports on players or saved tournaments (finished or not),

- Launch a new tournament or search a previously saved Tournament
-> enables to:         
  1: directly launch a new tournament      
  2: search an ongoing tournament to land on its managing page. You can resume it from there.

Player Management Menu:  
Player Creation:
- Add player:
-> fill the form and validate each field: the player is created;
-> if cancelled the player is not created and you land back to the Player Management page
  
Player Ranking Update (anytime):
- Update Player Ranking
-> search the player by ID
-> enter the new ranking  
-> the new ranking is saved
  
Display all Players by Last Name
- Display By Last Name 
-> All Players in the registry are returned sorted by Last Name
  
Display all Players by Ranking
- Display by Ranking
-> All Players in the registry are returned by Ranking from highest to lowest
  
Search Players by ID
- Search by Id
-> enter an ID or part of an ID
-> all matching players are returned
  
Tournament Management Menu:  
Tournament Creation:
- Add Tournament
-> fill the form and validate each field: the tournament is created;
-> if cancelled the tournament is not created and you land back to the Tournament Management page

Display By Start Date, Name, or Location
- Display By Start Date
- Display By Name 
- Display By Location
-> All Tournament in the registry are returned sorted by the selected criteria
  
Search Tournaments     
- Search Tournaments    
-> enter a date or name or location or part of them     
-> all matching tournaments are returned
  
Select One Tournament
- Select One
-> enter a date or name or location or part of them 
-> When only one result returns, you are redirect to this Tournament Page  
  
Tournament process
- Launch New Tournament (from Home Menu)    
-> Fill the form to create and register the tournament       
-> You are redirected to this Tournament specific page   
-> Select Proceed Tournament to enter results of the matches of Round one   
-> the round is saved and you are redirected to the Tournament's page   
-> Select Proceed Tournament to enter the next rounds results   
-> Until all the rounds are played    
-> When all the rounds are played, select Proceed Tournament once more to update players rankings   

A tournament can be paused at the end of each round and resumed  
- Search Registered Tournament To Resume(from Home Menu)   
- Select One (from Tournaments Management Page)
-> Select Proceed Tournament to enter the next results of next round    

Specific Tournament's Page
- Reach the page
-> Search Registered Tournament To Resume(from Home Menu)
-> Select One (from Tournaments Management Page)     
- Proceed Tournament
-> enter next step of the Tournament
- Sort Players by Last Name, Ranking, Result
-> displays all the players of the tournament by the selected criteria   
- Display Rounds and Matches
-> displays all matches of all previous rounds  
- Display Not Played Matchups
-> lists for all players the possible next opponents 


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