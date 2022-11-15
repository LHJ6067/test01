from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://jaejeonglee:8d5dqKiseNJdDliN@cluster0.ze5iksx.mongodb.net/?retryWrites=true&w=majority')

reviewDB = client.reviewDB
hospitalInfo = client.hospitalDB.hospitalInfo
userDB = client.userDB
# index-----------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# index-----------------------------------------------------------
@app.route('/hospital/')
def hospital():
    return render_template('hospitals.html')

@app.route("/hospitalInfo", methods=["GET"])
def hospitalInfo_get():
    hospitalInfo_list = list(hospitalInfo.find({}, {'_id': False}))
    return jsonify({'hospitalInfo_list': hospitalInfo_list})

# detailPage-----------------------------------------------------------
@app.route('/hospital/<params>')
def detail(params):
    return render_template('detailPage.html')


# # review
@app.route("/hospital/review/<params_receive>", methods=["POST"])
def review_post(params_receive):
    nickname_receive = request.form['nickname_give']
    review_receive = request.form['review_give']
    hospital_params = params_receive

    reviewtList = list(reviewDB.review.find({}, {'_id': False}))

    count = len(reviewtList) + 1;
    doc = {
        "review_num": count,
        "nickname": nickname_receive,
        "review": review_receive,
        "hospital_params": hospital_params
    }
    reviewDB.review.insert_one(doc)
    return jsonify({'msg': '작성 완료'})

@app.route("/hospital/review", methods=["GET"])
def review_get():
    all_reviews = list(reviewDB.review.find({}, {'_id': False}))
    return jsonify({'review': all_reviews})

@app.route("/hospital/review/<review_num>", methods=["DELETE"])
def review_delete(review_num):
    review_num_receive = request.form['review_num_give']
    reviewDB.review.delete_one({'review_num': int(review_num_receive)})
    return jsonify({'message': "삭제 완료"})
# -----------------------------------------------
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)