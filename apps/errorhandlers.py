from flask import render_template

#ERROR HANDLERS

def error_401(e):
    #mc is for the menu highlighting, which in this case should not be set
    return render_template('home/401.html',mc=""),401


def error_404(e):
    #mc is for the menu highlighting, which in this case should not be set
    return render_template('home/404.html',mc=""),404


def error_500(e):
    #mc is for the menu highlighting, which in this case should not be set
    return render_template('/home/500.html', mc=""),500