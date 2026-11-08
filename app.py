
from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>BILAL PRO</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    background: #101020;
    color: white;
    font-family: Arial;
    text-align: center;
    padding: 20px;
}
.container {
    max-width: 450px;
    margin: auto;
    background: #20203a;
    padding: 22px;
    border-radius: 15px;
}
input, textarea, button {
    box-sizing: border-box;
    width: 100%;
    padding: 13px;
    margin: 10px 0;
    border-radius: 8px;
}
button {
    background: #7045ff;
    color: white;
    border: 0;
    font-weight: bold;
}
textarea { height: 100px; }
</style>
</head>
<body>
<div class="container">
<h1>BILAL PRO</h1>
<p>Personal Message Preview Tool</p>
<form method="POST">
<textarea name="message" placeholder="Enter your message" required>{{message}}</textarea>
<input type="number" name="count" min="1" max="100"
placeholder="Repeat count (1-100)" required>
<button type="submit">Generate Preview</button>
</form>
{% if results %}
<h3>Message Preview</h3>
{% for item in results %}
<p>{{item}}</p>
{% endfor %}
{% endif %}
<p>Created By: BILAL</p>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        try:
            count = int(request.form.get("count", "1"))
        except ValueError:
            count = 0

        if message and 1 <= count <= 100:
            results = [
                f"{i}. {message}"
                for i in range(1, count + 1)
            ]

    return render_template_string(
        PAGE, message=message, results=results
    )

if __name__ == "__main__":
    app.run()
  
