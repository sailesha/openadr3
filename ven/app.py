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


@app.route("/create_ven", methods=["POST"])
def create_ven():
    with open("ven.json", "r") as json_file:
        data = json.load(json_file)
    ven_response = requests.post(
        f"{VTN_URL}/vens",
        headers=HEADERS,
        json=data
    )
    print("Status Code:", ven_response.status_code)
    print("VEN response Body:", ven_response.json())

    with open("resource.json", "r") as json_file:
        data = json.load(json_file)
    resource_response = requests.post(
        f"{VTN_URL}/vens/0/resources",
        headers=HEADERS,
        json=data
    )
    print("Status Code:", resource_response.status_code)
    print("VEN resource response Body:", resource_response.json())

    # Redirect back to the home page after the action
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=8082, debug=True)
