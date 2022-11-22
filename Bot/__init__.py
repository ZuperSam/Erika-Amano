import os, sys, logging
from pyrogram import Client 

if os.path.exists('error.log'):
    os.remove('error.log')
        
#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO, filename='error.log')
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5562438875:AAHKfFy6PdRkrEBqlt6w2mqghtlOKB19kSo') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 8978848)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', '24ce3cff2d32cf529df1c0018e28d6cf')# Telgram App hash  
OWNER_ID = int(os.environ.get('OWNER_ID', 1995886602))
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://Botlover:Botlover@cluster0.e1ymmrm.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001810558901)
BOT_NAME = os.environ.get('BOT_NAME', 'Zub0Compress1_bot')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
