import requests

def gettext(url):
    p = 'https://stepic.org/media/attachments/course67/3.6.3/'
    furl = p + url
    r = requests.get(furl)
    if r.text[0:2] == 'We':
        print(r.text)
    else:
        gettext(r.text)

gettext('699991.txt')