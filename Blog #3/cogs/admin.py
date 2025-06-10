# /cogs/admin_cog.py

import discord
from discord.ext import commands
import os

from bot_config import bot_config



class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"$$ AdminCog: cog is ready! (from {self.bot.user})")

    # cogs 폴더 안의 코드를 수정 시 재부팅 할 필요 없이 적용
    @commands.command(name='restart', aliases=['reload']) # 명령어 이름 추가 및 별칭 추가
    async def restart_cogs(self, ctx):
        # bot_config.admin 리스트에 봇 관리자 ID를 추가 <- 중요
        if ctx.author.id not in bot_config.admin:
            return await ctx.send(
                '`권한이 없습니다.'
                '\n❗ 봇 관리자라면 config 파일의 admin 리스트에 디스코드 ID를 추가하여주십시오`')

        command = await ctx.send("```모듈을 다시 불러오는 중...```")
        
        # admin.py, __init__.py 은 제외
        cog_list = [
            i[:-3] for i in os.listdir(bot_config.cogs_dir) 
            if i.endswith('.py') and i not in ['__init__.py', 'admin.py']
        ]

        # 모든 확장(Cog)을 다시 로드
        for cog_name in cog_list:
            try:
                await self.bot.reload_extension(f"{bot_config.cogs_dir}.{cog_name}")
                print(f"'{cog_name}' reloaded")
            except commands.ExtensionNotLoaded:
                print(f"'{cog_name}'는 로드되지 않은 상태이므로 재로드할 수 없습니다. loading.")
                try:
                    await self.bot.load_extension(f"{bot_config.cogs_dir}.{cog_name}")
                    print(f"'{cog_name}' load complete.")
                except Exception as e:
                    print(f"'{cog_name}' reload fail: {e}")
            except Exception as e:
                print(f"'{cog_name}' reload fail: {e}")

        await command.edit(content="```cs\n'reload complete'```")
        print("All cog reload complete.")


# discord.py가 Cog 파일을 확장으로 로드할 때 호출
async def setup(bot):
    await bot.add_cog(AdminCog(bot))
    print("$$ AdminCog setup complete.")

# Cog가 언로드될 때 호출
async def teardown(bot):
    print("$$ AdminCog is being unloaded.")