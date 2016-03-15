n = int(raw_input())

while n != 0:
    vagoes = map(int, raw_input().split())
    if(vagoes[0] == 0):
        print ""
        n = int(raw_input())
        continue
    estacao = []
    vagaoMaior = n
    possivel = True
    for i in range(n):
        elemento = vagoes.pop() 
        if not estacao:
            estacao.append(elemento)
            if(elemento == vagaoMaior):
                vagaoMaior -= 1
                estacao.pop()
        else:
            if(elemento < estacao[-1]):
                if(elemento == vagaoMaior):
                    vagaoMaior -= 1
                    estacao.pop()
                    while estacao[-1] == vagaoMaior:
                        elemento = estacao.pop()
                        vagaoMaior-=1
                        if len(estacao) == 0: break
                else:
                    possivel = False
            else:
                estacao.append(elemento)
                if(elemento == vagaoMaior):
                    vagaoMaior -= 1
                    estacao.pop()
                    while estacao[-1] == vagaoMaior:
                        elemento = estacao.pop()
                        vagaoMaior-=1
                        if len(estacao) == 0: break
    if len(estacao) > 0: possivel = False
    if possivel:
        print "Yes"
    else: print "No"