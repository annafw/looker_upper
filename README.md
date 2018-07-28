# looker_upper

The looker_upper app answers the question:

    Is this product safe for me to use?


## Tech Stack

* Python 3
* Django
* Sqlite3

## Setup

* Download this repository.
* To activate this project's virtualenv, run pipenv shell.
* Alternatively, run a command inside the virtualenv with pipenv run.
* Run database migrations: `python3 manage.py migrate`

## Run

To run the server:

```
python manage.py runserver
```

## Design

Look up what I want. Tell me if this product is safe or if it's gonna make my skin so super sad.

Here's what it's about:

* put my api stuff in a yml file that i don't check into git
* Take a UPC code and look up product ingredients.
* have a list of what you are allergic to.
* * Look up what you input as your allergens and find related ones and that makes the list of "baddies"
* compare the "baddies" to the ingredients in the product.
  * What about misspellings like Quanternium-15? That's in the J&J baby shampoo.
* upc scanning for the product. scan upc. get the product in the db.

## Things to think about

* Misspellings of ingredients. Maybe get similar names?
* Product ingredient updates. Maybe this database isn't reliable?

## First Steps

1. Enter product name, get list of ingredients back
   POST /ingredients { product_name: NAME }

2. Add UI to enter product name

