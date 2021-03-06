#!C:\xampp\htdocs\web\Environments\Bitmo\Scripts\python.exe
print("Content-Type: text/html\n")

import os
import subprocess
import cgi

#REQUIRED GLOBAL VARIABLE FOR FUNCTIONS
form = cgi.FieldStorage()

def convert(message, css, price, form):
	
	inpu = form.getfirst('USD', 1)	
	usd = float(inpu)
	price = float(price)
	calc = "{:,d}".format(int((usd/price)*100000000))
	concat = str(calc), "sats"
	out = " ".join(concat)

	html = """
	<html>
	<link href='https://fonts.googleapis.com/css?family=Ubuntu:700italic' rel='stylesheet' type='text/css'>
	{css}
	<div id = "bit">{message}</div>
	<br/>
	<div id = "equal">Enter an amount in Dollars to be converted into Satoshis</div>
	<form action = "convert.cgi" method = "post">
	
 	<div id="wrapper">
 	<input type="text" name="USD" Value="{usd}">
	<text>=</text>
	<text id='result' name = "conversion">{out}</text></div><br>
	<input id = "button" type = "submit" value = "Submit"/>
	</form>
	</html>"""
	return html.format(message=message, css=css, out = out, usd=usd)


message = "USD to Satoshi"

php = subprocess.check_output('php price_web.php', shell=True).decode('utf-8')

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
print(convert(message, css, php, form))

