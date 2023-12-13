from flask import Flask, request, render_template_string, render_template, make_response
import os

app = Flask(__name__)
FLAG = os.getenv("FLAG") 
MAX_LENGTH = 20

def waf(string):
    blacklist = ["{{", "_", "'", "\"", "[", "]", "|", "eval", "os", "system", "env", "import", "builtins", "class", "flag", "mro", "base", "config", "query", "request", "attr", "set", "glob", "py"]
    for word in blacklist:
        if word in string.lower()[:MAX_LENGTH]:
            return False
    return True

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/render", methods = ["GET"])
def render():
    template = request.args.get("template")
    variable = request.args.get("variable")
    if len(template) == 0 or len(variable) == 0:
        return "Missing parameter required"
    if len(template) > MAX_LENGTH or len(variable) > MAX_LENGTH:
        return "Input too long"
    if not waf(template) or not waf(variable):
        return "Try harder broooo =)))"
    data = template.replace("{FLAG}", FLAG).replace("{variable}", variable)
    return render_template_string(data)

@app.route("/source", methods = ["GET", "POST"])
def source():
    response = make_response(open("./app.py", "r").read(), 200)
    response.mimetype = "text/plain"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
