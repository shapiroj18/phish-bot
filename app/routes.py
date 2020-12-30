import datetime
from app import app, mail
from app.tasks import timed_functions
from flask import render_template, url_for
from flask_mail import Mail, Message
from app import phishnet_api, phishin_api

phishnet_api = phishnet_api.PhishNetAPI()
phishin_api = phishin_api.PhishINAPI()


@app.route("/")
def hello():
    return "Listen to the Japan 2000 Tour"


@app.route("/radio")
def radio():
    return f"Phish Radio"


@app.route("/process/<name>")
def process(name):
    testing.reverse.delay(name)
    return "Async sent"


@app.route("/emailtest")
def emailtest():
    song, date = phishnet_api.get_random_jamchart()
    jam_url = phishin_api.get_song_url(song=song, date=date)
    relisten_formatted_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
        "%Y/%m/%d"
    )
    phishnet_url = phishnet_api.get_show_url(date)

    with app.app_context():
        msg = Message(
            subject="Daily Phish Jam",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["shapiroj18@gmail.com"],
        )
        msg.html = render_template(
            "random_jam_email.html",
            song=song,
            date=date,
            jam_url=jam_url,
            relisten_formatted_date=relisten_formatted_date,
            phishnet_url=phishnet_url,
        )
        mail.send(msg)
    return "Mail sent"
