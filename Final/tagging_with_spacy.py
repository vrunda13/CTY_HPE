'''from __future__ import unicode_literals, print_function

import plac #  wrapper over argparse
import random
from pathlib import Path
from tqdm import tqdm # loading bar
import spacy

def tagging(data):
      with open('{}'.format(data.replace('pdf','txt')),'r') as file:
          content=file.read()
      #replacing \n, /, : and , with space 
      content=content.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
      #creating a list to store all the read words
      #l=content.split()
      output_dir=Path("C:/Users/Admin/Downloads/FINAL")
      # test the saved model
      print("Loading from", output_dir)
      nlp2 = spacy.load(output_dir)
      doc = nlp2(content)
      print('Entities', [(ent.text, ent.label_) for ent in doc.ents])'''

import spacy
import csv

#################### version parser ########################################
def version_parser(txtfile,referenceKB,newKb):
    import re
    import csv

    words=[]
    tech_words=[]
    versions=[]
    
    with open(txtfile,'r') as f: #Give the text extracted file here for tagging
        content1=f.read()
        #print(content1)
        content=content1.split(' ')
        for i in range(len(content)):
            if '\n' in content[i]:
                l=content[i].split('\n')
                for w in l:
                    if not w.isdigit():
                        content.insert(i,w)
                        
    file=referenceKB.encode("utf-8")

    with open(file, 'r') as csvfile:
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=",",skipinitialspace=True)
        for row in reader:
            words.extend(row)
            
    content_words=[]
    content_words1=content1.split(' ')
    for i in content_words1:
        content_words.extend(i.split('\n'))
        
    with open(newKb,'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in range(len(content_words)):
            #print(content[i])
            if content_words[i] in words:
                tech_words.append(content_words[i])
                #print(tech_words)
                for n in content_words[i+1].split('.'):
                    if re.match('v\d((\.\d)*|(\.[a-zA-Z]))',content_words[i+1].lower()):
                        versions.append(content_words[i+1])
                        writer.writerow((content_words[i],content_words[i+1]))
                        print('c1',content_words[i], content_words[i+1])
                        break
                    elif (content_words[i+1].lower()=='ver' or content_words[i+1].lower()=='version') and any(content_words[i+2].split('.')) in ['0','1','2','3','4','5','6','7','8','9']:
                        versions.append(content_words[i+2])
                        writer.writerow((content_words[i],content_words[i+2]))
                        print('c2',content_words[i], content_words[i+2])
                        break
                    elif n in ['0','1','2','3','4','5','6','7','8','9'] and content_words[i+1][-1]!='.' and not '/' in content_words[i+1]:
                        versions.append(content_words[i+1])
                        writer.writerow((content_words[i],content_words[i+1]))
                        print('c3',content_words[i],content_words[i+1])
                        break
                    else:
                        versions.append('NA')
                        writer.writerow((content_words[i],"NA"))
                        break
    return tech_words, versions

def tagging(data):
    prdnlp = spacy.load("C:/Users/Admin/Downloads/FINAL")
    txtfile='{}'.format(data.replace('pdf','txt'))
    with open(txtfile,'r') as f: #Give the text extracted file here for tagging
        content1=f.read()
        content1=content1.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
        content=content1.split()
        for i in range(len(content)):
            if '\n' in content[i]:
                l=content[i].split('\n')
                for w in l:
                    if not w.isdigit():
                        content.insert(i,w)

    doc = prdnlp(content1)

    items = [x.text for x in doc.ents]

    # Update KB with new words

    new_words=set(items)#[w for w in items if not w in words] # words tagged by spacy which are not there in the KB
    referenceKB='{}'.format(data.replace('pdf','csv'))
    with open(referenceKB,'w', newline='') as file:
        writer=csv.writer(file)
        for w in new_words:
            writer.writerow([w])
            
    newKB=data[:-4]
    newKB=newKB+"1.csv"

    version_parser(txtfile,referenceKB,newKB)



