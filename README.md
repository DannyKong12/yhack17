# Project for YHacks 2017
## Emotionji Backend Django Server
A server that handles requests to our sentiment analyzers. Accepts strings of a sentence or entire paragraphs and returns the detected emotion and language tones.


``` javascript
$.get( "ajax/test.html", function( data ) {
  $( ".result" ).html( data );
  alert( "Load was performed." );
});
```
