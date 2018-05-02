iimport random

wordFile = open("popular_words.txt",'r')
wordlist = wordFile.readlines()

class XKDC:
    def __init__(self,maxWordLen, minWordLen, maxOverLen, numSub):
        self.maxwl = maxWordLen
        self.minwl = minWordLen
        self.mol = maxOverLen
        self.numSub = numSub
        self.goodwords = []
        self.wlist = []

    def goodWordFinder(self):
        for words in wordlist:
            if len(words) > self.minwl and len(words) <= self.maxwl:
                self.goodwords.append(words.strip('\n'))
    
    def createPasswords(self):
        self.goodWordFinder()
        while len(self.wlist) != 20:
            password = []
            for i in range(4):
                password.append(self.goodwords[random.randrange(len(self.goodwords))])
            wordlen = len("".join(password))
            if wordlen <= self.mol and wordlen >= 6:
                score = self.easyScore(password)
                password.append(score)
                if self.numSub:
                    password = self.numberSub(password)
                    self.wlist.append(password)
                else:
                    self.wlist.append(password)
        return self.wlist
    
    def easyScore(self,plist):
        score = 0.0
        lefthand = "asdfgzxcvbqwert"
        righthand = "lkjhpoiuymn"
        for word in plist:
            for i in range(len(word)-1):
                if word[i] in lefthand and word[i+1] in righthand:
                    score += 1
                elif word[i] in righthand and word[i+1] in lefthand:
                    score += 1
                elif word[i] == word[i+1]:
                    score += 1
            score = score / (len(word))
                
        return round(score,3)
    
    def numberSub(self,password):
        word = ""
        for i in range(len(password)-1):
            word = password[i].replace('e','3')
            word = word.replace('o','0')
            word = word.replace('l','1')
            password[i] = word
        
        return password