#!C:\Users\jackt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html\n")

import os
import subprocess

def spot(message, css, price):
	
	php = price
	html = """
	<html>
	<link href='https://fonts.googleapis.com/css?family=Ubuntu:700italic' rel='stylesheet' type='text/css'>
	{css}
	<div id = "bit">{message}</div>
	<br/>
	<div id = "container">{php}</div>
	<form action = "convert.cgi" method = "post">
	<input id = "button" type = "submit" value = "Submit"/>
	</form>
	</html>"""
	return html.format(message=message, css=css, php=php)

message = "$BTC Price"

#
price = subprocess.check_output('php price_web.php', shell=True).decode('utf-8')

css = """<style>#container{
   font-size: 40px;
   font-family:sans-serif;
   text-align: center;
}

#bit{
   font-size: 40px;
   font-family: 'Ubuntu';
   text-align: center;
}
#button{
	padding:5px 15px; 
    background:#ccc; 
    border:0 none;
    cursor:pointer;
    -webkit-border-radius: 5px;
    border-radius: 5px;
    margin: 0 auto;
    display: block;
}</style>"""

print(spot(message, css, price))