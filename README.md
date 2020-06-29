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
### Curl Commands
curl --location --request GET 'localhost:5000/read_file'
curl --location --request GET 'localhost:5000/read_file?start_line=1&end_line=10'
curl --location --request GET 'localhost:5000/read_file/file3.txt?start_line=1&end_line=10'
