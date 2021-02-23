import streamlit as st
import os
import datetime as dt
import csv
import pickle as pk

st.write("""
# Let sentinel figures its sentiment
""")

st.write("""
***
""")

with st.echo():
    import spacy as sp
    import pickle as pk

    nlp=sp.load('en_core_web_sm')

    training = [
        "This paper shows an alternative deployment of recommender systems. To this end, the authors use two variations of CHC genetic algorithm.",
        "This manuscript provides an interesting solution with machine learning techniques to classify spectra legacy data of the Hubble Space Telescope. The experiment is sound and very interesting to the Infonor and JCC community. A confusion matrix and parameters for each classifier could clarify results.",
        "Nothing new from a machine learning perspective. The authors should provide more information about the models they have obtained with the different classifiers and statistical significance.",
        "In the context of software engineering, the authors do a good job describing the technical details of the tool.",
        "This paper is not suitable for the SCCC conference. The author should consider reporting this experience on a conference related to computer engineering. The material presented in the paper could be of interest for Oracle.",
        "A definition of ERP is required - can't assume the reader knows what this means.",
        "A segmentation procedure for breast tissue images using SVM. Parameter selection in an SVM is critical and may improve notably the performance.",
        "Woke up hours earlier than I needed too. Doggo stole my blanket. Fiona snoring. I'm smiling, because they are the best. Hope they wake up so we can all eat breakfast.",
        "Horrible. I sat on my bed breaking down for about an hour.",
        "It was great. It was the 543rd day where I did exactly the same thing.",
        "My day's just started. Well it's 9:35am anyway, so I'm at work.",
        "Asked a girl at the mall for her number, she had a boyfriend. I said sorry and to have a good day we both laughed at it, and went our seperate ways. Was quite a decent day.",
        "Good. But looking forward to some child-free time.",
        "It just started. Highlight: Coffee.",
        "It was so nice day. it was my memorable day.",
        "Actually not bad! I'm getting help for some personal issues, and things aren't so darned bleak anymore, it seems.",
        "Super, thanks for asking!",
        "not bad as i only work till 1 pm on fridays.",
        "The husband and his sister visit their mother during last Christmas in Munich.",
        "I want to know why Peter kissed Louise if he is in love with Jolly.",
        "Apple earned more than 69 million USD just by selling their recently published iPhone14 last month.",
        "As Tesla expanded its grasp to aviation tech, we assume that Elon Musk tries to conquer air, land, sea, and space."
    ]

    default_ner = []
    new_ner = []
    ner = []

    for k in range(len(training)):
        doc = nlp(training[k])
        line = []
        print(doc)
        for j in doc.ents:
            print(" ")
            word = j.text
            start = training[k].find(word)
            end = start + len(word)
            label = j.label_
            print(word,label)
            ans = input("Do you agree with the label for {}: Y/y => ".format(word))
            if ans.lower() == 'y':
                group = (start,end,label)
                line.append(group)
        default_ner.append(line)
        print("---------------------------------------")

    new_label = []
    while True:
        a = input("=> ")
        if a.lower() == "stop":
            break
        new_label.append(a)

    for g in range(len(training)):
        split = training[g].split()
        ran = [(training[g].find(kl),training[g].find(kl)+len(kl)) for kl in split]
        mark = []
        for f in range(len(default_ner)):
            if f == g:
                for k in range(len(default_ner[f])):
                    for h in range(len(ran)):
                        if default_ner[f][k][0] == ran[h][0]:
                            if default_ner[f][k][1] == ran[h][1]:
                                mark.append(h)
        split = [split[y] for y in range(len(split)) if y not in mark]
        ran = [ran[c] for c in range(len(ran)) if c not in mark]
        print(training[g])
        print(split)
        print(ran)
        print(" ")
        more = []
        while True:
            ranger = input("range of position: like this 3,10 which starts from 3 and ends at 9. => ")
            if ranger == "0,0":
                break
            ranger = ranger.split(',')
            print("what tag do you want for {} from the new label?\n".format(training[g][int(ranger[0]):int(ranger[1])]))
            print("input the index as integer below")
            for w, t in enumerate(new_label):
                print(w, "=>",t)
            ind = int(input("index here: "))
            if ind > w:
                raise ValueError("No this option")
            pack = (int(ranger[0]),int(ranger[1]),new_label[ind])
            more.append(pack)
        new_ner.append(more)
        print("-------------------------------------")

    out = []
    for z in range(len(default_ner)):
        for s in range(len(new_ner)):
            if z == s:
                if len(default_ner[z]) == 0:
                    if len(default_ner[z]) == len(new_ner[s]):
                        out.append(z)

    default_ner = [default_ner[v] for v in range(len(default_ner)) if v not in out]
    new_ner = [new_ner[g] for g in range(len(new_ner)) if g not in out]
    training = [training[d] for d in range(len(training)) if d not in out]

    c = 0
    while len(ner) != len(default_ner):
        squad = []
        for n in range(len(default_ner[c])):
            squad.append(default_ner[c][n])
        for m in range(len(new_ner[c])):
            squad.append(new_ner[c][m])
        c += 1
        ner.append(squad)

    stack = []
    u = 0
    while len(stack) != len(new_ner):
        txt = training[u]
        dic = {"entities":ner[u]}
        tup = (txt,dic)
        u += 1
        stack.append(tup)

    open_file = open('./pickle.pickle', "wb")
    pk.dump(stack, open_file)
    open_file.close()

    open_file = open('./pickle.pickle', "rb")
    loaded_list = pk.load(open_file)
    open_file.close()

    print(loaded_list)

st.graphviz_chart('''
    digraph {
        Sequential -> Embedding
        Embedding -> LSTM1
        LSTM1 -> LSTM2
        LSTM2 -> Dropout
        Dropout -> TimeDistributed
        TimeDistributed -> Dense
        Dense -> Softmax
        Softmax -> ModelSummary
        sentence -> words
        words -> coreConcepts
        coreConcepts -> pos
        pos -> ner
        coreConcepts -> extra
        ner -> coreConcepts
        Org -> ner
        Fin -> ner
        Dated -> ner
        Loc -> ner
        Date -> ner
        BBegin -> tags
        EEnd -> tags
        SSingle -> tags
        OOther -> tags
        tags -> Org
        OOther -> extra
        tags -> Fin 
        tags -> Dated
        tags -> Loc
        tags -> Date
        IIntermediate -> tags
        ner -> trainingData
        trainingData -> training
        ModelSummary -> training
        training -> ModelSummary
        training -> resultModel
        ModelSummary -> resultModel
    }
''')

op = open('./pickle.pickle',"rb")
lo = pk.load(op)
op.close()

with st.beta_expander("Check your data"):
    lo
