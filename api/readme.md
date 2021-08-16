# String Matching

## Introduction
This problem is designed to test your ability to write software, not set up new projects. It is designed
such that an experienced developer can complete it within a couple of hours. With that in mind, we have
provided some starting files to hopefully avoid some of the common pitfalls with beginning a new project.
The starting app is provided as a means to help you get things off the ground. If you feel more comfortable
using a different approach, you are welcome to do so.

**We will assume you have both Node.js and Python3 installed globally on your system**

to start a new react project using [Create React App][2]:
```commandline
$ npx create-react-app web
```

to begin using the `api` backend code:

```commandline
$ cd api
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

to run the backend app:

```commandline
$ python main.py
```

to run the unit tests for the backend app:

```commandline
$ python -m unittest
```

If you have any questions during the exercise, please feel free to reach out and ask for clarity.

## Problem

Create a webapp which allows you to maintain a list of words. A user should be able to add a new word
to the list, fetch the list of words, and fetch a filtered list based on a provided pattern.

#### Match

Create a string matching function which takes 2 inputs:
 1. pattern
 2. string
 
and returns whether they are a match. The pattern may use any number of the following special characters:
 * `*` = 0 or more of any character (regex `.*`)
 * `!` = 1 of any character (regex `.{1}`)
 
You may not use the `re` module.
 
 examples:
 
 ```python
match('a*b', 'ab')  // True
match('a*b', 'azzb')  // True
match('a!b', 'ab')  // False
match('a!b', 'azb')  // True
match('a*b!c', 'ayybzc')  // True
```

#### API

Create a `words` API which supports the following operations:
* Add [`POST`] = Insert words
* List [`GET`] = Retrieve words

We will use our `match` method to support an optional `pattern` parameter to the List operation.

```json
POST /words ["apple", "banana"]
["apple", "banana"]
``` 

```json
GET /words
["apple", "banana"]
``` 

```json
GET /words?pattern=b*a
["banana"]
```

#### Web

Create a simple React webapp to consume our API. The front end should be able to to view the word 
list, add new words to the word list, and filter the word list using the back end `pattern` filter.
Styling can be kept to a minimum, but the UI should be clear and organized. Use of a 3rd party 
library (e.g., [Bootstrap][0]) is allowed, but some raw CSS should also be used. Functionality is key.


## Hints
* persisting data is not required; feel free to use in memory data structures for storage
* unless you have a strong preference, use a simple webserver like [Flask][1] for the API
* unless you have a strong preference, use [Create React App][2] to begin your front end work
* code should be optimized for readability and performance
* unit tests can help rapid iteration during development, and validation of the final product
* a reasonable backend solution can be achieved in less than 50 lines of code

[0]: https://getbootstrap.com/
[1]: https://flask.palletsprojects.com/
[2]: https://reactjs.org/docs/create-a-new-react-app.html
