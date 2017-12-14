# Sis: Simple Image Search Engine

[Demo](http://www.simple-image-search.xyz/) | Workflow
:---:|:---:
![](http://yusukematsui.me/project/sis/img/screencapture.jpg)|![](http://yusukematsui.me/project/sis/img/overview.jpg)

## Overview
- *Sis* is a simple image-based image search engine using Keras + Flask. You can launch the search engine just by running two python scripts.
- `offline.py`: This script extracts deep features from images. Given a set of database images, a 4096D fc6-feature is extracted for each image using the VGG16 network with ImageNet pre-trained weights.
- `server.py`: This script runs a web-server. You can send your query image to the server via a Flask web-intereface. Then relevant images to the query are retrieved by the simple nearest neighbor search.
- On an aws-ec2 instance with t2.large, the feature extraction takes 0.9 s per image. The search for 1000 images takes 10 ms.
- We tested the system on Ubuntu 16.04 with Python3.

## Links
- [Project page](http://yusukematsui.me/project/sis/sis.html)
- [Demo](http://www.simple-image-search.xyz/)

## How to run
```bash
# Clone the code and install libraries
$ git clone https://github.com/matsui528/sis.git
$ cd sis
$ pip install -r requirements.txt

# Put your image files (*.jpg) on static/img

$ python offline.py
# Then fc6 features are extracted and saved on static/feature

$ python server.py
# Now you can do the search via localhost:5000
```
## Launch on AWS EC2
- To run the server on AWS, please first launch an EC2 instance and open the port 5000.
- A middle-level CPU instance is fine, e.g., m4.large.
- After you log in the instance by ssh, please run the command above.
- After you run `$ python server.py`, you can access the system via `http://ec2-XX-XX-XXX-XXX.us-west-2.compute.amazonaws.com:5000`


## Citation

    @misc{sis,
	    author = {Yusuke Matsui},
	    title = {Sis: Simple Image Search Engine},
	    howpublished = {\url{https://github.com/matsui528/sis}}
    }