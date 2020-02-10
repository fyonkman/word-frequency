##@Fiona Yonkman 2020
##Python file that contains Queries object and controls webpage

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import model
import pickle

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///previousfiles.db'
db=SQLAlchemy(app)

#class Queries has the attributes: id, filename, original_text, word_frequencies,
#date_created, and stopwords
class Queries(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	filename=db.Column(db.Text, nullable=False)
	original_text=db.Column(db.Text)
	word_frequencies=db.Column(db.PickleType)
	date_created=db.Column(db.DateTime, default=datetime.utcnow)
	stopwords=db.Column(db.Boolean)

#route for main page
@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		#creating a new query
		if 'original_text' in request.form:
			text=request.form['original_text']
			filename=request.form['filename']
			stopwords=request.form.get('stopwords')
			if stopwords:
				stopwords=True
			else:
				stopwords=False
			frequency_dict=model.countWords(text, stopwords)
			new_query=Queries(filename=filename, original_text=text,
						stopwords=stopwords, word_frequencies=frequency_dict)
			try:
				db.session.add(new_query)
				db.session.commit()
				return redirect('/')
			except:
				return 'There was an issue with your query'
		#viewing a previous query
		elif 'view' in request.form:
			current=int(request.form['current'])
			queries=Queries.query.order_by(Queries.date_created).all()
			return render_template('index.html', queries=queries, current=current)
		else:
			return redirect('/')

	else:
		queries = Queries.query.order_by(Queries.date_created).all()
		return render_template('index.html', queries=queries, current=None)

#route which clears database history
@app.route('/clear_history')
def clear_history():
	db.session.query(Queries).delete()
	db.session.commit()
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
