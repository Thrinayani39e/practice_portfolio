"""Flask application factory and route definitions."""

import os
import datetime
from flask import Flask, render_template, redirect, url_for, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict
from app.constants import NAV_LINKS, PAGE_TITLES, HOBBIES, PROJECTS, EXPERIENCES, EDUCATION

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database connection
mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

# --- Task 2: TimelinePost Model ---
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

# Connect and create the table
mydb.connect()
mydb.create_tables([TimelinePost])

# --- Task 2: API Endpoints ---
@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
    post = TimelinePost.get_by_id(id)
    post.delete_instance()
    return {"message": f"Post {id} deleted successfully"}

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }
 

# --- Existing Routes ---
@app.context_processor
def inject_globals():
    return {
        "nav_links": NAV_LINKS,
        "url": os.getenv("URL"),
    }

@app.route("/")
def index():
    return redirect(url_for("about"))

@app.route("/about")
def about():
    return render_template("components/about.html", title=PAGE_TITLES["about"], active_page="about")

@app.route("/experience")
def experience():
    return render_template(
        "components/experience.html",
        title=PAGE_TITLES["experience"],
        active_page="experience",
        experiences=EXPERIENCES,
        education=EDUCATION,
    )

@app.route("/projects")
def projects():
    return render_template(
        "components/projects.html",
        title=PAGE_TITLES["projects"],
        active_page="projects",
        projects=PROJECTS,
    )

@app.route("/hobbies")
def hobbies():
    return render_template(
        "components/hobbies.html",
        title=PAGE_TITLES["hobbies"],
        active_page="hobbies",
        hobbies=HOBBIES,
    )
