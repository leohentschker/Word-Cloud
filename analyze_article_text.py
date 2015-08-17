from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import random
from random import Random
cur_dir = path.dirname(__file__)

article_text = open(path.join(cur_dir, 'article_text.txt')).read()
ampelman_mask = imread(path.join(cur_dir, 'ampelman_mask.png'))

word_cloud = WordCloud(mask=ampelman_mask, background_color='white', stopwords=STOPWORDS.add("m"))

word_cloud.generate(article_text)

plt.imshow(word_cloud)
plt.axis("off")
plt.show()