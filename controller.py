from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import logging

app = FastAPI()

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

@app.get("/show/mlb")
def show_mlb():
    logger.info("MLB endpoint hit")
    subprocess.run([
        "xdotool",
        "search", "--onlyvisible", "--class", "chromium",
        "windowactivate", "--sync",
        "key", "Ctrl+L", "type", "http://localhost:4200", "key", "Return"
    ])
    return {"status": "Switched to MLB Live Stats"}

@app.get("/show/otters")
def show_otters():
    logger.info("Otters endpoint hit")
    subprocess.run([
        "xdotool",
        "search", "--onlyvisible", "--class", "chromium",
        "windowactivate", "--sync",
        "key", "Ctrl+L",
        "type", "https://www.youtube.com/watch?v=9mg9PoFEX2U",
        "key", "Return"
    ])
    return {"status": "Switched to Otter Cam"}

@app.get("/show/otters")
def show_roulette():
    logger.info("otters endpoint hit")
    subprocess.run([
        "xdotool",
        "search", "--onlyvisible", "--class", "chromium",
        "windowactivate", "--sync",
        "key", "Ctrl+L", "type", "https://www.youtube.com/watch?v=9mg9PoFEX2U", "key", "Return"
    ])
    return {"status": "Switched to Roulette Wheel"}


import logging
logger = logging.getLogger("uvicorn")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("controller:app", host="0.0.0.0", port=5555, reload=True)
