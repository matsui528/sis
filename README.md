# Sis: simple image search engine

## Overview
- *sis* is a simple image-based image search engine using Keras + Flask.
- Given a set of images, a 4096D fc6-feature is extracted for each image using a pre-trained VGG16 network (`offline.py`).
- Given a query image via a Flask web-intereface, similar images are retrieved by the simple nearest neighbor search (`server.py`).
- On an aws-ec2 instance with t2.large, the feature extraction takes 0.9 s per image. The search for 1000 images takes 10 ms.
- [Project page](https://www.hal.t.u-tokyo.ac.jp/~matsui/project/sis/sis.html)
- [Demo](http://www.simple-image-search.xyz/)

## Requirements
```bash
$ pip install numpy Pillow h5py tensorflow Keras Flask   # python3
```

## How to run (on your local computer)
```bash
# Make sure numpy, Pillow, h5py, tensorflow, Keras, and Flask are installed
# Clone the code
$ git clone https://github.com/matsui528/sis.git
$ cd sis

# Put your image files (*.jpg) on static/img

$ python offline.py    # python3
# Then fc6 features are extracted and saved on static/feature

$ python server.py
# Now you can do search via localhost:5000
```

## How to run (on AWS EC2)
```bash
# Launch an instance on AWS EC2, and open the port 5000.
# A middle-level CPU instance is fine, e.g., m4.large.
# Make sure you can ssh. Then log in the instance.

# Setup python stuff
$ wget https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh
$ bash Anaconda3-4.3.0-Linux-x86_64.sh
$ source ~/.bashrc  # Activate anaconda
$ pip install tensorflow keras

# Clone the code
$ git clone https://github.com/matsui528/sis.git
$ cd sis

# Put your image files (*.jpg) on static/img

$ python offline.py
# Then fc6 features are extracted and saved on static/feature

$ python server.py
# Now you can do search via http://ec2-XX-XX-XXX-XXX.us-west-2.compute.amazonaws.com:5000
```
