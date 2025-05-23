from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = "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"
html_code = '''
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Chatbot mit LLaMA 3.2 3B Instruct</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            width: 400px;
            padding: 25px 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }
        form {
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex-grow: 1;
            padding: 10px 15px;
            border: 1.5px solid #ccc;
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #007bff;
            box-shadow: 0 0 5px rgba(0,123,255,0.5);
        }
        button {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 0 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        .response {
            margin-top: 20px;
            padding: 15px;
            background: #e9f0ff;
            border-left: 5px solid #007bff;
            border-radius: 6px;
            white-space: pre-wrap;
            color: #333;
            font-size: 1rem;
            line-height: 1.4;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chat mit LLaMA 3.2 3B Instruct</h1>
        <form method="post" autocomplete="off">
            <input name="msg" type="text" placeholder="Frag mich etwas..." required autofocus />
            <button type="submit">Senden</button>
        </form>
        {% if response %}
        <div class="response">
            <strong>Antwort:</strong><br>{{ response }}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        msg = request.form["msg"]
        try:
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "meta-llama/llama-3.2-3b-instruct:free",
                "messages": [{"role": "user", "content": msg}]
            }
            r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
            r.raise_for_status()
            response = r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            response = f"Fehler: {e}"
    return render_template_string(html_code, response=response)

if __name__ == "__main__":
    app.run(debug=True)
