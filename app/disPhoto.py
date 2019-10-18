from flask import render_template, url_for, session
from app import webapp


@webapp.route('/disPhoto')
def disPhoto():
    error_dis = None
    if 'error_dis' in session:
        error_dis = session['error_dis']
    return render_template("disPhoto.html", error_dis=error_dis)