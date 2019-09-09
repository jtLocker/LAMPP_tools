#!C:\Users\jackt\AppData\Local\Programs\Python\Python36\python.exe
print("Content-Type: text/html\n")

import os
import subprocess
import cgi
from pywallet import wallet
import qrcode

# generate 12 word mnemonic seed
seed = wallet.generate_mnemonic()

# create bitcoin wallet
wallet = wallet.create_wallet(network="BTCtest", seed=seed, children=1)
# print(str(wallet))
w = wallet.keys(), wallet.values()

def gen_wallet(message, css, wallet):

	coin = wallet["public_key"]
	data = "https://www.blockchain.com/btc/address/"+"32hQKijSkpC6WYSs73Y9ir6AxxMBCjkBfN"

	qr = qrcode.QRCode(
	    version = 1,
	    error_correction = qrcode.constants.ERROR_CORRECT_H,
	    box_size = 10,
	    border = 4,
	)

	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image()
	img.save("image.jpg")

	html = """
	<html>
	<link href='https://fonts.googleapis.com/css?family=Ubuntu:700italic' rel='stylesheet' type='text/css'>
	{css}
	<div id = "bit">{message}</div>
	<div id = "wallet_wrapper">
	<text>{coin}</text>
	<img src = image.jpg>
	</div>
	</html>"""
	return html.format(message=message, css=css, coin=coin)

form = ""
message = "Generate Wallet"
php = subprocess.check_output('php price_web.php', shell=True).decode('utf-8')

css = """<style>
    #container {
      font-size: 40px;
      font-family: sans-serif;
      text-align: center;      
    }

    #wallet_wrapper {
      font-size: 25px;
      font-family: sans-serif;
      text-align: center;
      
      
      border: solid 1px;
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
print(gen_wallet(message, css, wallet))

# contents = ""

# for ele in w:
# 	contents +=(str(ele))
# print("<html>"+contents+"</html>")