from urllib2 import urlopen


def form_url(hour,minute):
    return "https://sslimgs.xkcd.com/comics/now/"+hour+"h"+minute+"m.png"


def fetch_img(hour,minute):
    return ''.join(i for i in urlopen(form_url(hour,minute)))


img = []
for hour in range(24):
    hour = str(hour)
    if len(hour) == 1:
        hour = '0' + hour
    for minute in ['00','15','30','45']:
        img = fetch_img(hour,minute)
        with open('imgs/'+hour+'h'+minute+'m.png','w') as f:
            f.write(img)










