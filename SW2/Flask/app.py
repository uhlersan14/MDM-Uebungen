from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello2, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {subpath}'

@app.route("/test", methods=["GET"])
def test():
    # Hole den 'text'-Parameter aus der URL
    text = request.args.get("text")

    # Überprüfe, ob der 'text'-Parameter leer ist
    if text == "" or text is None:
        return "Please use the 'text' parameter in the GET URL"
    
    # Gib den 'text'-Parameter zurück
    return text