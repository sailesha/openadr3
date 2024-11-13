from flask import Flask, render_template, redirect, url_for
import requests
import json
import pricing
from datetime import datetime

VTN_URL = "http://localhost:8080/openadr3/3.0.1"

HEADERS = {
    "Content-type": "application/json",
    "Authorization": "Bearer bl_token"
}

day_ahead_prices = pricing.get_day_ahead_prices()

app = Flask(__name__)

@app.route("/")
def home():
    hours = [info.hour for info in day_ahead_prices]
    prices = [info.price for info in day_ahead_prices]
    return render_template("index.html", hours=hours, prices=prices)


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
    
    today_date = start_date = (datetime.now()).strftime("%Y%m%d")
    data["intervalPeriod"]["start"] = f"{today_date}T00:00:00.000Z"
    data["intervals"] = _get_intervals(day_ahead_prices)
    
    response = requests.post(
        f"{VTN_URL}/events",
        headers=HEADERS,
        json=data
    )
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

    # Redirect back to the home page after the action
    return redirect(url_for("home"))


def _get_intervals(prices):
    intervals = []
    interval_id = 0
    for price in prices:
        payload = {
            "type": "PRICE",
            "values": [
                price.price / 1000  # Convert from $/MWh to $/kWh
            ],
        }
        interval = {
            "id": interval_id,
            "payloads": [payload],
        }
        intervals.append(interval)
        interval_id += 1
    return intervals


if __name__ == "__main__":
    app.run(port=8081, debug=True)
