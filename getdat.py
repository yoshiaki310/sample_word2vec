#!/usr/bin/python
# coding:utf-8
import urllib2
import re
import sys

# テキストからタグやURLなどゴミを取り除く正規表現です。
del_tag = re.compile('<.*?>')
del_ref = re.compile('&gt;&gt;\d+')
del_url = re.compile('h*t+ps*?://[\w/:%#\$&\?\(\)~\.=\+\-]+')
del_dayofweek = re.compile('\(.*\)')
del_millisecond = re.compile('\..*')
re_resnum = re.compile('\([0-9]+\)')


# 指定文字列をタイトルに含むスレッドのスレッド名、ファイル名の一覧を取得しリストで返します
def get_2ch_thread_info(board_url, search_name):
    file_name = []
    thread_title = []
    try:
        for line in urllib2.urlopen(board_url + 'subject.txt'):
            title = re_resnum.sub('', line.split('<>')[1].decode(
                'cp932', 'replace')).replace('\n', '')
            if search_name in title:
                file_name.append(line.split('<>')[0].replace('.dat', '/'))
                thread_title.append(title)
    except Exception as e:
        print("exception on get_2ch_thread_info")
        print str(e)
    return thread_title, file_name

# 各スレッドの本文を取り出して出力します


def print_res(thread, title, search_name):
    try:
        for line in urllib2.urlopen(thread):
            try:
                articles = line.split("<>")
                name = articles[0]
                email = articles[1]
                date = articles[2]
                res = articles[3]

                print del_url.sub('', del_ref.sub('', del_tag.sub('', res)))
            except Exception as e:
                print("exception on print_res try-catch")
                print str(e)
    except Exception as e:
        print("exception on print_res")
        print str(e)


def get_2ch_data(url, board, search_name):
    titles, file_names = get_2ch_thread_info(url + board, search_name)
    for cnt in range(len(titles)):
        file_name = file_names[cnt]
        thread_title = titles[cnt]
        print_res(url + board + "dat/" +
                  file_name[:-1] + ".dat", thread_title, search_name)


if __name__ == "__main__":
    argvs = sys.argv
    url = argvs[1]
    board = argvs[2]
    keyword = argvs[3].decode('cp932', 'replace')
    get_2ch_data(url, board, keyword)
