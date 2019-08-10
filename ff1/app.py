from flask import Flask, render_template, redirect, url_for, request
from mongodb import search_all_food, find_recipe
# from data import
app = Flask(__name__)

listFood = []

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/search')
def menu():
    return render_template('menu.html')

@app.route('/search', methods=["POST"])
def search():
    listFood = request.get_json()["data"]
    return '/results/' + ', '.join(str(x) for x in listFood)
    # return "1"

# Chi Phan Anh
@app.route("/results/<listFood>")
def result(listFood):
    a = listFood.split(', ')
    
    if 'hanh' in a:
        num = a.index('hanh')
        a[num]='hanh tay'
    if 'ca' in a:
        num = a.index('ca')
        a[num]='ca chua'

    ls = search_all_food()
    food_select = []
    
    a.sort()
    for u in ls:
        u['kw'].sort()
        if u['kw'] == a:
            food_select.append(u)
        
    if len(food_select) == 0: 
        for v in a:
            for i in ls:
                if v in i['kw']:
                    if i not in food_select:
                        food_select.append(i)
    return render_template('index.html',data=food_select)

# Dung
@app.route('/recipe/<recipe_id>')
def description(recipe_id):
    recipe = find_recipe(recipe_id)
    return render_template('page3.html',food=recipe)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    