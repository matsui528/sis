import os
import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
import glob
import pickle

from datetime import datetime

from flask import Flask, request, render_template

app = Flask(__name__)

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in glob.glob("static/feature/*"):
    features.append(pickle.load(open(feature_path, 'rb')))
    img_paths.append('static/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['query_img']

        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
        img.save(uploaded_img_path)

        query = fe.extract(img)
        dist = np.linalg.norm(features - query, axis=1)  # Do search
        ids = np.argsort(dist)[:30]
        dist = [dist[id] for id in ids]
        retrieved_img_paths = [img_paths[id] for id in ids]

        return render_template('index.html',
                               query_path=uploaded_img_path,
                               scores=zip(dist, retrieved_img_paths))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run()
