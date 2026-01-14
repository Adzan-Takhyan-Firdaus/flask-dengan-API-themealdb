from flask import Flask, render_template
import requests as req

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s='
    try:
        res = req.get(url, timeout=5)
        data = res.json()['meals']
    except:
        data = []
        
    return render_template('index.html', products=data, title="Menu Rekomendasi")

@app.route('/categories')
def categories_list():
    url = 'https://www.themealdb.com/api/json/v1/1/categories.php'
    try:
        res = req.get(url, timeout=5)
        data = res.json()['categories']
    except:
        data = []
    return render_template('categories.html', categories=data)

@app.route('/category/<name>')
def category_items(name):
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={name}'
    try:
        res = req.get(url, timeout=5)
        data = res.json()['meals']
    except:
        data = []
    
    return render_template('index.html', products=data, title=f"Kategori: {name}")

@app.route('/product/<id>')
def product(id):
    url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}'
    res = req.get(url, timeout=20)
    meal_data = res.json()['meals'][0]
    
    daftar_bahan = []

    for i in range(1, 21):
        ingredient = meal_data.get(f'strIngredient{i}')
        measure = meal_data.get(f'strMeasure{i}')

        if ingredient and ingredient.strip():
            daftar_bahan.append({
                'nama': ingredient,
                'takaran': measure,
                'gambar': f'https://www.themealdb.com/images/ingredients/{ingredient}.png'
            })
   
    return render_template('product.html', product=meal_data, ingredients=daftar_bahan)

@app.route('/about')
def about():
    tim_kita = [
        {"nama": "Adzan Takhyan Firdaus", "nim": "312410043", "foto": "/static/src/adzan.jpg"},
        {"nama": "Dimas Anggraito Wicaksono",   "nim": "312410585", "foto": "/static/src/dimas.jpg"},
        {"nama": "Muhammad Khoirul Anam",    "nim": "312410013", "foto": "/static/src/anam.jpg"},
        {"nama": "Nabila Rahmadani",   "nim": "312410656", "foto": "/static/src/bila.jpeg"},
        {"nama": "Wulan Melinda",  "nim": "312410028", "foto": "/static/src/wulan.jpeg"},
    ]
    return render_template('about.html', tim=tim_kita, title="Our Chef Team")

if __name__=='__main__':
    app.run(debug=True)