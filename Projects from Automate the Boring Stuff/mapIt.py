import sys
import webbrowser
import pyperclip


def search_gmap():
    '''
    Problem Statement - 1. Gets a street address from the command line arguments or clipboard
                        2. Opens the web browser to the Google Maps page for the address
    '''
    if len(sys.argv) > 1:
        street_adr = sys.argv[1].replace(' ', '+')
    else:
        street_adr = pyperclip.paste().replace(' ', '+')

    webbrowser.open('https://www.google.com/maps/search/{}'.format(street_adr))


search_gmap()
