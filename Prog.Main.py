from flask import Flask, jsonify, render_template, request
from random import *
import threading
import time

app = Flask(__name__)


# def thrdLoop():
#     global my_rand   
#     while True:
#         time.sleep(2)
#         my_rand=randint(1, 100)
#         #print(my_rand)


# t = threading.Thread(target=thrdLoop)
# #t.daemon = True
# t.start()





@app.route('/_add_numbers')
def add_numbers():
    #print("Helloooo")
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)



@app.route('/_change')
def add_numbers33():
    #print("Helloooo")
    a = request.args.get('a', 0, type=int)
    xx=jsonify(result=a)

    print("\nValue is:%s\n"%xx)
    return xx

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    global MY_JSON_CONTENTS  

    content = request.get_json()
    MY_JSON_CONTENTS=content
    
    #print (content)
    print("nodeName is :%s"%content['sensorName'])
    print("sensorType is :%s"%content['sensorType'])
    print("Values are :%s"%content['values'])
    print("Times are :%s"%content['timestamps'])
    return 'JSON posted'

@app.route('/_ref')
def add_numbers2():
    global MY_JSON_CONTENTS
    #print("Refs")
    return jsonify(myresult=MY_JSON_CONTENTS)

@app.route('/')
def index():
    return render_template('index.html')

app.run(threaded=True,debug=True, host='0.0.0.0',port=5050);
