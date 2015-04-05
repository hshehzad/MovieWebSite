# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 12:53:13 2015

@author: hs272x
"""
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
                
        