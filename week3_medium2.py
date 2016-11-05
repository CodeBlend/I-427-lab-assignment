#The Minion Game
#https://www.hackerrank.com/challenges/the-minion-game

vowel = 'AEIOU'
stuart_score = 0
kevin_score = 0

s = raw_input()
for i in range(len(s)):
    if s[i] in vowel:
        kevin_score += (len(s)-i)
    else:
        stuart_score += (len(s)-i)

if stuart_score > kevin_score:
    print "Stuart", stuart_score
elif kevin_score > stuart_score:
    print "Kevin", kevin_score
else:
    print "Draw"
