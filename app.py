from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://jaejeonglee:wjdwo2538!@cluster0.ze5iksx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# index-----------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# index-----------------------------------------------------------
@app.route('/hospital')
def hospaial():
    return render_template('hospitals.html')
# detailPage-----------------------------------------------------------
@app.route('/hospital/1')
def detail():
    return render_template('detailPage.html')


# -----------------------------------------------
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)