#!/usr/bin/python3
# -*- coding: <UTF-16> -*-
import requests
import argparse
import sys
import unicodedata
import hashlib

DATADIR = "data/"

from url_validator import *
from make_hash import make_hash

def get_html(url):
    if not has_http( url ):
            exit(-1)
    results = requests.get( url , timeout=.2) 
    return results.text

def validate_with( validate_func, url):
    return validate_func(url)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="get the raw html content of a site.")
    argparser.add_argument('-u', dest='url', default='None', help="The URL to try.")
    argparser.add_argument('--output', dest='output', default='stdout', help="the type of ouptut. stdout or file")
    argparser.add_argument("-f", dest='filename', help='the filename to write to')
    args= argparser.parse_args()

    #set output type, file or stdout
    if args.output == 'file':
        filename = ""
        if args.filename:
            filename = args.filename
        else:
            filename = make_hash( args.url )
        args.output = open( DATADIR+filename+'.pu', 'w' )
    else:
        args.output = sys.stdout

    # visit then write out
    if validate_with(is_tip_top_level, args.url):
        uni_version = get_html(args.url)
        uni_version = unicodedata.normalize('NFC', uni_version).encode("ascii", 'xmlcharrefreplace')
        args.output.write( args.url + '\n' )
        args.output.write( uni_version )
    else:
        print "Sorry, requires URLS of the form 'http://www.<somesite>.<domain>' for now."
        exit(-2)

    ##close that shit out.
    try:
        output.close()
    finally:
        exit(0)

