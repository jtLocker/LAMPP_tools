#!C:\Users\jackt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html\n")

import os
import subprocess
import cgi

form = cgi.FieldStorage()
i = form.getfirst('USD', 1)

def convert(message, css, price, i):
	
	usd = float(i)
	php = float(price)
	calc = "{:,d}".format(int((usd/php)*100000000))
	concat = str(calc), "sats"
	out = " ".join(concat)

	html = """
	<html>
	<link href='https://fonts.googleapis.com/css?family=Ubuntu:700italic' rel='stylesheet' type='text/css'>
	{css}
	<div id = "bit">{message}</div>
	<br/>
	<div id = "container">{php}</div>
	<form action = "convert.cgi" method = "post">
	<center><text id='result'>USD to Satoshi</text></center>
 	<div id="wrapper">
 	<input type="text" name="USD" Value="{usd}">
	<text>=</text>
	<text id='result' name = "conversion">{out}</text></div><br>
	<input id = "button" type = "submit" value = "Submit"/>
	</form>
	</html>"""
	return html.format(message=message, css=css, php=php, out = out, usd=usd)


message = "$BTC Price"

price = subprocess.check_output('php price_web.php', shell=True).decode('utf-8')

css = """<style>
    #container {
      font-size: 40px;
      font-family: sans-serif;
      text-align: center;      
    }

    #wrapper {
      font-size: 40px;
      font-family: sans-serif;
      text-align: center;
      margin: 0 auto;
      width: 600px;
      border: solid 1px;
    }

    #bit {
      font-size: 40px;
      font-family: 'Ubuntu';
      text-align: center;
    }

    #button {
      padding: 5px 15px;
      background: #ccc;
      border: 0 none;
      cursor: pointer;
      -webkit-border-radius: 5px;
      border-radius: 5px;
      margin: 0 auto;
      display: block;

    }

    #result {
    
      font-size: 20px;
      font-family: 'sans-serif';
    }

    #input {
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 20px;
      font-family: 'sans-serif';
    }

    #equal {
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 20px;
      font-family: 'sans-serif';
    }

  </style>"""
print(convert(message, css, price, i))

