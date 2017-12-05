# Emotionji Backend Django Server
### A project for YHack 2017
A server that handles requests to our sentiment analyzers. Accepts strings of a sentence or entire paragraphs and returns the detected emotion and language tones, or submit an audio file and we will try to

## Getting started
Our server is purely independent, send a request and you're on your way! Send a request however you'd like.

##

## Calling our Server
Send a typical GET request to our server with a url argument at the end.  

e.g.
``` javascript
$.get( "immense-lowlands-49222.herokuapp.com/yhackss/1/<str>", function( data ) { // send a request to the url with your input replacing <str>
  ... data ...
});
```

We return lists of tuples with (emotion, confidence, language tone), one for each sentence
Example:
```python
[('Joy', 0.98270000000000002, 'Analytical'), ('Joy', 0.99839999999999995, 'Tentative')] # example api results

```

## Built with
Django 2.0
Python 3.6.2
NLTK
IBM-Watson api
Indico
