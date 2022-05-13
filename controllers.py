from flask import redirect, render_template

class CalcController():
  def soma(num1, num2):
    soma = int(num1) + int(num2)
    return f'Soma = {soma}'

class Index():
  def index():
    return render_template('index.html')