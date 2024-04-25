import threading
import urllib.request
import ssl
import time

start = time.time()
urls = ["https://www.google.com/", "https://www.apple.com/", "https://www.instagram.com/"]

def chama_url(url):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req, context=context)
    the_page = response.read()
    print("'%s\' carregando em %ss" % (url, (time.time() - start)))
    #print(the_page)

threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed Time: %s" % (time.time() - start))