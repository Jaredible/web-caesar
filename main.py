from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="{rot}">
                <p class="error">{rot_error}</p>
            </div>

            <textarea type="text" name="text">{text}</textarea><br>
            
            <input type="submit">
        </form>
    </body>
</html>
"""

def is_integer(var):
    try:
        int(var)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    return form.format(rot='', rot_error='', text='')

@app.route("/", methods=['POST'])
def encrypt():
    rot = cgi.escape(request.form['rot'].strip())
    text = cgi.escape(str(request.form['text']))

    rot_error = ''

    if not is_integer(rot):
        return form.format(rot=rot, rot_error='Not a valid integer', text=text)
    else:
        return form.format(rot='', rot_error=rot_error, text=rotate_string(text, rot=int(rot)))

app.run()