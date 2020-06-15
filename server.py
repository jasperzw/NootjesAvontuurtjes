from flask import Flask, render_template
import json
from random import randint

with open('totalAsiaMergeSortedGeolocated.json') as json_file:
    data = json.load(json_file)


app = Flask(__name__)
@app.route('/')
def index():
    stat = 1
    while stat==1:
        postId = randint(1,len(data))
        caller = 'Post '+str(postId)
        if(data[caller]['URL'][-4:]=='.jpg'):
            title = data[caller]['Title']
            url = data[caller]['URL']
            lat = data[caller]['lat']
            lon = data[caller]['lon']
            stat = 0
            print("current data: ",data[caller])
    return render_template('index.html', url=url, title=title, lat=lat, lon=lon)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
