# Shortening: a simple URL shortener

Endpoints:

 * To generate a short url:
 
 	```curl -X "POST" http://127.0.0.1:5000/ -d "url=https://www.google.com"```
 
 
 * To retrieve a url:
 
 	```curl -X "GET" http://127.0.0.1:5000/<hash>```
 
 
