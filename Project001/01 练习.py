# bs4伪装通用框架.py
import requests
from bs4 import BeautifulSoup
newsoup=BeautifulSoup("<b><!--This is a comment--></b>\
    <p>This is not a comment</p>","html.parser")
newsoup.b.string
type(newsoup.b.string)
newsoup.p.string
type(newsoup.p.string)