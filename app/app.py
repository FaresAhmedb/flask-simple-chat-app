from datetime import datetime
from secrets import token_urlsafe

from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__, static_folder="/")
app.static_folder = "/"
cache = {"msgs": {}, "mark": ""}


@app.get("/")
def index():
    """The website root endpoint

    Returns:
        Static[HTML]: index.html
    """

    return app.send_static_file("index.html")


@app.post("/messages/send")
def messages_send():
    """Send a message to the chat

    Returns:
        JSON: Sample -> {
            "status": "sucess",
            "msg": "<pre></pre>",
            "mark": "123456",
        }
    """

    tim = datetime.now().strftime("%H:%M")
    usr = request.form['usr']
    msg = escape(request.form['msg'])

    cache["mark"] = token_urlsafe(6)
    cache["msgs"][cache["mark"]] = f"<pre>[{tim}] {usr}: {msg}</pre>"

    return jsonify(
        {
            "status": "sucess",
            "msg": cache["msgs"][cache["mark"]],
            "mark": cache["mark"],
        }
    )


@app.post("/messages/heartbeat")
def messages_heartbeat():
    """Check for new chat messages

    Returns:
        JSON: Sample -> {
            "status": "outdated/uptodate",
            "msg": "<pre></pre>",
            "mark": "123456",
        }
    """

    client_mark = request.form["mark"]

    if client_mark != cache["mark"]:
        k, v = list(cache["msgs"].keys()), list(cache["msgs"].values())
        return jsonify(
            {
                "status": "outdated",
                "msg": "".join(v[k.index(client_mark) + 1 :][::-1]),
                "mark": cache["mark"],
            }
        )

    return jsonify(
        {
            "status": "uptodate",
        }
    )
