from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('spend_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        income = float(request.form['income'])
        pred = model.predict([[age, gender, income]])[0]
        prediction = round(pred, 2)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
