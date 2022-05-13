from flask import Flask
from controllers import CalcController, Index

app = Flask('app')

@app.route('/')
def index():
  return Index.index()
  

@app.route('/sum/<num1>/<num2>')
def soma(num1, num2):
  return CalcController.soma(num1, num2)
  
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)