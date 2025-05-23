from flask import Flask, request, render_template_string
from ai import simple_ai_response

html_code = '''
<!DOCTYPE html>
<html>
<head><title>Chatbot</title></head>
<body>
    <h1>Chatbot</h1>
    <form action="/" method="post">
        <input name="msg" type="text" placeholder="Deine Nachricht">
        <button type="submit">Senden</button>
    </form>
    {% if response %}
        <p><strong>Antwort:</strong> {{ response }}</p>
    {% endif %}
</body>
</html>
'''

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form["msg"]
        response = simple_ai_response(user_input)
    return render_template_string(html_code, response=response)

if __name__ == "__main__":
    app.run(debug=True)
