from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/geturl")
def recehtml():
    name=request.args.get("t1")
    address=request.args.get("t2")

    return "The user {} stays in {} ".format(name,address)

#Accepting and returning the data to the html file

@app.route('/see')
def callhtmal():
    return render_template("home.html")

'''Calling the HTML file which is should be in the "scripts" folder in 
the current folder
'''
if __name__=='__main__':
    app.run(debug=True)
