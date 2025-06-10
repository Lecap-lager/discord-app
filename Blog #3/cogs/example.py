#/cogs/example.py

import discord
from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("ExampleCog has been initialized.")

    # 이 Cog가 로드되었을 때 (봇 재시작 또는 Cog 로드 시) 실행될 이벤트
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"ExampleCog: Cog is ready! (from {self.bot.user})")

    # 이 Cog가 로드되었을 때 실행될 명령어
    @commands.command(name='안녕')
    async def hello_from_cog(self, ctx):
        await ctx.send(f'안녕하세요, {ctx.author.mention}! ExampleCog에서 인사드립니다.')


##########
# 이 함수는 discord.py가 Cog 파일을 확장으로 로드할 때 호출합니다.
async def setup(bot):
    await bot.add_cog(ExampleCog(bot))
    print("$$ ExampleCog setup complete.")

# 이 함수는 Cog가 언로드될 때 호출됩니다.
async def teardown(bot):
    print("ExampleCog is being unloaded.")