from PIL import Image
import numpy as np 
from fastai.tabular.learner import load_learner
from fastai import *
from fastai.vision import *
import torch
import sys
import warnings

def predict(img):
    # load the pre trained model
    learn_inf = load_learner('export.pkl')
    learn_inf.dls.vocab
    pred_class,pred_idx,probs = learn_inf.predict(img)
    print('predicted Class: {} '.format(pred_class) )
    print('Predicted Probability:{:.3} '.format(float(probs[pred_idx])))

def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# Uploading the File to the Page


args = sys.argv[1:] # read the first argument

# Checking the Format of the page
if args[0] == '-s':        
    # Load a single image for prediction
    img = load_image(args[1])    
    print("Image Uploaded Successfully")
    predict(img)
else:
    print('Use {python <filename.py> s followed by the filename} to run single test image\n \
           Use {python <filename.py> b followed by the filename} to run batch of test images')



