# Place, time, and mind

> A place and time for things and mind.

## Build Setup

``` bash
# clone the repository
git clone git@github.com:mihaiconstantin/PlaceTimeMind.git

# setup a virtual environment 
cd PlaceTimeMind/
virtualenv venv
cd venv/Scripts/
activate

# install `Python` dependencies
cd ..
cd ..
pip install -r requirements.txt
# or
pip install --upgrade -r requirements.txt

# install `node.js` dependencies
cd client/
npm install

# build for production with minification
npm run build

# start the `Flask` development server (the instructions below apply to Windows)
# for more details consult the flask documentation at 
# http://flask.pocoo.org/docs/0.12/quickstart/
cd..
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run

# open http://localhost:5000 in your broswer
```

For more details, feel free to drop me a line at `m.a.constantin@uvt.nl`.