# Emotionji Backend Django Server
### A project for YHack 2017
A server that handles requests to our sentiment analyzers. Accepts strings of a sentence or entire paragraphs and returns the detected emotion and language tones, or submit an audio file and we will try to

## Getting started
Our server is purely independent, send a request and you're on your way! Send a request however you'd like.


## Calling our Server
Send a typical GET request to our server with a url argument at the end.  

e.g.
``` javascript
var url = "immense-lowlands-49222.herokuapp.com/yhackss/1/"
$.get( url + <str>, function( data ) { //  send request with your input replacing <str>
  ... data ...
});
```

We return lists of tuples with (emotion, confidence, language tone), one for each sentence  
Example:
```python
[('Joy', 0.98270000000000002, 'Analytical'), ('Joy', 0.99839999999999995, 'Tentative')] # example api results

```

## Our frontend
Our frontend was made by our team, and is hosted on a different repo.
[Github](https://github.com/sharon-ho/emotionji/blob/master/index.html)


## Built with
[Django 2.0](https://docs.djangoproject.com/en/2.0/releases/2.0/) - The web framework we used  
[NLTK](http://www.nltk.org/) - Used for sentence tokenizing  
[IBM-Watson api](https://www.ibm.com/watson/) - Our analytics engine  
[Indico](https://indico.io/) - Our emotion analytics  

## Authors
- Tate Cheng
- Nicolas Hudon
- Sharon Ho
- Danny Kong

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/DannyKong12/yhack17/blob/master/LICENCE.md) file for details
