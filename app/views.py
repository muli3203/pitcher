from flask import render_template
from app import app

#Views
@app.route('/pitcher/<int:pitcher_id>')
def index():
    '''
    View the root page function that returns the index page and its data.
    '''
    return render_template('pitcher.html', id = pitcher_id)