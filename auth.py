from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)
#render_template for the return of the pages. Create html page for each of the routes. 
@auth.route('/contact')
def contact():
    return "<p>Contact</p>" #render templates for these existing pages

@auth.route('/video')
def video():
    return render_template("video.html") #Tab shows Premiere pro work and results -Only show the results and the work in progress of video editing-

@auth.route('/technical')
def technical():
    return "<p>Technical Analysis</p>" #Tab to show the project on Forex -Add a few pictures of winning and losing trades along with what I learned-

@auth.route('/stockpitch')
def stockpitch():
    return "<p>stockpitch - Coming Soon</p>" #only upload the greenwood proect online pitch competition with the stamp. -Use webm or different type-

@auth.route('/journal')
def journal():
    return render_template("journal.html") #Uoload example of pictures and what they have done for me

@auth.route('/iiewae')
def iiewae():
    return render_template("iiewae.html") #display product in an excel and explain the process and formulas. 

