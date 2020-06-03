def ans_query(q, data):
    import csv
    import nltk
    import re
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    tech_words, versions=[],[]
    #file="KnowledgeBases/"+pdfname+'.csv' 
    file=data[:-4]
    file=file+"1.csv"
    q=q.lower()
    with open(file) as f:
        reader = csv.reader((line.replace('\0','') for line in f), delimiter=",",skipinitialspace=True)
        for row in  reader:
            tech_words.append(row[0].lower())
            versions.append(row[1])
        print(tech_words)
        print (versions)
    if q.lower()=="are there any technologies used" or q.lower()=='Is any technology used in the document' :
        if tech_words:
            return 'Yes'
        else:
            return 'No technology is used'
    elif q.lower()=="what are the technologies used?" or q.lower()=='technologies used?':
        s=set(tech_words)
        ans=""
        for i in s:
            ans+=i+" "
        return "The technologies used are:"+ans
    elif 'version' in q.split(' '):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(q)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(filtered_sentence)
        for w in filtered_sentence:
            if w!='version' and w in tech_words:
                return versions[tech_words.index(w)]
    elif re.match( r'is .* (used|implemented).*', q):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(q)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(filtered_sentence)
        for w in filtered_sentence:
            if w in tech_words:
                return "Yes, "+ str(w)+" is used."
            else:
                return "No, "+ str(w)+" is not used."


            
