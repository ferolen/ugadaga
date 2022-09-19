from random import choice

lw = 5 # word length
level = -1 # level. The more the rarer world can be guessing
errColor = 'red' # Error message color
normalColor = 'red' # normal message color
vocFileName = 'voc.txt'

def getvoc(filename):
  voc = {}
  with open(filename,encoding='utf-8') as f:
    for a in f:
      w = a.split()
      voc[w[0]] = int(w[1])
  return(voc)

def guess(voc, ds, lw):
  a = []
  for i in voc:
    if voc[i] > ds and len(i) == lw:
      a.append(i)
  return(choice(a))

def guessed(vc, filename):
  with open(filename,'w',encoding='utf-8') as fv:
    for i in vc:
      fv.write(f'{i}\t{vc[i]}\n')
