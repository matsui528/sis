# Sis: Simple Image Search Engine

## [Demo](http://www.simple-image-search.xyz/)
![](http://yusukematsui.me/project/sis/img/screencapture2.jpg)

## Workflow
![](http://yusukematsui.me/project/sis/img/overview.jpg)

## Overview
- *Sis* is a simple image-based image search engine using Keras + Flask. You can launch the search engine just by running two python scripts.
- `offline.py`: This script extracts deep features from images. Given a set of database images, a 4096D fc6-feature is extracted for each image using the VGG16 network with ImageNet pre-trained weights.
- `server.py`: This script runs a web-server. You can send your query image to the server via a Flask web-intereface. Then relevant images to the query are retrieved by the simple nearest neighbor search.
- On an aws-ec2 instance with t2.large, the feature extraction takes 0.9 s per image. The search for 1000 images takes 10 ms. We tested Sis on Ubuntu 16.04 with Python3.

## Links
- [Demo](http://www.simple-image-search.xyz/)
- [Project page](http://yusukematsui.me/project/sis/sis.html)
- [Tutorial](https://ourcodeworld.com/articles/read/981/how-to-implement-an-image-search-engine-using-keras-tensorflow-with-python-3-in-ubuntu-18-04) and [Video](https://www.youtube.com/watch?v=Htu7b8PUyRg) by [@sdkcarlos](https://github.com/sdkcarlos)

## Usage
```bash
# Clone the code and install libraries
$ git clone https://github.com/matsui528/sis.git
$ cd sis
$ pip install -r requirements.txt

# Put your image files (*.jpg) on static/img

$ python offline.py
# Then fc6 features are extracted and saved on static/feature
# Note that it takes time for the first time because Keras downloads the VGG weights.

$ python server.py
# Now you can do the search via localhost:5000
```
## Launch on AWS EC2
- You can easily launch Sis on AWS EC2 as follows. Note that the following configuration is just for the demo purpose, which would not be secure.
- To run the server on AWS, please first open the port 5000 and launch an EC2 instance. Note that you can create a security group such that port 5000 is opened.
- A middle-level CPU instance is fine, e.g., m5.large.
- After you log in the instance by ssh, the easist way to setup the environment is to use anaconda:
```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh
$ bash Anaconda3-5.3.1-Linux-x86_64.sh # Say yes for all settings
$ source ~/.bashrc  # Activate anaconda
```
- You might need to use python3.6 because currently tensorflow doesn't support 3.7: `conda install python=3.6`. Otherwise please create a new conda environment with python=3.6.
- Then let's run the commands in the above usage section.
- After you run `$ python server.py`, you can access the system via `http://ec2-XX-XX-XXX-XXX.us-west-2.compute.amazonaws.com:5000`
- (Advanced) If you'd like to deploy the system properly, please consider to run the Sis with the usual web server, e.g., uWSGI + nginx.



## Citation

    @misc{sis,
	    author = {Yusuke Matsui},
	    title = {Sis: Simple Image Search Engine},
	    howpublished = {\url{https://github.com/matsui528/sis}}
    }
