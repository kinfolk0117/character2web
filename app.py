from flask import Flask, request
from urllib.parse import urlparse
from pathlib import Path
import json

app = Flask(__name__)

import os
import openai
MAX_TOKENS = 2048

site_map = {
    "/index.html": "Home",
    "/sitemap.html": "Site Map",
}

# open characters.json
character = "NinjaNerd"
characters = open("characters.json").read()
characters = json.loads(characters)


# find character with nickname
for c in characters:
    if c["nickname"] == character:
        character_sheet = c["text"]




sys_prompt = """
You are a AI software that produces html pages for a person making a personal website on geocities. The year is 2002.

Here is a character sheet for the person making the website:
---
""" + character_sheet + """
---
The  user uses a lot of hyperlinks in her texts, linking between different pages".

Make up a lot of details about the person, add long texts describing her life and interests.

Add css for styling inline in the page. Make the design colors match the personality with a early 2000s vibe. Every page should have a header and menu with links to other pages.

Images can be added by using `https://source.unsplash.com/random/WIDTHxHEIGHT?KEYWORD` where KEYWORD is a keyword for the image, and width and height are the width and height of the image in pixels.

The webpage has an intricate design with many subpages, and a lot of internal links.

The user will request a page and you will return the html code for the page. You will only return the html code nothing else. No commentary or explanations.


Currently known pages:
"""


for page, description in site_map.items():
    sys_prompt += f"{page}: {description}\n"


sys_prompt += "You can add more pages, blog posts, essays to the website and site map by creating links to them. The user will request a page and you will return the html code for the page."


def summarize(page, content):
    # if file exists, return it
    msgs = []
    msgs.append ({"role": "system", "content": "Write a short summary of the content of this page on a personal website"})

    content = "PATH: " + page + "\nCONTENT:\n" + content
    msgs.append ({"role": "user", "content": content})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs, max_tokens=MAX_TOKENS)
    return response["choices"][0]["message"]["content"]

@app.route('/sitemap.html')
def get_sitemap():
    content = ""
    content += "<html><body><h1>Site Map</h1><ul>"
    for page, description in site_map.items():
        content += f"<li><a href='{page}'>{description}</a></li>"
    content += "</ul></body></html>"

    return content

def read_page_from_file(page):
    file_name = page_to_file_name(page)
    return open(file_name).read()


def page_to_file_name(page):
    # add index.html if ends with /
    if page.endswith("/"):
        page += "index.html"

    prefix = "./cache/" + character + "/"

    # remove leading /
    if page.startswith("/"):
        page = page[1:]
    # store in ./cache
    file_name = prefix + page

    # get dir and mkdir -p
    dir = os.path.dirname(file_name)
    Path(dir).mkdir(parents=True, exist_ok=True)
    return file_name

@app.route('/')
def index():
    return get_page("index.html")

def save_sitemap():
    with open("sitemap.html", "w") as f:
        f.write(get_sitemap())

@app.route('/<path:page>')
def get_page(page):
    file_name = page_to_file_name(page)

    # if file exists, return it
    if os.path.isfile(file_name):
        return open(file_name).read()
    msgs = []
    msgs.append ({"role": "system", "content": sys_prompt})

    referrer_msg = ""
    if request.referrer:
        referer_path = urlparse(request.referrer).path
        print("referer_path: " + referer_path)

        referrer_msg += "The user is currently on this page: {request.referrer}\n"
        referrer_msg += "with content:\n"
        referrer_msg  += read_page_from_file(referer_path) + "\n"


    request_msg = "REQUEST: " + page
    content = referrer_msg + request_msg
    msgs.append ({"role": "user", "content": content})
    print("new page requested: " + page)
    print("prompts" + str(msgs))

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs, max_tokens=MAX_TOKENS)
    print(response)
    content = response["choices"][0]["message"]["content"]


    # find first markdown code block ``` or ```html
    start = content.find("```")

    end = content.find("```", start + 3)
    if start != -1 and end != -1:
        # start on next line
        start = content.find("\n", start) + 1
        content = content[start:end]

    # write page to file
    with open(file_name, "w") as f:
        f.write(content)

    # save page to sitemap
    site_map[page] = summarize(page, content)

    return content

