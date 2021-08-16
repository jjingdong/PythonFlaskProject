import json
import re

from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import request

from match import match


app = Flask(__name__)
CORS(app)

# define Flask API here



@app.route('/words/', methods=['GET', 'POST'])
def words():  # put application's code here

    if request.method == 'GET':
        file = open('storage.txt', 'r')
        a = file.read()
        if a == '':
            lst_words = []
        else:
            lst_words = a.split(', ')
            file.close()


        args = request.args
        if 'pattern' in args:
            pa = args.get('pattern')
            result = []
            for word in lst_words:
                if match(pa, word):
                    result.append(word)

            return jsonify(result)
        else:
            return jsonify(lst_words)



    elif request.method == 'POST':
        # data = ['apple', 'banana']
        data = request.data
        if data:
            b = data.decode("utf-8")
            words = b.strip('][')
            lst_words = words.split(', ')

            file = open('storage.txt', 'w')
            file.write(words)
            file.close()

            return jsonify(lst_words)
        else:
            return jsonify('Invalid Request')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



