from PIL import Image
from feature_extractor import FeatureExtractor
from pathlib import Path
import numpy as np
import os, re

if __name__ == '__main__':
    fe = FeatureExtractor()

    for img_path in sorted(Path("./static/img").rglob("*.jpg")):
        print(f"Processing: {img_path}")  # e.g., ./static/img/xxx.jpg
        save_path = Path("./static/feature") / re.sub(r"static[\\\/]img[\\\/]|[^\\\/]+$", "", str(img_path))
        try:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
        except:
            print(f"Can't Create Dir: {save_path}")

        try:
            feature = fe.extract(img=Image.open(img_path))
            feature_path = save_path / (img_path.stem + ".npy")  # e.g., ./static/feature/xxx.npy
            np.save(feature_path, feature)
        except:
            print(f"Error: {img_path}")