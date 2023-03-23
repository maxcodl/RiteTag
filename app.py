from flask import Flask, render_template, request
from ritetag import RiteTagApi
from nltk.tokenize import word_tokenize

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/result', methods=['POST'])
def result():
    access_token = '2fe342b61da1aacf32d3429496c82a8bb968267277c1'
    client = RiteTagApi(access_token)

    def limit_80_percentage_reached(limit):
        message = 'Used {}% of API credits. The limit resets on {}'.format(limit.usage, limit.reset)
        print(message)

    client.on_limit(80, limit_80_percentage_reached)

    text = request.form['text']
    hashtags = client.hashtag_suggestion_for_text(text)

    return render_template('result.html', hashtags=hashtags)


if __name__ == '__main__':
    app.run(debug=True)

app.run(host='0.0.0.0', port=5000)