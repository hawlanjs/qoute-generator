from flask import Flask, redirect, render_template, request
import http.client
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

  

    conn = http.client.HTTPSConnection("motivational-quotes1.p.rapidapi.com")

    payload = "{\r\n    \"key1\": \"value\",\r\n    \"key2\": \"value\"\r\n}"

    headers = {
        'content-type': "application/json",
        'X-RapidAPI-Key': "57c99e0d11msh814eadae209acdcp1d8e2fjsn623a617d7a12",
        'X-RapidAPI-Host': "motivational-quotes1.p.rapidapi.com"
        }

    conn.request("POST", "/motivation", payload, headers)

    res = conn.getresponse()
    data = res.read()



    return render_template('index.html', result=data.decode("utf-8"))

  
    