from bs4 import BeautifulSoup as bsoup
import hashlib
import argparse
import sys
import url_validator as validator 

#note all the shit we see


# url | title | links_from_here | links_to_here | #images_on_site | #videos_on_site | #documents_on_site | n_grams_from_text | 
# links:    mailto, javascript, discard div elements, http::// ftp:// file: ... etc.
#   how many http://... type headers are there?


def get_body_text(tags):
    body_text = []
    for item in tags.body.find_all('p'):
        body_text.append( item.text )
    return body_text

def get_image_count( tags ):
    return len(tags.find_all('img'))

def get_image_list( tags ):
    imgs = []
    for image in tags.find_all('img'):
        text = image.get('alt')
        source = image.get('src')
        height = image.get('height')
        width = image.get('width')
        size = None
        if height and width:
            size = (height,width)
        imgs.append( ( text, source, size ) )
    return imgs


            


def get_scripts( tags ):
    scripts = []
    for script in tags.find_all('script'):
        script_src = script.get('src')
        if script_src:
            scripts.append( script_src )
        else:
            scripts.append(script)
    return scripts

def get_tags(html):
    soup = bsoup( html, 'html.parser' )
    return soup 

def get_links( tags ):
    links = []
    for link in tags.find_all('a'):
            url = link.get('href')
            #check whether we have a bunch of relative links, or tags, or scripts or even just garbage
            if validator.non_shitty_link(url):
                url = validator.clean_crappy_link(url)
                if validator.relative_link( url ) or not (validator.has_http(url) or validator.has_https(url) ):
                    url = validator.make_non_relative_link( site_url, url ) #this seems inefficient...
                 
                links.append(url)
    return links

if __name__=="__main__":
    argparser = argparse.ArgumentParser(description="get the raw html content of a site.")
    argparser.add_argument("--input", dest='input_name', help='the filename to read_from')
    args = argparser.parse_args()
    if not args.input_name:
        exit(-1)
    try:
        html_file = open(args.input_name, "r")
        site_url = html_file.readline()
        data = html_file.read()
        tags = get_tags(data)
        print tags.title.string
        
        #gather links
        links = get_links(tags)
        for link in links:
            print link
        
        scripts = get_scripts(tags) ##grab all the scripts, in place or linked.
        print scripts

        print get_image_count(tags) ##count how many images on the site
        print get_image_list(tags)  ## get all the info about the images
        body_text = get_body_text( tags )
        

    finally:
        html_file.close()