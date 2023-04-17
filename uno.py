from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "products")
   categoria = int(request.args.get('categoria'))
   table = df[df["category_id"] == categoria].sort_values(by="product_name")
   tabella = table.to_html()
   return render_template('risultato.html', tabella = tabella)

@app.route('/esercizio2',methods = ["GET"])
def esercizio2():
   import pandas as pd
   df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name = "products")
   estremo_minore = int(request.args.get('estremo_minore'))
   estremo_maggiore = int(request.args.get('estremo_maggiore'))
   table = df[(df["list_price"] >= estremo_minore) & (df["list_price"] <= estremo_maggiore)].sort_values(by="list_price", ascending = False)
   tabella = table.to_html()
   return render_template('risultato2.html', tabella = tabella)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)