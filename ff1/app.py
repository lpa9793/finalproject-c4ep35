from flask import Flask, render_template, request, redirect
app = Flask(__name__)

from mongodb import search_all_food, search_food

@app.route('/results')
def index():
    return render_template('index.html', data = search_all_food())

@app.route('/results', methods=['GET'])
def search_result():
    food_keyword = request.form.get('keyword')
    search_food(food_keyword)
    return render_template('index.html', food = search_food(food_keyword))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
