from flask import Flask, render_template_string, request

app = Flask(__name__)

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>MOLAPO CYBERSECURITY</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f5f5f5;
        }

        .box {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 320px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            box-sizing: border-box;
        }

        button {
            width: 100%;
            margin-top: 15px;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>MOLAPO CYBERSECURITY</h2>

        <form method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>

        <p><small>For educational/demo purposes only.</small></p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")

        return f"""
        <h2>Welcome, {username}!</h2>
        <p>This is a demo application. No password was stored.</p>
        """

    return render_template_string(LOGIN_PAGE)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5678, debug=True)
