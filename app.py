#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask, redirect, url_for, request

import logging
# Flask app should start in global layout
app = Flask(__name__)


# hostname='localhost'
# username='postgres'
# password='root'
# database='HRbot'

# def doQuery( conn,name ) :
#     cur = conn.cursor()

#     cur.execute( "SELECT * FROM Employee_details where name ="+name+";" )
#     leave_balance;
#     for leave in cur.fetchall() :
#         print( leave_balance)
#         leave_balance=leave_balance
#     return leave_balance    


# print( "Using psycopg2…")
# import psycopg2
# myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )




@app.route('/test',methods = ['POST', 'GET'])
def test():
    return "Hello world"

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    
    logging.debug('This is a debug message')
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    #r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    return res

def makeWebhookResult(req):

    if req.get("result").get("action") != "leave-types":
       return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("leaves")

    # leave_bal=doQuery( myConnection ,zone)
    # myConnection.close()
    
    cost = {'Casual leave':'11', 'Sick leave':'15', 'Privileage leave':'20'}

    speech = "The leave  balance for " + zone + " is " + str(cost[zone])
    #print(leave_bal)
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": "leave-balance"
    }

if __name__ == '__main__':
    #port = int(os.getenv('PORT', 5000))

    #print ("Starting app on port %d" %(port))

    app.run(debug=True,port=80, host='0.0.0.0')