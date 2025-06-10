# /main.py

import discord
from discord.ext import commands

import sys
import os

#cogs 내부에서 쓸 수 있게 절대 경로 지정
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from bot_config import bot_config




# Intents 설정
intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

# 봇 객체 생성
bot = commands.Bot(command_prefix=bot_config.prefixes, intents=intents)

# 봇이 Discord에 연결될 준비가 되었을 때 호출되는 코루틴
# 봇의 초기 설정, Cog 로드 등의 비동기 작업
@bot.event
async def on_ready():
    print(f'==========')
    print(f'Logged on as {bot.user}!')
    print(f'version={bot_config.version}')
    print('==========')
    print('Ready to load cogs...')

# setup_hook 설정정
async def setup_hook():
    print("Running setup_hook to load cogs...")
    
    # cogs 폴더가 없으면 생성 | 리스크 관리
    if not os.path.exists(bot_config.cogs_dir):
        os.makedirs(bot_config.cogs_dir)
        print(f"Created '{bot_config.cogs_dir}' directory.")

    # AdminCog를 먼저 로드
    admin_cog_filename = 'admin.py' # 실제 파일 이름에 맞춰 수정
    admin_cog_name = admin_cog_filename[:-3]
    try:
        if admin_cog_filename in os.listdir(bot_config.cogs_dir):
            await bot.load_extension(f'{bot_config.cogs_dir}.{admin_cog_name}')
            print(f'Successfully loaded AdminCog: {admin_cog_name}')
        else:
            print(f"AdminCog file '{admin_cog_filename}' not found in '{bot_config.cogs_dir}'. Skipping.")
    except Exception as e:
        print(f'Warning! Failed to load AdminCog {admin_cog_name}: {e}')

    # 나머지 Cog 파일을 로드 (admin_cog.py, __init__.py 제외)
    for filename in os.listdir(bot_config.cogs_dir):
        if filename.endswith('.py') and filename != admin_cog_filename and filename != '__init__.py':
            cog_name = filename[:-3] 
            try:
                await bot.load_extension(f'{bot_config.cogs_dir}.{cog_name}')
                print(f'Successfully loaded cog: {cog_name}')
            except Exception as e:
                print(f'Warning! Failed to load cog {cog_name}: {e}')
    print("All cogs processed by setup_hook.")
    print('==========')



bot.setup_hook = setup_hook


# 봇 실행
if __name__ == '__main__':
    bot.run(bot_config.token)