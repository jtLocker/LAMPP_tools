#!C:\Users\jackt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html\n")

import os
import subprocess
import cgi

form = cgi.FieldStorage()
i = form.getfirst('USD', [9])[0]

print((i))

def convert(message, css, price, i):
	
	usd = int(str(i))
	php = price
	
	out = usd/float(price)

	html = """
	<html>
	<link href='https://fonts.googleapis.com/css?family=Ubuntu:700italic' rel='stylesheet' type='text/css'>
	{css}
	<div id = "bit">{message}</div>
	<br/>
	<div id = "container">{php}</div>
	<form action = "convert.cgi" method = "post">
	<input type = "text" name = "USD">
	<input id = "button" type = "submit" value = "Submit"/>
	<div>{out}</div>
	</form>
	</html>"""
	return html.format(message=message, css=css, php=php, out = out)






message = "$BTC Price"

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

print(convert(message, css, price, form))
print(usd)
