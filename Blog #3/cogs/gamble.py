#/cogs/gamble.py

import random

import discord
from discord.ext import commands

class GamblingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("GamblingCog has been initialized.")

    def coinflip(self):
        return random.randint(0, 1)
    
    # 이 Cog가 로드되었을 때 (봇 재시작 또는 Cog 로드 시) 실행될 이벤트
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"GamblingCog: cog is ready! (from {self.bot.user})")

    # 이 Cog가 로드되었을 때 실행될 명령어
    @commands.command()
    async def gamble(self, ctx):

        result = self.coinflip()
        if result == 0 :
                result = '뒷면'
                return await ctx.send(f'동전 던지기의 결과는? {result}! ')  
        elif result == 1 :
                result = '앞면'
                return await ctx.send(f'동전 던지기의 결과는? {result}! ')  
        

##########
# 이 함수는 discord.py가 Cog 파일을 확장으로 로드할 때 호출합니다.
async def setup(bot):
    await bot.add_cog(GamblingCog(bot))
    print("$$ GamblingCog setup complete.")

# 이 함수는 Cog가 언로드될 때 호출됩니다.
async def teardown(bot):
    print("GamblingCog is being unloaded.")