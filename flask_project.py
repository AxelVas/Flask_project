from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


x = np.random.randint(15,500, 600)
y = np.random.randint(500,1255, 600)
fig, ax = plt.subplots()
ax.scatter(x, y)

app = Flask(__name__)

course_list='Ya course'
hi= 'best_frend'

@app.route('/')

def index():

    
    return render_template('page.html', course_list=course_list, hi=hi, Img=fig) #'<html><body><h1>Hello World</h1></body></html>'

if __name__ == '__main__':
    app.run(debug = True)

'''
    x = np.random.randint(15,500, 600)
    y = np.random.randint(500,1255, 600)
    plt.figure(figsize=(10,8))
    plt.plot(sorted(x),sorted(y))
    plt.title('Random Randint')
    plt.ylabel('some numbers')
    plt.savefig('figure.jpg')
    Img = Image.open("figure.jpg")
    '''