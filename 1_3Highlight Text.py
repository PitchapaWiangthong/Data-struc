print("*** Reading E-Book ***")
text = input("Text , Highlight : ")
highlight = text[-1]
newtext = ""
text = text[:-2]
for i in range(len(text)):
        if text[i] == highlight:print("["+text[i]+"]",end='')
        else:print(text[i],end='')

