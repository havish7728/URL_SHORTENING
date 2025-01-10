from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory data structures for URL mapping
url_map = {}
reverse_map = {}

# Base URL
BASE_URL = "http://127.0.0.1:5000/"
CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def generate_short_url():
    """Generate a random 6-character short URL."""
    import random
    return ''.join(random.choices(CHARACTERS, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if long_url in reverse_map:
            short_url = reverse_map[long_url]
        else:
            short_url = generate_short_url()
            while short_url in url_map:
                short_url = generate_short_url()
            url_map[short_url] = long_url
            reverse_map[long_url] = short_url
        
        return render_template('result.html', short_url=BASE_URL + short_url, long_url=long_url)
    return render_template('index.html')

@app.route('/<short_key>')
def redirect_to_long_url(short_key):
    long_url = url_map.get(short_key)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)