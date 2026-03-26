from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "123"

PRODUCTS = ["Laptop", "Phone", "Shoes"]

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form["username"]
        return redirect("/home")
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/add/<product>")
def add(product):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product)
    return redirect("/cart")

@app.route("/cart")
def cart():
    return render_template("cart.html", items=session.get("cart", []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
