
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import re
import json
import time


url= 'https://www.rollingstone.com/culture/culture-lists/50-best-stand-up-comics-of-all-time-126359/russell-peters-127224/'
with open('ytb_token.txt', 'r') as f:
    ytb_key = f.readlines()


def read_url(url):
    """This function returns the parsed content of the url in a 'soup'. """
    html = requests.get(url).content
    soup = bs(html, 'html.parser')
    return soup



def find_names(soup):
    """This function is the first round of cleaning the soup so we can get the names 
    that still have some trash string."""
    names = soup.find_all("header")
    dirty = [names[i] for i in range(len(names))]
    almost_clean = [dirty[i].text for i in range(len(dirty))]
    return almost_clean 
    



def clean_name(lst):
    """This function takes the names with some extra strings and cleans them."""
    clean_n =[]
    for s in lst:
        s = str(s)
        s = s.replace("\n","")
        s = s.replace("\t","")
        s = re.sub("\d", "", s)
        clean_n.append(s)
    
    return clean_n



def obtain_final_list(almost_clean):
    """This list takes the list of names and only selects names. 
    That list includes other stuff like publicity for the magazine, so we select
    only the names."""
    lst_semi = almost_clean[2:-8]
    final_list = lst_semi[::-1]
    short_version = final_list[:10]
    return short_version



def create_dataframe(short_version):
    """This list receives as an input the final list of names and returns
    a data frame that also has a ranking column. The code is easy to understand."""
    df = pd.DataFrame(index=[x for x in range(1,11)])
    df['Comedian'] = short_version
    df.index.name = "Ranking"
    return df 


def exe(url):
    """Finally, this function takes all the previous functions and executes the process cleanly."""
    x = read_url(url)
    y = find_names(x)
    z = clean_name(y)
    w = obtain_final_list(z)
    f = create_dataframe(w)
    return f


def get_names_youtube(url):
    """The purpose of this function is to get the names without a space 
    so I can put that name directly in the youtube search"""
    names_youtube = []
    x = read_url(url)
    y = find_names(x)
    z = clean_name(y)
    w = obtain_final_list(z)
    for e in w:
        e = re.sub(r"\W","",e)
        names_youtube.append(e)
    return names_youtube


#aquí iría el with open
def list_links_api(get_name_youtube):
    """The purpose of this function is to generate the relevant youtube search 
    link for each comedian, with the API key included and all."""
    list_links = []
    str_basic = f"https://www.googleapis.com/youtube/v3/search?part=snippet&order=ViewCount&maxResults=5&key={ytb_key}&q="
    list_links = [str_basic + e for e in get_name_youtube]
    return list_links


def get_titles(list_links):
    list_titles = []
    for link in list_links: 
        html = requests.get(link)
        info = json.loads(html.text)
        x = info.get("items")
        y = x[0]
        z = y['snippet']['title']
        list_titles.append(z)
        time.sleep(10)
    return list_titles


def get_links(list_links):
    list_youtube=[]
    basic="https://youtube.com/watch?v="
    for link in list_links:
        try: 
            html = requests.get(link)
            info = json.loads(html.text)
            x = info.get("items")
            y = x[0]
            z = y['id']['videoId']
            z = str(z)
            list_youtube.append(basic+z)
            time.sleep(10)
        except KeyError:
            list_youtube.append("Link not found.")
        
    return list_youtube


def clean_titles(list_titles):
    """This function cleans the youtube titles that the past function gave me."""
    clean_t = []
    for t in list_titles:
        t = t.replace("#","")
        t = t.replace("3","")
        t = t.replace(";","")
        t = re.sub("&9", "", t)
        t = t.lower()
        t = t.title()
        t = re.sub("&Amp", "and", t)
        clean_t.append(t)
    return clean_t



def assign_new_columns(df, clean_ytb_titles, clean_ytb_links, clean_parag_final):
    """This function creates two new columns in the data frame:
    the first has the most viewed youtube video and the second
    has the link to that youtube video."""
    df['Description'] = clean_parag_final
    df['Most Watched Youtube Video'] = clean_ytb_titles
    df['Link'] = clean_ytb_links
    return df


def clean_paragraphs(list_paragraphs):
    """This function helps us clean the comedian description."""
    clean_parag = []
    for p in list_paragraphs:
        p = p.replace("\'", "")
        p = p.strip()
        clean_parag.append(p)
    return clean_parag





def get_paragraphs(url):
    """This function will get the comedian's description with 
    string trash so we can clean that later in the function 
    called clean_paragraph"""
    list_parag_dirty = []
    html = requests.get(url).content
    soup= bs(html, 'html.parser')
    para = soup.find_all("p")
    list_1 = para[10:64]
    list_2 = list_1[::-1]
    for e in list_2[:10]:
        e = e.text
        list_parag_dirty.append(e)
        
    return list_parag_dirty



def exe(url):
    """Finally, this function takes all the previous functions and executes the process cleanly."""
    x = read_url(url)
    y = find_names(x)
    z = clean_name(y)
    w = obtain_final_list(z)
    f = create_dataframe(w)
    p1 = get_paragraphs(url)
    p2 = clean_paragraphs(p1)
    v1 = get_names_youtube(url)
    v2 = list_links_api(v1)
    lst_titles = get_titles(v2)
    clean_t = clean_titles(lst_titles)
    lst_searches_links = get_links(v2)
    f = assign_new_columns(f,clean_t,lst_searches_links,p2)
    return f


final = exe(url)
print(final.head(10))

