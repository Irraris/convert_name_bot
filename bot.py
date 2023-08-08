import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
  user_name = message.from_user.full_name
  user_id = message.from_user.id

  logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
  await message.answer(f"Здравствуйте, {user_name}! Введите ваше ФИО: ")

@dp.message_handler()
async def convert_to_latin(message: types.Message):
  user_id = message.from_user.id
  text = translit_name(message.text) # method translit_name is called
  logging.info(f'{user_id=} sent message: {message.text}')
  await bot.send_message(user_id, text)

def translit_name(text):
  translit = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 
            'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie','ы': 'y', 
            'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia', ' ': ' '}

  words = text.lower().split()
  latin_words = []

  if text.replace(' ', '').isalpha():
    for word in words:
        latin_word = ''
        for char in word:
            latin_char = translit.get(char, char)
            latin_word += latin_char
        latin_words.append(latin_word.capitalize())
    return ' '.join(latin_words)
  else:
    return 'ФИО может включать в себя только буквы'

if __name__ == '__main__':
  executor.start_polling(dp)
