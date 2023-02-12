from flask import *
from webmashup import mashup

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer=request.form["singer"]
        count=int(request.form["count"])
        duration=int(request.form["duration"])
        email=request.form["email"]
        print(email)
        mashup(singer,count,duration,'mashup.mp3')
        
        return "form submitted to " + email
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=8000)