# Trello project management - API testing with Python Requests library.


This project contains couple of tests written agains Trello REST API. 
In order to run this tests you have to have your own Trello account which you can create here: __https://trello.com/__


Additionally you have to login into Developers Trello __https://developers.trello.com__
and generate **key** and **token**. This action you can perform here __https://trello.readme.io/docs/api-introduction__. 


When you will get **key** and **token**, you have two options
    

- set them as environmental variables as I did on Ubuntu 16.04:
    

    ```

    $ export TRELLO_KEY=your key here
    $ export TRELLO_TOKEN=your token here

    ```

- paste generated Trello key and token into **config.py** file and set them in the **class Credentials** as class variables.


# How run this tests


Tests were written with Python 3.6.5 and run on Ubuntu 16.04 LTS.
After downloading the repo, go to __Trello_REST_API_Tests__ folder and create __virtualenvironment__


```
$python3.6 -m venv ./venv

```


When virtualenvironment will be created, run it.


```
$ source /venv/bin/activated

```


Install required dependencies from __requirements.txt__ file.

```
$ pip3 install -r requirements.txt

```


Check if requests library was sucessfully installed in your environment:


```

$ pip3 list

```


Go to __Trello__ package and run test by entering the command:


```

$ python3 run.py

```