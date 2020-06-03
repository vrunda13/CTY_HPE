from flask import *
from chat import *
import nltk
import csv
import re
import random
from extracting_pdf import *
from queryClassifier import *
from tagging_with_spacy import *
from techBot import *
from threeQuestions import *

app = Flask(__name__)  
f=''
ff=''
@app.route('/')  
def upload():  
    return render_template("test.html")  
 
@app.route('/home', methods = ['POST'])  
def success():
    global f,ff
    if request.method == 'POST':  
        f = request.files['file']
        print(f)
        print(type(f))
        fn=str(f)
        fn=fn[15:]
        ff=fn[:-22]
        print(ff)
        f.save(f.filename)
        pdfparser(ff)
        tagging(ff)
        return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    query_type=mainQuery(userText)
    if userText.lower()=="are there any technologies used" or userText.lower()=='is any technology used in the document' or userText.lower()== "what are the technologies used?" or userText.lower()=='technologies used?' :
            print("Basic")
            return ans_query(userText,ff)
    elif re.match( r'is .* (used|implemented).*',userText.lower()):
        print("Basic")
        return ans_query(userText,ff)
    elif "version" in userText.lower():
        print("Basic")
        return ans_query(userText,ff)
    elif query_type=="generic":
        print("Gen")
        if str(genericResponse(userText)) !="None":
            return str(genericResponse(userText))
        else:
            return "Sorry. I did not understand..."
    elif query_type=="tech":
        if userText.lower()=="are there any technologies used" or userText.lower()=='is any technology used in the document' or userText.lower()== "what are the technologies used?" or userText.lower()=='technologies used?' :
            return ans_query(userText,ff)
        elif "version" in userText.lower():
            return ans_query(userText,ff)
        else:
            print("Tech")
            return str(chatty(userText))
    else:
        return "Sorry.No idea..."
  
if __name__ == '__main__':  
    app.run() 
