'''
https://github.com/amueller/word_cloud/blob/master/examples/masked.py
'''

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def displayWordCloud(data = None, backgroundcolor = 'white', width=800, height=600 ):
    wordcloud = WordCloud(stopwords = STOPWORDS
    , background_color = backgroundcolor, width = width, height = height).generate(data)
    plt.figure(figsize = (15 , 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show() 

def makeWordCloudImage(text = None):
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "alice.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()

text = open('alice.txt').read()
displayWordCloud(text)
# makeWordCloudImage(text)