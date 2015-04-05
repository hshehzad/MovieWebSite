# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 13:10:09 2015

@author: hs272x
"""

import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story", "A Story of a boy and his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/c/c4/Toy_Story_Soundtrack.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
movies_list=[toy_story]
fresh_tomatoes.open_movies_page(movies_list)