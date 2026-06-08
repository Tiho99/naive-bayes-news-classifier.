


# def for clean
pnt = ".,!?;:'\"()-[]{}_"
append = []
def clean(text):
    txxt = text.lower()
    for j in pnt:
        txxt = txxt.replace(j, "")
    return txxt

# def for tokenize
def tokenize(text):
    t = clean(text)
    token = t.split()
    return token


# def vocab
def vocab(text):
    v = []
    for it in text:
        w = tokenize(it)
        for j in w:
            if j not in v:
                v.append(j)
    return v

# def vectorizing 
def veectorize(text):
    t =vocab(text)
    vector = [] #vecteur
    for j in text:
        t1 = tokenize(j)
        voc = []
        for j in t:
            if j in t1:
                voc.append(1)
            else:
                voc.append(0)
        vector.append(voc)
    
    return t,vector

#NV
def nv(v , lab):
    pos = lab.count("positive")
    neg = lab.count("negative")

    p_pso = pos / len(lab)
    p_neg = neg / len(lab)
    ele_counnt = len(v[0])

    pos_ele = [1] * ele_counnt
    neg_ele = [1] * ele_counnt

    pt = 2
    nt = 2
    for i in range(len(v)):
        if lab[i] == "positive":
            for j in range(ele_counnt):
                pos_ele[j] += v[i][j]
            pt += 1
        else:
            for j in range(ele_counnt):
                neg_ele[j] += v[i][j]
            nt += 1
    return p_pso, p_neg, pos_ele, neg_ele, pt, nt

#predicat

def predicat(txt,vocab,md):
    p_pso, p_neg, pos_ele, neg_ele, pt, nt = md
    t = tokenize(txt)
    p_pos = p_pso
    p_neg = p_neg
    for i in range(len(vocab)):
        if vocab[i] in t:
            p_pos *= pos_ele[i] / pt
            p_neg *= neg_ele[i] / nt
    if p_pos > p_neg:
        return "positive"   
    else:
        return "negative"

D1 = "Wow, I feel good"
D2 = "I knew that I would, now !"
D3 = "what's up ?"
D4 = "I feel really good"
D5 = " I feel nice."
txt = [D1, D2, D3, D4, D5]
leb = ["pos","pos","pos","neg","neg"]

for i in txt:
    print("ORIGINAL : ", i)
    print("CLEAN : ", clean(i))
    print("TOKENIZE : ", tokenize(i))
    print()

v, vectors = veectorize(txt)
print("VOCABULARY : ", v)
print("VECTORS : ",vectors)
print("\n")
for i in range(len(vectors)):
    print(f"D{i+1} : {vectors[i]}")

modl = nv(vectors, leb)
tst = "I feel really good"
print(f"Prediction for '{tst}': {predicat(tst, v, modl)}")