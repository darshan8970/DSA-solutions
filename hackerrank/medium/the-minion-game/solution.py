def minion_game(string):
    vowels = "AEIOU"
    score = {"Stuart":0, "Kevin":0}
    
    for i in range(len(string)):
        player = "Kevin" if string[i].upper() in vowels else "Stuart"
        score[player] += (len(string) - i)
    
    if score["Kevin"] == score["Stuart"]:
        print("Draw")
    else:
        winner = max(score, key=score.get)
        print(f"{winner} {score[winner]}") 

