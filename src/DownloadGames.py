#open(f.split('_')[1]+'.pgn','wb').write(bz2.decompress(open(f,'rb').read()))

import bz2
import requests
import datetime
import os
import errno
import urllib2


for year in xrange(1999, datetime.datetime.now().year):
    r = requests.post("http://www.ficsgames.org/cgi-bin/download.cgi", data = {
        'gametype': '4',
        'player': '',
        'year': str(year),
        'month': 0,
        'movetimes': 0,
        'download': 'Download'
    })

    if 'query quota exceeded' in r.text:
        print "Wait a little, I don't know how long"
        break

    urlstart = r.text.index('/dl/')
    urlend = r.text.index('.pgn.bz2">') + len('.pgn.bz2')

    url = "http://www.ficsgames.org" + r.text[urlstart:urlend]

    data = urllib2.urlopen(url).read()
    try:
        if not os.path.exists(("../Games")):
            os.makedirs("../Games")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    open('../Games/%d.pgn.bz2'%year, 'wb').write(data)
    decompressed = bz2.decompress(data)
    open("../Games/%d.pgn"%year, 'wb').write(decompressed)