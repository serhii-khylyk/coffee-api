from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/', methods=['POST'])
def coffee():
    if request.method == 'POST':
        payment = float(request.json['payment'])
        if payment < 2.0:
            return 'Espresso'
        elif payment > 2.0 and payment < 3.0:
            return 'Latte'
        else:
            return 'Cappuccino'
    else:
        return 'Wrong Method'
if __name__ == '__main__':
    app.run()