from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/add_food', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('food_form.html')
    elif request.method =="POST":
        form = request.form
        t = form["title"]
        l = form["link"]
        print(t ,l)
        return "POST"

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register_form.html')
    elif request.method == "POST":
        form = request.form
        u = form['username']
        p = form['password']
        print(u , p)
        return "Register"
  
if __name__ == '__main__':
  app.run(debug=True)