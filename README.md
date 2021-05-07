# P4_python_program_chess-tournament

## Chapters

1. [Presentation](#presentation)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Execution](#execution)
5. [Usage](#usage)
6. [Generation of a code review report with flake8-html](#generation_of_a_code_review_report)
***

## 1. Presentation <a name="presentation"></a>
This Python program is an offline management tool running in a terminal
for the organization of chess tournaments using the swiss-system.
***

## 2. Prerequisites <a name="prerequisites"></a>
This program runs under python 3.9 in a virtual environment.  
Thus, it is usable on Windows, Unix-based operating systems
insofar as the followings are installed:
- python 3.9 (including pip3)
- virtualenv

__Linux__  
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

__Mac__  
_installation of python3.9 and pip3:_  
$ brew install python@3.9    
(pip3 comes along with it) 
if not, download and install the file get-pip.py from https://bootstrap.pypa.io/get-pip.py    
$ py get-pip.py       
_Installation of virtualenv :_    
$ pip3 install virtualenv
  
__Windows__     
_installation of python3.9 and pip3:_  
Download and install python 3.9 for windows from python.org    
(pip3 comes along with it)     
if not, download and install the file get-pip.py from https://bootstrap.pypa.io/get-pip.py    
$ py get-pip.py     
_Installation of virtualenv :_   
$ pip install virtualenv    
***

## 3. Installation <a name="installation"></a>

__Download the project:__    
_Via Git_      
$ git clone https://github.com/AxAks/P4_Programme-python_tournoi-echecs.git    
    
_Via the Web_     
- Visit the page : https://github.com/AxAks/P4_Programme-python_tournoi-echecs      
- Click on the button "Code"     
- Download the project     

__Linux / Mac__       
in the project directory in a shell:       
_create the virtual environment_       
$ python3.9 -m virtualenv 'venv_name'        
_activate the environment:_        
$ source 'venv_name'/bin/activate         
_install project requirements:_       
$ pip install -r requirements.txt         
  
__Windows__    
in the project directory in a shell:        
_create the virtual environment_      
$ virtualenv 'venv_name'      
_activate the environment:_     
$ C:\Users\'Username'\'venv_name'\Scripts\activate.bat       
_install project requirements:_            
$ pip install -r requirements.txt
***

## 4. Execution <a name="execution"></a>
from the terminal, in the root directory of the project:

_activate the environment:_    
$ source 'venv_name'/bin/activate        
_launch the program_:       
$ python main.py          
-> The home menu is then dislayed in the terminal          
***

## 5. Usage <a name="usage"></a>

__Homepage Menu__  
_Navigate through the menu with digits to select a menu option_    
0: Quit the program (saves state before exiting)     
1: Back to Home Menu    
2: Back to previous screen    
3: Load database   
4: Save to database    
n: Menu specific choices     

__From Home Menu__   
_Launch a new tournament or search a previously saved Tournament_   
- enables to:
1. directly launch a new tournament      
2. search an ongoing tournament to land on its managing page. You can resume it from there.

_Manage Players or registered Tournaments_      
- enables to:
1. add players / display reports on registered players
2. add tournaments for later / display reports on saved tournaments (finished or not),      

__Tournament process__    
- Launch New Tournament (from Home Menu)        
-> Fill the form to create and register the tournament        
-> You are redirected to this Tournament specific page    
-> Select Proceed Tournament to enter results of the matches of Round one       
-> the round is saved and you are redirected to the Tournament's page     
-> Select Proceed Tournament to enter the next rounds results     
-> The tournament is over when all the rounds have been played or when all Players have played together.      
-> When the tournament is over, select Proceed Tournament once more to update players rankings and close the tournament    
 
_A tournament can be paused at the end of each round and resumed_    
- Search Registered Tournament To Resume(from Home Menu)     
- Select One (from Tournaments Management Page)   
-> Select Proceed Tournament to enter the next results of next round       
     
__Specific Tournament's Page__   
_Reach the page_    
- Search Registered Tournament To Resume(from Home Menu)   
- Select One (from Tournaments Management Page)     

- Proceed Tournament    
-> enter next step of the Tournament    
- Sort Players by Last Name, Ranking, Result    
-> displays all the players of the tournament by the selected criteria   
- Display Number of Rounds Played
-> displays the number of rounds already played and the total number of rounds   
- Display Rounds and Matches   
-> displays the results of all matches of all previous rounds   
- Display Not Played Matchups    
-> lists for all players the possible next opponents    

__Player Management Menu__  
_Player Creation_
- Add player   
-> fill the form and validate each field: the player is created;    
-> if cancelled the player is not created and you land back to the Player Management page
  
_Player Ranking Update (anytime)_
- Update Player Ranking   
-> search the player by ID   
-> enter the new ranking   
-> the new ranking is saved   
  
_Display all Players by Last Name_    
- Display By Last Name    
-> All Players in the registry are returned sorted by Last Name   
   
_Display all Players by Ranking_   
- Display by Ranking   
-> All Players in the registry are returned by Ranking from highest to lowest   
  
_Search Players by ID_   
- Search by Id   
-> enter an ID or part of an ID    
-> all matching players are returned   
    
__Tournament Management Menu__   
_Tournament Creation_   
- Add Tournament    
-> fill the form and validate each field: the tournament is created    
-> if cancelled the tournament is not created and you land back to the Tournament Management page   

_Display By Start Date, Name, or Location_   
- Display By Start Date, Name or Location    
-> All Tournament in the registry are returned sorted by the selected criteria   
  
_Search Tournaments_    
- Search Tournaments    
-> enter a date or name or location or part of them     
-> all matching tournaments are returned    
  
_Select One Tournament_   
- Select One    
-> enter a date or name or location or part of them     
-> When only one result returns, you are redirect to this Tournament Page     
***

## 6. Generation of a code review report <a name="generation_of_a_code_review_report"></a>
__flake8_html__    
_Launch the Analysis_
(at the project root level)    
$ flake8 --format=html --htmldir=flake-report . -v   

format = format of the report (html)
htmldir = name of the directory to be created to store the report (mandatory)
. = current directory
-v = verbose (optional)

(from anywhere in the system)       
$ flake8 --format=html --htmldir=flake-report --config [path/to/config/file] [path/to/project/root/] -v          
config = the file is named 'setup.cfg and is located at the root of the project (mandatory if not in the working directory)     

see more options here:  
https://flake8.pycqa.org/en/latest/user/options.html  
note: setup.cfg file excluding files from the analysis 
and setting te limit to 119 characters per line  

to read the reports:  
- browse files to the 'flake-report' directory
- open the file index.html in a webbrowser
***