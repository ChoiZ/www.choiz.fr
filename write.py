from datetime import datetime
from uuid import uuid4
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import unicodedata
import subprocess

def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

post = {}
post['title'] = raw_input('Article Title: ')
post['slug'] = datetime.now().strftime('%Y-%m-%d-')+remove_accents(post['title'].lower().replace(' ', '-').replace("'", '-'))
post['date'] = datetime.now().strftime('%Y-%m-%d')
post['time'] = datetime.now().strftime('%H:%M:%S')
post['tags'] = raw_input('Tags (like: gentoo, linux...): ')

header = """Title: %(title)s
Date: %(date)s %(time)s
Author: choiz
Category: text
Tags: %(tags)s
Slug: %(slug)s
Status: published


""" % (post)

out_file = 'content/%s.md' % (post['slug'])

try:
    with open(out_file) as f:
        out_file = 'content/%s.md' % (uuid4())
        print('The specified output file exists. Writing to %s' % out_file)
except:
    pass

with open(out_file, 'w') as f:
    f.write(header)

# open vim at line 20
subprocess.call(['vi', '%s' % out_file, '+20'])
