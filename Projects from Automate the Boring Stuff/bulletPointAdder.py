import pyperclip

text = pyperclip.paste()

#TODO - add bullet points to the text
lines = text.split('\n')
for i in range(len(lines)) :
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)
