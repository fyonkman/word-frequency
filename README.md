Fiona Yonkman

To run this app:

1. pip install flask, flask_sqlalchemy
2. Run app.py
3. Go to the address http://127.0.0.1:5000/

Functionality of this app:

1. User may upload .txt files from their computer (or input their own text) and
    the text will be put into the textbox for the user to check.
2. Check or uncheck stopwords checkbox to filter out the most common words.
3. Click the "Count!" button to find out the top 25 most frequent words and
    their frequencies. The data is displayed in a table.
4. When a file (or inputted text) is analyzed, it is saved in a database (shown
    by a table) with its filename and date created.
5. To compare a previously-analyzed text, click the view button next to the
    appropriate query and the word frequency table will be displayed below
    the most recent word frequency table.

Class structure:

1. app.py is a Python file that acts as the controller between the text-analysis
    model.py file and the view (index.html). It also contains the class object
    Query.
2. model.py contains two functions that process the inputted text to return a
    dictionary of word frequencies. There is also a function which stems the
    words.
3. index.html controls the view of the webpage.
4. style.css handles style for index.html.
5. script.js is a JavaScript file that handles uploading a .txt file from the
    user's computer.
6. previousfiles.db stores information from previous queries.
7. modelUnitTests.py is a file of unit tests for the functions in model.py.
8. stopwordslist.txt contains a list of the most common words that a user can
    choose to omit from the word frequency analysis. It is a pickled list.

Notes on .db file:

If the .db file gets deleted, create a blank .db file:
1. open python shell
2. from app import db
3. db.create_all()
