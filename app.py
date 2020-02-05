from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///previousfiles.db'
db = SQLAlchemy(app)

class Queries(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.Text, nullable=False)
	originalText = db.Column(db.Text)
	word_frequencies = db.Column(db.Text)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<File %r>' % self.filename

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		text = request.form['originalText']
		filename = request.form['filename']
		stopwords = request.form.get('stopwords')
		new_task = Queries(filename=filename, originalText=text)
		return redirect('/')

		# try:
		# 	db.session.add(new_task)
		# 	db.session.commit()
		# 	return redirect('/')
		# except:
		# 	print(request.form['filename'])
		# 	return 'There was an issue adding your task'

	else:
		tasks = Queries.query.order_by(Queries.date_created).all()
		return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
	app.run(debug=True)