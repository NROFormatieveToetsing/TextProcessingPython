from os import path
from scipy.misc import imread
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib.pyplot as plt


def alice1 ():
    d = path.dirname(__file__)

#Read the whole text.
    text = open(path.join(d, 'input.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    alice_mask = imread(path.join(d, "alice_mask.png"))

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=STOPWORDS.add("said"))
# generate word cloud
    wc.generate(text)

# store to file
    wc.to_file(path.join(d, "alice.png"))

# show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

def hope ():
    d = path.dirname(__file__)

    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
    mask = imread(path.join(d, "stormtrooper_mask.png"))
    text = open(path.join(d, 'input.txt')).read()

   # preprocessing the text a little bit
   #text = text.replace("HAN", "Han")
   #text = text.replace("LUKE'S", "Luke")

   # adding movie script specific stopwords
    stopwords = STOPWORDS.copy()
    stopwords.add("int")
    stopwords.add("ext")

    wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
   # store default colored image
    default_colors = wc.to_array()
    plt.title("Custom colors")
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
    wc.to_file("a_new_hope.png")
    plt.axis("off")
    plt.figure()
    plt.title("Default colors")
    plt.imshow(default_colors)
    plt.axis("off")
    plt.show()

def alice2 ():
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'input.txt')).read()

    # read the mask / color image
    # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    alice_coloring = imread(path.join(d, "alice_color.png"))

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=STOPWORDS,
               max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

def normal ():
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, 'input.txt')).read()
    wordcloud = WordCloud().generate(text)
    # Open a plot of the generated image.
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def bird ():
    d = path.dirname(__file__)
    # Read the whole text.
    text = open(path.join(d, 'input.txt')).read()
    twitter_mask = imread(path.join(d,"twitter_mask.png"))
    wc = WordCloud(background_color="white", max_words=2000, mask=twitter_mask,
               stopwords=STOPWORDS,max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)                          
    plt.imshow(wc)
    plt.axis("off")
    #plt.savefig('./my_twitter_wordcloud_2.png', dpi=300)
    plt.show()

def gun ():
    d = path.dirname(__file__)
    # Read the whole text.
    text = open(path.join(d, 'input.txt')).read()
    gun_mask = imread(path.join(d,"gun.png"))
    wc = WordCloud(background_color="white", max_words=2000, mask=gun_mask,
               stopwords=STOPWORDS,max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)                          
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig('./my_twitter_wordcloud_2.png', dpi=300)
    plt.show()

def heart ():
    d = path.dirname(__file__)
    # Read the whole text.
    text = open(path.join(d, 'input.txt')).read()
    twitter_mask = imread(path.join(d,"heart.png"))
    wc = WordCloud(background_color="white", max_words=2000, mask=twitter_mask,
               stopwords=STOPWORDS,max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)                          
    plt.imshow(wc)
    plt.axis("off")
    #plt.savefig('./my_twitter_wordcloud_2.png', dpi=300)
    plt.show()

   

