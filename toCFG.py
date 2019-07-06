from automata.pda.npda import NPDA


# f=NPDA()

def isUpper(string):
    if string.upper()==string:
        return True
    return False
def isLower(string):
    if string.lower()==string:
        return True
    return False
def toCFG(input_npda):
    # input_transitions=list(input_npda.transitions.values())[0]
    state={}
    for i in input_npda.transitions:
        # print(i)
        for element in input_npda.transitions[i]:
            element1=[i]+element
            # print(element1)
            if len(element1[3])==1:
                if str('('+element1[0]+element1[2]+element1[4] + ')') not in state.keys():
                    state[str('('+element1[0]+element1[2]+element1[4] + ')')]=[element1[1]]
                else:
                    state[str('('+element1[0]+element1[2]+element1[4] + ')')].append(element1[1])
            else:
                
                if len(element1[3])==2:
                    re=[]
                    for t in input_npda.states:
                        s = element1[1] + '(' + element1[4] + element1[3][0] + t + ')' + '(' + element1[4] + element1[3][1]
                        for j in input_npda.states:
                            s += j + ')'
                        re.append(s)
                    if str('('+element1[0]+element1[2]+element1[4] + ')') not in state.keys():
                        state[str('(' + element1[0] + element1[2] + element1[4] + ')')]=re
                    else:
                        state[str('(' + element1[0] + element1[2] + element1[4] + ')')] += re

    return state
def normalizeGrammar(dictionary):
    re=[]
    for i in dictionary.keys():
        for j in dictionary[i]:
            re.append([i,j])
    return re
# print(normalizeGrammar(toCFG(npda)))
def printGrammar(npda):
    dictionary=toCFG(npda)
    for element in dictionary.keys():
        s=element+'->'
        for i in dictionary[element][:-1]:
            s+=i
            s+='|'
        s+=dictionary[element][-1]
        print(s)
# printGrammar(npda)