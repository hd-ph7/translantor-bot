import discord
from discord.ext import commands
from mtranslate import translate
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    original_text = message.content

    try:
        detected_lang = detect(original_text)
    except LangDetectException:
        detected_lang = 'unknown'

    translated_text_en = None
    translated_text_ru = None
    translated_text_pt = None
    translated_text_es = None

    if detected_lang != 'en':
        translated_text_en = translate(original_text, 'en')
    if detected_lang != 'ru':
        translated_text_ru = translate(original_text, 'ru')
    if detected_lang != 'pt':
        translated_text_pt = translate(original_text, 'pt')
    if detected_lang != 'es':
        translated_text_es = translate(original_text, 'es')

    response = f""

    if translated_text_en and translated_text_en != original_text:
        response += f"\n\n*{translated_text_en}*"
    if translated_text_ru and translated_text_ru != original_text:
        response += f"\n\n*{translated_text_ru}*"
    if translated_text_pt and translated_text_pt != original_text:
        response += f"\n\n*{translated_text_pt}*"
    if translated_text_es and translated_text_es != original_text:
        response += f"\n\n*{translated_text_es}*"

    await message.channel.send(response)

    await bot.process_commands(message)

bot.run('MTE0MDgwMDg2MDQ3ODI1OTI5MQ.GLnEAe.LKvyaHgsgRqzl8hWSs4IlpIdzqhYQ5g2agTu6Y')
