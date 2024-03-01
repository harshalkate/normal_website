from flask import Flask,render_template,request,jsonify,redirect,url_for

app = Flask("__name__")

@app.route('/')
def home():
    return render_template("index.html", name="harshal",learning="Data Science")
@app.route('/profile')
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html",name=name)
@app.route('/json')
def get_json():
    return jsonify({'name':'Harshal','website_name':'Unknown'})

@app.route('/data')
def get_data():
    data = request.json
    return jsonify(data)

@app.route('/go_to_home')
def go_to_home():
    return redirect(url_for("app.get_json"))




if __name__=="__main__":
    app.run(debug=True)