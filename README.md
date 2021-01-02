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
## Coding on Jupyter Notebook
1. After importing the necessary libraries, load the excel sheet using pandas read_excel
<img target="_blank" src="https://64.media.tumblr.com/cbffa66fec5375457ff0f5407b503f3b/494bc3862fd97b16-69/s1280x1920/78f12d4de2a2bebe03dcde4d67bd1d01f4e4e438.png">

2. Data cleaning: Since we have only a few NaN data, we are going to drop the NaN rows
<img target="_blank" src="https://64.media.tumblr.com/05f2274f5da35ccc3340dc2d7a1111ad/e134c79da8b817d9-b3/s1280x1920/bd08a5e0e23fc4478f93d9b8cd0186b8a5e4c59d.png">


3. Feature extraction: get the unique value of Airline, Source, Destination, Total_Stops of the catecorical data which will be doing one hot encoding and label encoding
<img target="_blank" src="https://64.media.tumblr.com/a1a2fa3f732cffeaccfa17d9d4fcb5eb/494bc3862fd97b16-aa/s1280x1920/2f52f00b5500ea729e63f8381d02bf0c40b9fd75.png">

4. Feature extraction: extracting day and month from the time stamp for arrival_time and dep_time
<img target="_blank" src="https://64.media.tumblr.com/b2bc203943b82b1ef9da2223548a7439/3621f30b68b85d4e-cd/s1280x1920/159aec8ed666c14db120e6dbd5ebd1f704dfc2ad.png">

5. Feature extraction: calculating duration from arrival_time and dep_time
<img target="_blank" src="https://64.media.tumblr.com/e72708d7e537fb1839691174c16a21a7/e134c79da8b817d9-ce/s1280x1920/4f7101283fd1507eefe55446e069e17c90696a1c.png">

5. Handling Categorical Data: performing one hot encoding on the nominal data (Airline, Source, Destination)
<img target="_blank" src="https://64.media.tumblr.com/5ab5dfb88e6c38308d92066d2c122d3e/e134c79da8b817d9-61/s1280x1920/fef1da728dc05585f82748b578e27b6dbe841fcb.png">

6. Handling Categorical Data: performing label encoding on the ordinal data (Total_Stops)
<img target="_blank" src="https://64.media.tumblr.com/65aa2c3de38ce9e1047887cd0734f2a6/3621f30b68b85d4e-e4/s1280x1920/c23835fbe2fde33d51e25c1dbe97a395f3d7c29b.png">
                          
## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

<p align="center">
<img target="_blank" src="https://64.media.tumblr.com/0aead3e6710612287f7c3586ae3eb80c/3fafd73153537ff9-e7/s2048x3072/ee701c63d62cb3a12f38a84f392a4337be25e6b7.png">
<img target="_blank" src="https://64.media.tumblr.com/835f2d919c97703be0b62e37fbb80acb/2bd18ddb098acf53-b0/s1280x1920/40f119edfa41fa3699d4becfe5161cdb8ed95687.png">
<img target="_blank" src="https://64.media.tumblr.com/db7ad57dce8db4112c94d2cdecefbc0b/852e853e46f155de-47/s1280x1920/82f0c655ec4c6bd1731874bea5fa557c7fd89f52.png">
<img target="_blank" src="https://64.media.tumblr.com/2913051a7c514e205d33f14bdbed5057/4f88ec94f7a9d379-56/s1280x1920/b8893bd33120476bd19f31a2175ad5cbc597626e.png">
<img target="_blank" src="https://64.media.tumblr.com/029bdfc5d6ab73e7cb4c51998659426b/3a090db3c9309298-99/s1280x1920/35b30c80e25da93e4ce32e61e8e469b7d91952a0.png">
</p>
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
