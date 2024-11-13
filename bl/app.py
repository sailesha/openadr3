from flask import Flask, render_template, redirect, url_for
import requests
import json

VTN_URL = "http://localhost:8080/openadr3/3.0.1"

HEADERS = {
    "Content-type": "application/json",
    "Authorization": "Bearer bl_token"
}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create_program", methods=["POST"])
def create_program():
    with open("program.json", "r") as json_file:
        data = json.load(json_file)
    response = requests.post(
        f"{VTN_URL}/programs",
        headers=HEADERS,
        json=data
    )
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Redirect back to the home page after the action
    return redirect(url_for("home"))


@app.route("/create_events", methods=["POST"])
def create_events():
    with open("event_pricing.json", "r") as json_file:
        data = json.load(json_file)
    response = requests.post(
        f"{VTN_URL}/events",
        headers=HEADERS,
        json=data
    )
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Redirect back to the home page after the action
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=8081, debug=True)
