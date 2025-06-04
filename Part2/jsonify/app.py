from flask import Flask

app = Flask(__name__)

@app.route('/api/vi/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result': 'success', 'data': {"feed1":"data1", "feed2":"data2"}}

    return data

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {'result': 'success', 'data': {"feed1": "data1"}}


    return data