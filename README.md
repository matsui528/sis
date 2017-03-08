# nanosearch

## Overview
*nanosearch* is an extremely simple image-based image search engine using Kelas + Flask.
Given a set of images, a 4096D fc6-feature is extracted for each image using a pre-trained VGG16 network (`offline.py`).
Given a query image via a Flask web-intereface, similar images are retrieved by the simple nearest neighbor search (`server.py`).

## Setup
```bash
git clone https://github.com/matsui528/nanosearch.git
cd nanosearch
mkdir -p static/feature static/img static/uploaded
pip3 install numpy Pillow h5py tensorflow Keras Flask 
```

## How to run

### Offline step: feature extraction
```bash
# Put your image files (*.jpg) on static/img
python3 offline.py
# Then fc6 features are extracted and saved on static/feature
```

### Online step: search
```bash
python3 server.py
# Now you can do search via localhost:5000
```