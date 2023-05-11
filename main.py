# pip install pytube
# pip install pyrogram

from pytube import YouTube 

import os

from pyrogram import filters , Client

app = Client(

  "my_bot",

  api_id=9176863,

  api_hash="afff208ad0de11acfc946ca6dcd74aec",

  bot_token="5844126858:AAEdmmujFdMr0rXhalHTRzmqorxzd62G1_c"

)

@app.on_message(filters.command("ytdl") & filters.private)

def yt(_,message):

  link = message.text.split("/ytdl")[1]

  bruh = message.reply("Downloading...")

  video= YouTube(link)

  video = video.streams.get_highest_resolution()

  try:

    video.download(output_path="./downloads")

  except:

    message.reply_text("error")

  bruh.delete()

  a =  message.reply_text("Uploading...")

  app.send_video(chat_id=message.chat.id, video="./downloads/" + video.default_filename)

  os.remove("./downloads/" + stream.default_filename)

        

app.run()
