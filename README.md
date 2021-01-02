# Flight fare prediction
Possibly contains awesomeness and flight_fare_prediction related files

## Overview
This is a Flask web app which predicts the fare of Flight ticket developed using python(Jupyter Notebook) and deployed on Heroku app.

## Installation
The Code is written in Python 3.8.6. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip, navigate into the installed python directory and open command promt:
```bash
python -m pip install --upgrade pip
```
If you have a higher version i.e. 3.8 or 3.9, make sure you install pip during your python installation or use this [get-pip.py](https://bootstrap.pypa.io/get-pip.py) in your python directory.
```bash
py get-pip.py
```
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[](https://64.media.tumblr.com/0aead3e6710612287f7c3586ae3eb80c/3fafd73153537ff9-e7/s2048x3072/ee701c63d62cb3a12f38a84f392a4337be25e6b7.png)
[![](https://64.media.tumblr.com/835f2d919c97703be0b62e37fbb80acb/2bd18ddb098acf53-b0/s1280x1920/40f119edfa41fa3699d4becfe5161cdb8ed95687.png)]
[![](https://64.media.tumblr.com/db7ad57dce8db4112c94d2cdecefbc0b/852e853e46f155de-47/s1280x1920/82f0c655ec4c6bd1731874bea5fa557c7fd89f52.png)]
[![](https://64.media.tumblr.com/2913051a7c514e205d33f14bdbed5057/4f88ec94f7a9d379-56/s1280x1920/b8893bd33120476bd19f31a2175ad5cbc597626e.png)]
[![](https://64.media.tumblr.com/029bdfc5d6ab73e7cb4c51998659426b/3a090db3c9309298-99/s1280x1920/35b30c80e25da93e4ce32e61e8e469b7d91952a0.png)]

You also use this [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Technologies Used
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" height=50>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" height=50>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" height=50>](https://scikit-learn.org/stable/)
<br>
[![made-with-python](https://img.shields.io/badge/made%20with-Python-yellow)](https://www.python.org/) [![made-with-jupyter](https://img.shields.io/badge/made%20with-Jupyter-orange)](https://jupyter.org/)

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/arunmozhidevan/flight_fare_prediction/issues) here by including your search query and the expected result.

## Directory Tree 
```
├── templates
│   ├── home.html
├── Procfile
├── README.md
├── app.py
├── flight_fare_predicition.ipynb
├── flight_rf.pkl
├── requirements.txt
```
