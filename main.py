import requests,json,threading,time

baseurl = 'https://clarksonmsda.org/api/get_product.php?pid='
#i = 0

def worker(i):
    global baseurl
    zc = str(i)
    url = baseurl + zc
    r = requests.get(url)#blocking function call
    data = json.loads(r.text)
    if data['data'] is None:
        pass
    else:
        if data['data']['prod_id'] is None:
            pass
        else:
            w = json.dumps(data['data'])
            fn = 'pid_'+str(i)
            f = open(fn,'w')
            f.write(w)
            f.close()


i = 0
while i <= 200:
    w = threading.Thread(name='tid_'+str(i),target=worker, args=(i,))
    w.start()
    i+=1
