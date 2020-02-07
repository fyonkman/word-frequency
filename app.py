from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import model
import pickle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///previousfiles.db'
db = SQLAlchemy(app)

class Queries(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.Text, nullable=False)
	originalText = db.Column(db.Text)
	word_frequencies = db.Column(db.PickleType)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)
	stopwords = db.Column(db.Boolean)

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		text = request.form['originalText']
		filename = request.form['filename']
		stopwords = request.form.get('stopwords')
		if stopwords:
			stopwords = True
		else:
			stopwords = False
		frequency_dict = model.countWords(text, stopwords)

		new_query = Queries(filename=filename, originalText=text,
						stopwords=stopwords, word_frequencies=frequency_dict)

		try:
			db.session.add(new_query)
			db.session.commit()
			return redirect('/')
		except:
			return 'There was an issue with your query'

	else:
		queries = Queries.query.order_by(Queries.date_created).all()
		return render_template('index.html', queries=queries)

@app.route('/clear_history')
def clear_history():
	db.session.query(Queries).delete()
	db.session.commit()
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
