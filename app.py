from flask import Flask
import re
from flask import render_template, request, redirect, url_for 
from models import db, Throwers,meetdata,outdoormeetdata
from tables1 import Throws
from constant import dbloc

app = Flask(__name__) 

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False 
app.config['SQLALCHEMY_DATABASE_URI'] = dbloc
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  


db.init_app(app) 



@app.route('/') 
def index():
    return render_template(
        'homefl.html')

@app.route('/process2', methods=['POST'])
def process2():
	name = request.form['name']
	date = request.form['date']
	shot = request.form['spthrow'] 
	#discus = request.form['discus']
    
	signature =meetdata(name=name, meetdate=date,spresult=shot )
	db.session.add(signature)
	db.session.commit()

	results= []
	qry = db.session.query(meetdata)
	results = qry.filter_by(name = name ).order_by(meetdata.spresult.desc())

	table = Throws(results)

	#return render_template('form1.html')
	return render_template('results.html',table=results)	
    	  
	

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	year = request.form['year']
	school = request.form['school'] 
   
	signature = Throwers(name=name, Gradyear=year)
	db.session.add(signature)
	db.session.commit()

	return redirect(url_for('index'))

@app.route('/adddata')
def sign():
	return render_template('sign.html')

@app.route('/addthrow')
def sign2():
	return render_template('inputthrows.html')	

@app.route('/meetresults')
def showresults():
	results= []
	qry = db.session.query(meetdata)
	results = qry.filter_by(name = 'Joe Edwards')
	table = Throws(results)

	return render_template('results.html',table=table)


    
	

@app.route('/links')
def links():
    links = ['http://www.willcountythrows.com', 'http://www.willcountythrows.com','https://www.twitter.com']
    return render_template('links.html', links = links)





if __name__ == '__main__' :
    app.run(debug=True) 
    
