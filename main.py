from flask import Flask
import random

app = Flask(__name__)
#
# def decorator(function):
#     def wrapper(*args):
#         number = function(*args)
#         if number
random_number = str(random.randint(0,10))

@app.route("/")
def guess_number():
    return ("<h1>Guess a number between 0 and 9</h1> <img src='https://media3.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy."
            "gif?cid=ecf05e471rbiyotx8snzd3fokidf5kistb1y7n5q58ut5104&ep=v1_gifs_search&rid=giphy.gif&ct=g'</src>")



@app.route("/<number>")
def random_num(number):
    if number == random_number:
        return ("<h1 style='color: green'>You GOT IT</h1>"
                "<img src='https://media4.giphy.com/media/chzz1FQgqhytWRWbp3/200w.webp?"
                "cid=ecf05e473600ck5p8q1qwpg4gi5nqj3one3c5g0gnvxc9r92&ep=v1_gifs_search&rid=200w.webp&ct=g'</img>")
    elif number < random_number:
        return ("<h1 style='color: red'>Too LOW! Try again</h1>"
                "<img src='https://media0.giphy.com/media/IevhwxTcTgNlaaim73/200w."
                "webp?cid=ecf05e47nck4fydkkdw0da1vzsf09h67closxlm2l94xi2ml&ep=v1_gifs_search&rid=200w.webp&ct=g'</img>")
    elif number > random_number:
        return ("<h1 style='color: black'>Too HIGH! Try again</h1>"
                "<img src='https://media1.giphy.com/media/LfpjDLDpGvmbS/giphy."
                "webp?cid=ecf05e47ci3aghxt17v2rlwzw5b27m7276x34b8pan13deq6&ep=v1_gifs_search&rid=giphy.webp&ct=g'</img>")


if __name__ == "__main__":
    app.run(debug=True)