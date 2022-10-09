from conf import *
import tkinter as tk

wnd=tk.Tk()
wnd.title('ugadaga')
vc = getvoc(vocFileName)
novc = []
def checkword():
  global beginscore
  global novc
  if btn['text'] == 'Начать':
    global gw
    gw = guess(vc,level,int(lblWordLen['text']))
    btn['text'] = 'Ok'
    com['text'] = 'загадано'
    ent['state'] = 'normal'
    beginscore = time() - 20
    return()
  wordent = ent.get()
  ent.delete(0,tk.END)
  if wordent:
    beginscore -= 20
    lbl_score['text'] = str(int(time()-beginscore))
    if not wordent in vc:
      com['fg'] = errColor
      com['text'] = 'не знаю такого слова'
      novc.append(wordent)
      return()
    vc[wordent] += 1
    if len(wordent) != len(gw):
      com['fg'] = normalColor
      com['text'] = f'пиши слово из {len(gw)} букв'
      return()
    box['state'] = 'normal'
    bull = cow = 0
    for i in range(int(lblWordLen['text'])):
      bull += wordent[i] == gw[i]
      
    wrd = list(wordent)
    for c in gw:
      if c in wrd:
        cow += 1
        wrd.remove(c)
    box.insert(0.0,f'{wordent} {bull},{cow}\n')
    box['state'] = 'disabled'
    ent.delete(0,tk.END)
  com['text'] = wordent
  if wordent == gw:
    com['text'] = 'Угадал'
    btn['text'] = 'Начать'
    ent['state'] = 'disabled'
    WordLenPlus()
    guessed(vc, novc, vocFileName)
    novc = []
  print(wordent)

def rt(event):
  checkword()

def exit_win(event):
  guessed(vc, novc, vocFileName)
  wnd.destroy()

def WordLenPlus():
  if lblWordLen['text'] != '10':
    lblWordLen['text'] = str(int(lblWordLen['text']) + 1)

def WordLenMinus():
  if lblWordLen['text'] != '3':
    lblWordLen['text'] = str(int(lblWordLen['text']) - 1)

box = tk.Text(width=20,bg='silver')
box['state'] = 'disabled'
com = tk.Label(width=18)
com['text'] = 'ugadaga'
#com['state'] = 'disabled'
ent = tk.Entry(width=18)
ent['state'] = 'disabled'
btn = tk.Button(
  text = 'Начать',
  command = checkword
  )
lbl_score = tk.Label(width=18)

frWordLen = tk.LabelFrame(text = 'длинна загаданного\nслова')
btnPlus = tk.Button(frWordLen, text = '+', command = WordLenPlus)
lblWordLen = tk.Button(frWordLen, text = '4')
btnMinus = tk.Button(frWordLen, text = '-',command = WordLenMinus)

box.pack()
com.pack()
ent.pack()
btn.pack()
frWordLen.pack()
lbl_score.pack()
btnPlus.grid(column = 2, row = 0)
lblWordLen.grid(column = 1, row = 0)
btnMinus.grid(column = 0, row = 0)
ent.focus()
wnd.minsize(170,0)
ent.bind('<Return>',rt)
wnd.bind('<Control-q>', exit_win)
wnd.mainloop()
