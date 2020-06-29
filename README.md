## Dev Prerequisites 

#### Ubuntu/Debian

* python 3.8.x
    * `sudo apt-get install python3.8 python3-pip`
* virtualenv
    * `sudo pip3 install virtualenv`

### First time setup (using virtualenv)
```
# using virtualenv
virtualenv --python=python3.8 testenv --no-site-packages
git clone git@.git
cd test
source testenv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```
