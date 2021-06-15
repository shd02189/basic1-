from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbnewprac1

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']
    industry_receive = request.form['industry_give']
    product_receive = request.form['product_give']
    link_receive = request.form['link_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name' : name_receive,
        'industry' : industry_receive,
        'product' : product_receive,
        'link': link_receive,
        'comment': comment_receive
    }

    db.company.insert_one(doc)

    return jsonify({'msg': '작성완료!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.company.find({}, {'_id': False}))
    return jsonify({'all_reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)