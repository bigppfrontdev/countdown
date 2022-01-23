import copy
import random
from flask import Flask, render_template, request, jsonify
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})


@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

app = Flask(__name__)



def number_game():
    amount = random.randint(2,4)
    small_numbers = [x for x in range(1, 10)]
    big_numbers = [25, 50 ,75, 100]
    final = []
    for i in range(amount):
        yeet = random.choice(small_numbers)
        final.append(yeet)
        small_numbers.remove(yeet)
    for i in range(6-amount):
        yeet = random.choice(big_numbers)
        final.append(yeet)
        big_numbers.remove(yeet)
    equ = ["/", "*","+","-"]
    bossman = copy.deepcopy(final)

    yeet1 = random.choice(bossman)
    bossman.remove(yeet1)


    for i in range(random.randint(3,4)):
        nem = random.choice(equ)
        yeet = random.choice(bossman)
        print(bossman)
        bossman.remove(yeet)


        if nem == "/":
            if yeet1 % yeet == 0:
                yeet1 = yeet1 / yeet
        if nem == "*":
            yeet1 = yeet1 * yeet
        if nem == "-":
            yeet1 = yeet1 - yeet
        if nem == "+":
            yeet1 = yeet1 + yeet

    answer = yeet1

    print(final, answer)
    return [final, answer]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/numbers')
def numbers():
    return render_template("numbers.html")

@app.route('/give_numbers', methods=["GET"])
def give_numbers():
    if request.method == "GET":
        nums_ans = number_game()
        nums = nums_ans[0]
        ans = nums_ans[1]

        return jsonify(nums,ans)




@app.route("/test_numbers", methods=["POST"])
def test_numbers():
    if request.method == "POST":
        request_data = request.json
        number = request_data["numbers"]
        number = eval(number)










if __name__ == '__main__':
   app.run()




print(add_numbers())
