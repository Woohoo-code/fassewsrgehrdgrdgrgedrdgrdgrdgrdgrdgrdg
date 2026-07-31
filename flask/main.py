from flask import Flask, render_template, request, jsonify, make_response, abort
import sqlite3
from cryptography.fernet import Fernet
import json
from flask import Flask
from pathlib import Path

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from datetime import datetime, timedelta, UTC


key = Fernet.generate_key()

fernets = Fernet(key)


DB_NAME = "count.db"
clicks = 1
clickse = 0

app = Flask(__name__)




@app.before_request
def limit_remote_addr():
    ips = ["10.144.6.57"]
    if not request.remote_addr in ips :
        abort(403)

@app.route("/")
def mainroute():
    return """<a href="/clicker">
A link to the icepop clicker page</a>."""
"""
def get_database():
    g = sqlite3.connect(DB_NAME)
    g.row_factory = sqlite3.Row
    return g 
def init_data():
    g = get_database()
    g.execute("CREATE TABLE IF NOT EXISTS counter
    (id INTEGER PRIMARY KEY, 
    visits INTEGER NOT NULL)")
    h = g.execute("SELECT * FROM counter WHERE id = 1").fetchone()
    if h is None:
        g.execute("INSERT INTO counter(id, visits) VALUES(1,0)")
    g.commit()
    g.close()
 
@app.route("/counter")
def counter():
    the_variable = get_database()
    the_variable.execute("UPDATE counter SET visits = visits+1 WHERE id = 1")
    the_variable.commit()
    visits = the_variable.execute("SELECT visits FROM counter WHERE id = 1").fetchone()["visits"]
    the_variable.close()
    print(visits)
    return  f"<div id=\"count\">{visits}</div>"; visits = visits
    """
def setcookie(template=None):
    global clicks
    global clickse
    if template == None:
        template = render_template("index.html", visits=clickse, clicks=clicks)
    resp = make_response(template) 
    
    thing = json.dumps(clickse).encode()
    thing2 = json.dumps(clicks).encode()
    thing = fernets.encrypt(thing).decode("utf-8")
    thing2 = fernets.encrypt(thing2).decode("utf-8")
    
    resp.set_cookie('clicks', str(thing), httponly=False)
    resp.set_cookie('cpc', str(thing2), httponly=False)
    return resp
def getcookie(number=1, template=None):
    if request.cookies.get("clicks") != None and number == 1:
        if number == 1:
            g=request.cookies.get("clicks")
            y =  fernets.decrypt(g.encode())
            return json.loads(y.decode())
    elif request.cookies.get("cpc") != None and number == 2:
        if number == 2:
            g=request.cookies.get("cpc")
            y =  fernets.decrypt(g.encode())
            return json.loads(y.decode())
    else:
        return None
@app.route("/getcookies", methods=['GET'])
def getcookies():
    return jsonify({"cookie1": str(getcookie(1)), "cookie2": str(getcookie(2))})
@app.route("/clicker")
def clicker():
    global key
    global clickse
    global clicks
    temp = render_template("index.html", visits=clickse, clicks=clicks)
    if getcookie(1) == None and  getcookie(2) == None: 
        clicks = 1
        clickse = 0
        return setcookie(temp)
    else:

        clickse =  getcookie(1, temp)
        clicks =  getcookie(2, temp)  
    return temp



@app.route("/clickerbuybackend", methods=['POST'])
def removebackend():
        removeamount = request.json["spent"]
        global clicks
        global clickse
        clickse = int(getcookie(1))
        if removeamount == 0:
            clickse = 0
            clicks = 1
            return setcookie(jsonify({"visits":0}))
            
        
        if clickse >= removeamount:
            clicks = request.json["clicks"]
            clickse -= removeamount
            return setcookie(jsonify({"visits": clickse}))
        
        return jsonify({"visits": "error"})

@app.route("/clickerbackend", methods=['POST'])
def backend():
    global clickse
    global clicks
    visits = int(getcookie(1))
    clicks = int(getcookie(2))
    visits += clicks
    clickse = visits
    print(visits)
    return setcookie(jsonify({"visits":visits}))

app.run(host="0.0.0.0", port=5000, ssl_context=("cert.pem", "key.pem"))