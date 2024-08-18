from flask import render_template, request, Flask
from .scorepost.create_score_title import create_title
from .scorepost.generate_screenshot import generate_ss
from .scorepost.util.get_score import get_score_info
import time
import os
app = Flask(__name__)

default_title = 'Player | Artist - Beatmap Title [Version] (Creator, 0.00*) 0.00% SS | 0pp'
default_score_img = '/static/default_score.jpg'
not_valid_link_msg = "No score found, please enter a valid score link, user link, or username"
no_score_found = "No score found to generate screenshot"

no_recent_score = "No recent scores"

@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        st = time.time()
        url = request.form['content']
        checkbox = request.form.getlist('checkbox')
        checked = len(checkbox) > 0
        results = ""
        #try:
        score = get_score_info(url)
        if score == None:
            if checked:
                results = no_score_found
            return render_template("home.html", score_title=not_valid_link_msg, image_src=default_score_img, results=results, input=url, checked=checked)
        elif score == -1:
            if checked:
                results = no_score_found
            return render_template("home.html", score_title=no_recent_score, image_src=default_score_img, results=results, input=url, checked=checked)

        print("successfully got score!")

        title = create_title(score)
        
        if checked:
            screenshot_file_name = generate_ss(score)
            score_img = f"/static/scorepost_generator_images/screenshots/{screenshot_file_name}"
            results = "Screenshot successfully generated"
            print("successfully made ss!")
            
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')
    else:
        score_img = default_score_img
        title = default_title
        results = ""
        url=""
        checked=True
    return render_template("home.html", score_title=title, image_src=score_img, results=results, input=url, checked=checked)