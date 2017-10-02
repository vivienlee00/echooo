#Vivien Lee
#SoftDev1 pd7
#HW06-- Echo Echo Echo
#2017-10-02 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_echo():
    print(request.args)
    #print(request.method)
    return render_template('echo_template.html')

@app.route("/echo")
def echo_echo():
    return render_template('echo_echo_template.html', name = request.args['username'], method = request.method)

if __name__=="__main__":
    app.debug = True
    app.run()
