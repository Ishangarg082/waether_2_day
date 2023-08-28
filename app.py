from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def weather_home():
    return render_template("home.html")


@app.route("/weather", methods=["POST"])
def get_data():
    try:
        name = request.form["data"]

        response = get_weather_report(name)
        temperature = "{0:.2f}".format(response["main"]["temp"])
        feels_like = "{0:.2f}".format(response["main"]["feels_like"])
        temp_min = "{0:.2f}".format(response["main"]["temp_min"])
        temp_max = "{0:.2f}".format(response["main"]["temp_max"])
        humidity = response["main"]["humidity"]
        weather = response['weather'][0]['main']
        location = response['name']
        country = response["sys"]["country"]
    except:
        return render_template("Error.html")

    return render_template("result.html",
                           temperature=temperature,
                           feels_like=feels_like,
                           temp_max=temp_max,
                           temp_min=temp_min,
                           humidity=humidity,
                           weather=weather,
                           location=location,
                           country=country
                           )


def get_weather_report(data):

    api_key = "acba3dd29e1f3b819df2ed03f7635d14"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={data}&units=metric&appid={api_key}"

    result = requests.get(api_url)
    return result.json()


if __name__ == "__main__":
    app.run(debug=True)
