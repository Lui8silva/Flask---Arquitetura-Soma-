from flask import redirect, render_template

class CalcController():
  def sum(num1, num2):
    res = int(num1), int(num2)
    return f'Soma = {sum(res)}'

class Index():
  def index():
    return render_template('index.html')