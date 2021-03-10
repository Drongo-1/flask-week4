import random
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
def quitess():
    dict[posts] = {1:{'author': 'Ngugidavid', 'title': 'random', 'quote':'This is a random quote'},
                   2:{'author': 'Ngugidavid2', 'title': 'random', 'quote':'This is a random quote'}} 
    res = key, val = random.choice(list(test_dict.items())) 
    # print("The random pair is : " + str(res)) 
    newauthor=str(val['author']) 
    return render_template('quotes.html', newauthor=newauthor, val=val)