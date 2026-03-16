from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/mmCM")
def a():
    return send_from_directory("files", "mmCM.pkg")

@app.route("/WebManMod")
def b():
    return send_from_directory("files", "WebManMod.pkg")

@app.route("/PKGi")
def c():
    return send_from_directory("files", "PKGi.pkg")

@app.route("/raps")
def d():
    return send_from_directory("files", "raps.zip")

@app.route("/ReActPSN")
def e():
    return send_from_directory("files", "ReActPSN.pkg")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
