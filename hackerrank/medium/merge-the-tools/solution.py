def merge_the_tools(string, k):
    n = len(string)
    count = 0
    sub = ""
    for i in range(n):
        count+=1
        sub+= string[i]
        
        if count == k:
            newsub=""
            for j in sub:
                if j not in newsub:
                    newsub+= j
            print(newsub)
            newsub = ""
            count = 0
            sub = ""
