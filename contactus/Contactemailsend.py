from flask import Flask, render_template, request

app=Flask('MyApp')

@app.route("/")
def main_page():
	render_template("index.html")

@app.route("/signup", methods = ["POST"])
def send_simple_message():
	form_data = request.form
	name = form_data["first_name"]
	email = form_data["email"]
	description = form_data["description"]
    return request.post(
        "https://api.mailgun.net/v3/sandbox97dd5dad9dd04faf84532afa0c98c4e6.mailgun.org/messages",
        auth=("api", "key-7cc88a49eec861c8cd44065ce3d9f901"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox97dd5dad9dd04faf84532afa0c98c4e6.mailgun.org>",
              "to": "El-Ghazali <elghazalias@gmail.com>",
              "subject": "Enquiry form",
              "text": "Name: {}; Email {}; Query:{}".format(first_name, email, description)
              }
    )

send_simple_message()

app.run(debug=True)