import emoji

def me_in_text(text):
    words_len = 0
    full_len = 0
   # print(text)
    for elem in text:
       # print(elem)
        words_len += int(elem['text'].count("Я")) + int(elem['text'].count(" я")) + int(elem['text'].count(".я")) + int(elem['text'].count(",я")) + int(elem['text'].count("?я"))+ int(elem['text'].count("!я"))+ int(elem['text'].count("(я"))+ int(elem['text'].count("-я"))+ int(elem['text'].count("+я"))+ elem['text'].count(":я") + int(elem['text'].count(";я"))
        full_len += len(elem['text'].split())
                              
    return (words_len / full_len) * 1000.0
            
def questions(text):
    # Should correct on the test case:
    # ??
    # 2, must be  - 1
    q_len = 0
    full_len = 0                      
    for elem in text:
        q_len += int(elem['text'].count("?"))
        full_len +=len(elem['text'].split())
        
    return (q_len / full_len) * 100.0

def smiles(text):

    emoji_len = 0
    full_len = 0
    for elem in text:
        emoji_len += int(emoji.emoji_count(elem['text']))
        full_len  += float(len(elem['text'].split()))
        
    return (emoji_len / full_len) * 100.0

def nonNormalLexic(text):
    dic = []
    
    return 0
    

def without_me(text):
    dic = ["ты","я", "мне", "ишь","ал", "ял","ала", "яла", "ула", "ул","ели","ела", "ол", "ел"]
    
    return 0

def direct_words(text):
    dic = ["ать","ять","оть","еть", "уть", "ем", "им", "ешь", "ишь","ал", "ял","ала", "яла", "ула", "ул","ели","ела", "ол", "ел"]
    direct_word_len = 0
    full_len        = 0
    for struct in text:
        lst = struct['text'].split()
        for word in lst:
            for word_in_dict in dic:
                if word.find(word_in_dict) > 0 or word[len(word) - 1] == "у" or word[len(word)-1] == "ю":
                    direct_word_len += len(word)
                full_len += len(word)
        
        
    return (direct_word_len / full_len)*100.0
    
def animals_words(text):
    counter = 0
    animals_len = 0
    full_len = 0
    dic = ["крыса","тварь","животное","баран","олень","змея","сука"]                          
    for elem in text:
        lst = elem['text'].replace('.', '').split()        
        for i in lst:
            if aproximation(dic, i):
                animals_len += len(i)
        full_len += len(elem['text'])
            
    return (animals_len / full_len)*100.0


# Функция приближенно определяет, то ли это слово:
#   рыба
#   рыбq
#   совпадение есть, тогда вернет, что слово подходит

def aproximation(string, word):
    counter = 0
    for w in string:
        for i in range(len(word)):
            if (len(w) > i) and (word[i] == w[i]):
                counter +=1
        if counter / float(len(word)) > 0.75:
            return 1
    return 0


#
#   Кнута-Морриса-Пратта
#
#


def prefix(s):
    v = [0]*len(s)
    for i in xrange(1,len(s)):
        k = v[i-1]
        while (k > 0) and (s[k] != s[i]):
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

def KnuthMorrisPratt(s,t):
    index = -1
    f = prefix(s)
    k = 0
    for i in xrange(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k-1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index


