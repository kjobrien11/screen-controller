from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import logging

app = FastAPI()

logger = logging.getLogger("uvicorn")

# HTML control page
@app.get("/", response_class=HTMLResponse)
def control_page():
    return """
<html>
    <head>
        <title>Screen Switcher</title>
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            button {
                width: 100%;
                height: 10vh;
                padding: 10rem;
                font-size: 5rem;
            }
        </style>
    </head>
    <body>
        <button onclick="fetch('/show/mlb')">MLB Live Stats</button>
        <button onclick="fetch('/show/roulette')">Roulette Wheel</button>
        <button onclick="fetch('/show/otters')">Otter Cam</button>
        <button onclick="fetch('/show/alaska')">Alaska Cam</button>
        <button onclick="fetch('/show/panda')">Panda Cam</button>
        <button onclick="fetch('/show/eagle')">Eagles Cam</button>
    </body>
</html>
"""

def launch_chromium(url: str, youtube=False):
    # Kill existing Chromium
    subprocess.run(["pkill", "-f", "chromium"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    args = [
        "chromium-browser",
        "--kiosk",
        "--hide-scrollbars",
        "--disable-overscroll-history-navigation",
        "--autoplay-policy=no-user-gesture-required",
        "--disable-infobars",
        "--disable-session-crashed-bubble",
        "--no-first-run",
        url
    ]
    if youtube:
        args.insert(1, "--app=" + url)

    subprocess.Popen(args)

def click_position(x: int, y: int):
    # Moves mouse and clicks
    subprocess.run([
        "xdotool",
        "mousemove", str(x), str(y),
        "click", "1"
    ])

@app.get("/show/mlb")
def show_mlb():
    logger.info("MLB endpoint hit")
    launch_chromium("http://localhost:4200")
    import time
    time.sleep(10)

    click_position(57, 1037)

    return {"status": "Switched to MLB Live Stats and clicked button"}

@app.get("/show/roulette")
def show_roulette():
    logger.info("Roulette endpoint hit")
    launch_chromium("http://localhost:4201")
    return {"status": "Switched to Roulette Wheel"}

@app.get("/show/otters")
def show_otters():
    logger.info("Otters endpoint hit")
    launch_chromium("https://www.youtube.com/embed/9mg9PoFEX2U?autoplay=1&mute=1&controls=0", youtube=True)
    return {"status": "Switched to Otter Cam"}

@app.get("/show/alaska")
def show_alaska():
    logger.info("Alaska endpoint hit")
    launch_chromium("https://www.youtube.com/embed/73-EekdVVU8?autoplay=1&mute=1&controls=0", youtube=True)
    return {"status": "Switched to Otter Cam"}

@app.get("/show/panda")
def show_pandas():
    logger.info("Panda endpoint hit")
    launch_chromium("https://www.youtube.com/embed/3szkFHfr6sA?autoplay=1&mute=1&controls=0", youtube=True)
    return {"status": "Switched to Otter Cam"}

@app.get("/show/eagle")
def show_eagles():
    logger.info("Eagle endpoint hit")
    launch_chromium("https://www.youtube.com/embed/B4-L2nfGcuE?autoplay=1&mute=1&controls=0", youtube=True)
    return {"status": "Switched to Otter Cam"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("controller:app", host="0.0.0.0", port=5555, reload=True)
