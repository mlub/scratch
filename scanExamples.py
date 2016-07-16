import requests
import subprocess
from lxml import html

old_url = 'http://matplotlib.org/1.5.1/examples/'
new_url = 'http://matplotlib.org/2.0.0b2/examples/'

# Skip any urls containing these strings
skip_these = ['animation/', 'api/']

if __name__ == '__main__':
    """
    Scan the matplotlib examples page and open the 1.5.1 version and
    2.0.0b2 version
    """
    old_page = requests.get(old_url+'index.html').text
    old_tree = html.fromstring(old_page)
    examples = old_tree.xpath('//a[@class="reference internal"]')

    for ex in examples:
        if 'index.html' in ex.attrib['href']:
            continue
        tmp=[skip for skip in skip_these if skip in ex.attrib['href']]
        if len(tmp)>0:
            continue

        subprocess.call(['google-chrome',
                         old_url+ex.attrib['href'],
                         new_url+ex.attrib['href']])

        input("%s - Press Enter to continue..." % (ex.attrib['href'],))