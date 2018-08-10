from flask import Flask
from flask import Markup
from flask import render_template
app = Flask(__name__)
 
 
@app.route("/")
def index():   
     return render_template('index.html')
	
@app.route("/barchart")
def barchart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('barchart.html', values=values, labels=labels)
	
@app.route("/linechart")
def linechart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('linechart.html', values=values, labels=labels)

@app.route("/piechart")
def piechart():
	labels = ["January","February","March","April","May","June","July","August"]
	values = [10,9,8,7,6,4,7,8]
	colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
	return render_template('piechart.html', set=zip(values, labels, colors))
 
if __name__ == "__main__":
    app.run(debug='true' , host='0.0.0.0', port=5001)
