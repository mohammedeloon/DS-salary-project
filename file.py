import classdoor_scraper as gs
import pandas as pd
path =  'C:/Users/khatib/Documents/CS_salarry_proj/chromedriver'
df = gs.get_jobs('Cyber Security', 15, False, path, 15)