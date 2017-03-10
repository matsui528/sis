# Sis: simple image search engine

## Overview
- *sis* is a simple image-based image search engine using Keras + Flask.
- Given a set of images, a 4096D fc6-feature is extracted for each image using a pre-trained VGG16 network (`offline.py`).
- Given a query image via a Flask web-intereface, similar images are retrieved by the simple nearest neighbor search (`server.py`).
- On an aws-ec2 instance with t2.large, the feature extraction takes 0.9 s per image. The search for 1000 images takes 10 ms.
- Demo: [simple-image-search.xyz](http://www.simple-image-search.xyz/)

## Requirement
```bash
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