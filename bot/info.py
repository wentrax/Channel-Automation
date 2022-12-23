from os import getenv

class Config(object):      
      ADMIN_ID = "1903280447"     
      FILES_FROM_CHANNEL = "@bdbdhdhvh"       
      FILES_TO_CHANNEL = -1001531149575
      FILES_CAPTION = "@HQFilms4U"
      AUTO_FILTER_CHANNEL =  -1001743048821   
      MULTI_CHANNEL_FORWARD_IDS = list(x for x in getenv("CHANNEL_ID", "-1001688669689:-1001641840781").replace("\n", " ").split(' '))
      

