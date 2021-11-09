from flask import Flask,render_template,request,jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/predict',methods=['POST'])
def predict():
  if request.method == "POST" :

     Loss = int(request.form["Loss"])
     dis = int(request.form["dis"]) 
     Fever = int(request.form["Fever"])
     Bp = int(request.form["Bp"])
     st = int(request.form["st"])

     
     with open('mod','rb') as f:
         model = pickle.load(f)    
     result = model.predict([[Loss, dis, Fever, Bp, st]])
     if result[0] == "covid-19":
       return render_template('index.html',data=["You have covid-19 symptoms consult doctor"])  
     else:
        return render_template('index.html',data=["You have Malaria symptoms consult doctor"])    


if __name__ == "__main__":
    app.run(debug=True)