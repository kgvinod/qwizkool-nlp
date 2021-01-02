# qwizkoolnlp
NLP based implementation of QwizKool

## Installation instructions

##### Clone the repository
```git clone git@github.com:kgvinod/qwizkoolnlp.git```
```
##### Go into the project directory
```cd qwizkoolnlp
```
##### Create a virtual environment to avoid messing with your system wide packages
```python3 -m venv .venv
source .venv/bin/activate
```
##### Install dependencies
```pip install -r requirements.txt 
```
##### Build and locally install the qwizkoolnlp package
```pip install .
```
##### Run the unit tests
```python setup.py test
or
pytest -s -v
```
##### Test drive using the console application
```python app/main.py 
```

## Code layout / guideines
##### Package folder
The qwizkoolnlp package folder is located in ./qwizkoolnlp. Everything under this folder will be packaged into qwizkoolnlp
package when 'pip install .' is run. All client cade imports (such as in apps, tests) are structured assuming that the qwizkoolnlp library is installed.

##### ./tests folder
All automated unit tests should be added here. Refer existing ones for how to write one. These tests will be run by the CI system. It can also be run manually by using 'python setup.py test' or 'pytest -s -v'.

##### ./app folder
Applications that use the qwizkoolnlp library are hosted here. These are typically test applications with console interface or a GUI. These apps ARE NOT run by the CI system automatically.

##### Adding/modifying code
The meat of the project is under ./qwizkoolnlp/*. If you are modifying/adding to existing functionality, sub-class the existing class and add/override existing implementation. Then, write testers in ./tests and demo/usage applications in ./app. Once everything is verified, modify the client to use the sub-class, overridden methods etc.






