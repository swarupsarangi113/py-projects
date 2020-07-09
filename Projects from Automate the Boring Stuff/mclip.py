import pyperclip,sys

TEXT = {'agree' : '''Yes I agree. That sounds fine to me.''',
        'busy' : '''Sorry, I can we do this later this week or next week ?''',
        'upshell' : '''Would you consider making this a monthly donation'''}

keyphrase = ''

if len(sys.argv) != 2 :
    print('Usage : mclip.py [keyphrase] - copy phrase text')
    sys.exit()
else :
    keyphrase = sys.argv[1]

if keyphrase in TEXT :
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for keyphrase \'{keyphrase}\' is copied to the clipboard')
else :
    print(f'Text for keyphrase \'{keyphrase}\' not found.')

    
    
