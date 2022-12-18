# @Lx_0988
import logging
from AutoForward import CAPTION_TEXT
from pyrogram import Client, filters, enums
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

caption_text = CAPTION_TEXT

@Client.on_message(filters.channel & (media_filter))
async def editing(bot, message):
      try:
         media = message.document or message.video or message.audio
         caption_text = CAPTION_TEXT
      except:
         caption_text = ""
         pass 
      if (message.document or message.video or message.audio): 
          if message.caption:                        
             file_caption = f"**{message.caption}**"                
          else:
             fname = media.file_name
             filename = fname.replace("_", ".")
             file_caption = f"`{filename}`"  
              
      try:                       await bot.edit_message_caption(
                 chat_id=message.chat.id, 
                 message_id=message.id,
                 caption=file_caption.replace("Latest_Movies_Reborn", "DXClassic"),
                 parse_mode=enums.ParseMode.MARKDOWN
             )

      except:
          pass
