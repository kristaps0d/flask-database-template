from flask import render_template

def PageNotFound():
    return render_template('404.html')

def PageForbidden():
    return render_template('403.html')