## Dev Prerequisites 

#### Ubuntu/Debian

* python 3.8.x
    * `sudo apt-get install python3.8 python3-pip`
* virtualenv
    * `sudo pip3 install virtualenv`

### First time setup (using virtualenv)
```
# using virtualenv
virtualenv --python=python3.8 prac_env
git clone https://github.com/FranklinBarretto/Prac.git
cd Prac
source prac_env/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```
