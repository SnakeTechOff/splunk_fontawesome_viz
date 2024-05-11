#!/usr/bin/python3
# -*- coding: utf-8 -*-

###### Import ########

import re 

from os import listdir
from os.path import isfile, join

from bs4 import BeautifulSoup
from fontTools import ttLib

###### Variable ######

path = "../appserver/static/fontawesome/webfonts/"
output = "/opt/splunk/etc/apps/splunk_fontawesome_viz/appserver/static/html/icons_available.html"
attrs = dict()

attrs["section"] = {"id":"icons-list"}
attrs["ul"] = {"class":"list d-flex flex-row flex-wrap justify-content-start align-content-start m-0 p-0"}
attrs["li"] = {"class":"d-block m-0 pb-0 px-1 w-grid-2 w-grid-4-m w-grid-6-l w-grid-20-xl"}
attrs["div"] = {"class":"d-flex flex-column justify-content-center position-relative shadow-sm rounded-top border-radius-sm p-3 mb-2"}
attrs["span_img"] = {"class":"d-flex flex-column align-items-center color-inherit rounded-top border-radius-sm p-2 w-100 hover-bg-blue"}
attrs["i"] = {"style":"font-size: 48px;"}
attrs["div2"] = {"class":"text-center w-100 px-1 py-2"}
attrs["span_string"] = {"class":"db gray5 hover-gray7 text align-top user-select-all"}

###### Function ######

def get_icon_list(path):
    icons = dict()
    pattern = re.compile(r'fa-(\S+)-\d+.ttf')
    files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".ttf")]
    for f in files:
        match = pattern.match(f)
        if match:
            tt = ttLib.TTFont(join(path, f))
            icons[match.group(1).lower()] = tt.getGlyphNames()[1:]
    return icons

def get_new_section(soup, key, attrs):
    section = soup.new_tag("section", attrs=attrs["section"])

    h1 = soup.new_tag("h1")
    h1.append(key.title())
    section.append(h1)
    
    return section

def get_new_li(soup, key, icon, attrs):
    
    li = soup.new_tag("li", attrs=attrs["li"])
    div = soup.new_tag("div", attrs=attrs["div"])
    span_img = soup.new_tag("span", attrs=attrs["span_img"])
    div2 = soup.new_tag("div", attrs=attrs["div2"])
    span_string = soup.new_tag("span", attrs=attrs["span_string"])
    
    i = soup.new_tag("i", attrs={"class":f"fa-{key} fa-{icon}", **attrs["i"]})
    
    span_img.append(i)
    span_string.append(icon)
    div.append(span_img)
    div2.append(span_string)
    div.append(div2)
    li.append(div)
    
    return li

def main():
    icons = get_icon_list(path)
    keys_reverse = sorted(list(icons.keys()))[::-1]
    
    soup = BeautifulSoup("", "html.parser")

    for key in keys_reverse:
        
        section = get_new_section(soup, key, attrs)
        
        ul = soup.new_tag("ul", attrs=attrs["ul"])
        
        for i in icons[key]:
            li = get_new_li(soup, key, i, attrs)
            ul.append(li)

        section.append(ul)    
        soup.append(section)

    html = soup.prettify("utf-8")

    with open(output, "wb") as file:
        file.write(html)

###### Program #######

if __name__ == "__main__":
    main()
