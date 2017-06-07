#Anna Pyramid Learning Journal

A pyramid learning online journal - used to display, create and edit blog posts. 

**Author**:

-Anna Shelby (bonanashelby@gmail.com)
-The class of Code Fellows Python 401d6

## Routes:

- `/` - the home page - list-view = index.html
-`/journal/{id:\d+}` - detail-view = detail version of blog post 
-`/journal/new-entry` - new-entry = new entry for blog post
-`/journal/{id:\d+}/edit-entry` - update-entry = updated entry for blog

## Set Up and Installation:

- Clone this repository to your local machine.

- Once downloaded, `cd` into the `pyramid-learning-journal`directory.

- Begin a new virtural environment with Python3 and activate it.

- `cd` into `anna_journal` directory. It should be at the same level of `setup.py`

- `pip install` this package as well as the `testing` set of extras into your virtual environment.

- `$ initialize_db development.ini` to initialize the database, populating with random models.

- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

## To Test:

- If you have the  `testing` extras installed, testing will be simple. If you're in the same directory as  `setup.py` just type the following into your command line:

```
$ py.test anna_journal
```

#Heroku URL: https://nameless-savannah-50229.herokuapp.com/