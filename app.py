from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')  # أو index.html لو دمجت الفورمين

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return f'Search query: {query}'

@app.route('/login', methods=['GET', 'POST'])  # ← لازم تكون GET و POST
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f'Logged in as: {username}'
    return render_template('login.html')  # ← لازم يكون موجود

if __name__ == '__main__':
    app.run(debug=True)
