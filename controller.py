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
    </body>
</html>
"""

def launch_chromium(url: str):
    # Kill any existing Chromium instances
    subprocess.run(["pkill", "-f", "chromium"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Launch Chromium in kiosk mode
    subprocess.Popen([
        "chromium-browser",
        "--kiosk",
        url
    ])

@app.get("/show/mlb")
def show_mlb():
    logger.info("MLB endpoint hit")
    launch_chromium("http://localhost:4200")
    return {"status": "Switched to MLB Live Stats"}

@app.get("/show/roulette")
def show_roulette():
    logger.info("Roulette endpoint hit")
    launch_chromium("http://localhost:4201")
    return {"status": "Switched to Roulette Wheel"}

@app.get("/show/otters")
def show_otters():
    logger.info("Otters endpoint hit")
    launch_chromium("https://www.youtube.com/watch?v=9mg9PoFEX2U&autoplay=1&mute=1")
    return {"status": "Switched to Otter Cam"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("controller:app", host="0.0.0.0", port=5555, reload=True)
