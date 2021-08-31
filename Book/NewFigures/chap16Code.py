from outrankingDigraphs import *
gt07 = PerformanceTableau('graffiti07')
##scores = {}
##for movie in gt07.actions:
##    scores[movie] = Decimal('0')
##    weight = Decimal('0')
##    for critic in gt07.criteria:
##        if gt07.evaluation[critic][movie] != gt07.NA:
##            scores[movie] += gt07.evaluation[critic][movie]
##            weight += gt07.criteria[critic]['weight']
##    scores[movie] /= weight
##scoresList = [(scores[movie],movie) for movie in scores]
##scoresList.sort(reverse=True)
##for item,score in enumerate(scoresList):
##    print('%s: %.2f' % (score[1],score[0]) )
          
globalScores = {}
for mv in gt07.actions:
    globalScores[mv] = Decimal('0')
    sumWeights = Decimal('0')
    for critic in gt07.criteria:
        stars = gt07.evaluation[critic][mv]
        if stars != gt07.NA:
            weight = gt07.criteria[critic]['weight']
            globalScores[mv] += (stars * weight)
            sumWeights += weight
    globalScores[mv] /= sumWeights
rankedList = [(globalScores[mv],mv) for mv in globalScores]
rankedList.sort(reverse=True)
for item in rankedList:
    print('%s: %.2f' % (item[1],item[0]) )
