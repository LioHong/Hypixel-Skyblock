# -*- coding: utf-8 -*-
"""
Filename: hs_collections_organiser.py
Date created: Mon Aug 24 21:06:15 2020
@author: Julio Hong
Purpose: Read wikitable to generate an Excel file
Steps: 
"""

import pandas as pd
from os import path
# I thought this would be useful but actually not really. It can't even scrape all the content properly.
import wikia
from wikia import html

# To adjust the dataframe appearance
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)

wikia.summary("Hypixel-Skyblock", "Collections")
collections_page = wikia.page("Hypixel-Skyblock", "Collections")
# I might as well scrape html using another more commonly-used lib.
html = collections_page.html()

# Each skill collection falls under table class=wikitable.
# But each item has a less consistent format.
# Kind of falls under 'tr' elem, but it's not unique to items
# Can also apply to tiers, or counts, or rewards.
# I can pull the data out. But how to organise it? That's the concern.