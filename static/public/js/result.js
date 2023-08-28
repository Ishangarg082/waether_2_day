
function Dynamic() {
    let weather1 = document.getElementById('weathers').innerText;
    we = weather1.replace(/\s/g, '').toLowerCase();
    if (we == "clouds") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/clouds.gif')";
    }
    if (we == "rain") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/rain.gif')";

    }
    if (we == "clear") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/clear.jpg')";

    }
    if (we == "thunderstorm") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/thunder.gif')";

    }
    if (we == "snow") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/snow.gif')";

    }
    if (we == "drizzle") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/drizzle.gif')";

    }
    if (we == "sand" || we == "dust") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/sand.gif')";

    }
    if (we == "smoke" || we == "fog" || we == "haze" || we == "mist") {
        document.getElementById("here").style.backgroundImage = "url('/static/public/image/fog.gif')";

    }


}