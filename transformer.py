#Warning : tab only
#Warning : no deftree nesting

lines = []

with open('tree_code.tpy','r') as f:
    lines = f.read().split('\n')
    #print(lines)

clines = []

def f(x):return x
print(f(5))

for l in lines:
    depth = 0
    while depth<len(l) and l[depth] == '\t':
        depth += 1
    clines.append((depth, l[depth:]))

for c in clines:
    print(c)

def norm(s):
    if s[0] == ' ':
        return s[1:]

def normwithoutcom(s):
    if '#' in s:
        return norm(s[:s.index('#')])
    else:
        return norm(s)

newcode = []

i = 0
while i<len(clines):
    d,l = clines[i]
    if l[:7] == 'deftree':
        mergepos = i+1
        while clines[mergepos][0] != d:
            mergepos+=1

        endpos = mergepos+1
        while endpos < len(clines) and clines[endpos] >= d:
            endpos+=1

        fname = l[l.index(' ')+1:l.index('(')]
        xname = l[l.index('(')+1:l.index(')')]
        l0 = l[l.index(':')+1:]

        lmerge = clines[mergepos][1]
        ylistname = lmerge[6:lmerge.index(':')]
        mergel0 = lmerge[lmerge.index(':')+1:]

        newcode.append((d,'def '+fname+'('+xname+'):'))
        newcode.append((d+1, ylistname+' = []'))
        newcode.append((d+1, l0))

        for j in range(i+1, mergepos):
            cd, cl = clines[j]
            '''if len(cl) > 0 and cl[0] == '<':
                newcode.append((cd,'return '+norm(cl[1:])))'''
            if len(cl) > 0 and cl[0] == '>':
                newcode.append((cd,ylistname+'.append('+fname+'('+normwithoutcom(cl[1:])+'))'))
            else:
                newcode.append((cd,cl))

        for j in range(mergepos+1, endpos):
            cd, cl = clines[j]
            '''if len(cl) > 0 and cl[0] == '<':
                newcode.append((cd,'return '+norm(cl[1:])))'''
            if len(cl) > 0 and cl[0] == '>':
                newcode.append((cd,'#ILLEGAL LINE '+cl))
            else:
                newcode.append((cd,cl))
        i = endpos
    else:
        newcode.append((d,l))
    i+=1

print(newcode)

with open('code.py','w') as f:
    for (d,l) in newcode:
        s = ''
        for i in range(d):
            s+='\t'
        s+=l
        print(s)
        f.write(s+'\n')
