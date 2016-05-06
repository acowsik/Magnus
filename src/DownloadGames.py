#open(f.split('_')[1]+'.pgn','wb').write(bz2.decompress(open(f,'rb').read()))

import bz2
import requests
import datetime


for year in xrange(1999, datetime.datetime.now().year):
    r = requests.post("http://www.ficsgames.org/cgi-bin/download.cgi", data = {
        'gametype': '4',
        'player': '',
        'year': str(year),
        'month': 0,
        'movetimes': 0,
        'download': 'Download'
    })

    print r.text

    urlstart = r.text.index('/dl/')
    urlend = r.text.index('.pgn.bz2">') + len('.pgn.bz2')

    url = r.text[urlstart:urlend]

    r = requests.get(url)
    decompressed = bz2.decompress(r.text)
    open("../Games/%d.pgn"%year, 'wb').write(decompressed)