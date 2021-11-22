import os
import discord
import gspread
import keep_alive
from datetime import date
from discord.ext import commands

keep_alive.keep_alive()

bot = commands.Bot(command_prefix='$')

gc = gspread.service_account(filename="./rich-atom.json")
key = "1OnGn2yPXfVCRKLY6BhHMrUUfvokBClqgyX_bw7mmsOc"
sheet = gc.open_by_key(key).sheet1

@bot.command()
async def log(ctx,hours,info):
  row = sheet.row_values(3).index(str(ctx.message.author.id))+1
  col = len(sheet.col_values(row))+1
  sheet.update_cell(col,row,hours)
  sheet.update_cell(col+1,row,str(date.today()))
  sheet.update_cell(col+2,row,info)
  await ctx.send("Done!")

bot.run(os.getenv('token'))
