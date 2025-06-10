# /bot_config.py

class BotConfig:
    def __init__(self):
        self.prefixes = ['$']
        self.token = 'Token' # 봇 토큰
        self.version = '1.0.0'
        self.admin = [admin_id]

        # Cog 파일들이 저장된 폴더
        self.cogs_dir = 'cogs' 
bot_config = BotConfig()