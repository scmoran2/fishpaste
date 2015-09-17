import sys
import getpass

import stem
import stem.connection
import stem.process

from stem.util import term

import pycurl
import io

SOCKS_PORT = 9050 #default tor proxy
#tor process needs to be running allready
#and set to allow socks connections to happen

def get_site(url):
    ##more sample code sampled from...
    ##https://stem.torproject.org/tutorials/to_russia_with_love.html
    output = io.BytesIO()
    query = pycurl.Curl()
    ## TODO: this is apparently how you set up a socks proxy, but we should verify
    query.setopt(query.URL, url)
    query.setopt(query.PROXY, 'localhost')
    query.setopt(query.PROXYPORT, SOCKS_PORT)
    query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
    query.setopt(query.WRITEFUNCTION, output.write)
    try:
        query.perform()
        return output.getvalue()
    except pycurl.error as exc:
        return "Couldn't reach %s (%s)"%(url,exc)


def print_bootstrap_lines(line):
    if "Bootstrapped " in line:
        print(term.format(line, term.Color.BLUE))

#thanks, example code
#https://stem.torproject.org/api/control.html


if __name__=='__main__':
    url = "http://64.31.47.121:9030/tor/rendezvous2/"
    print term.format("Connecting to: ", term.Color.BLUE),
    print term.format(url, term.Color.YELLOW)
    print(term.format(get_site(url), term.Color.RED))
