import logging
logging.basicConfig(level=logging.INFO)

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ContentType, Message, CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
						InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='1314059045:AAHANWfD9mkFP5ri2BsGiYw-YO3RptjO88k', parse_mode='HTML')
dp = Dispatcher(bot)

markup = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text='send contact', request_contact=True),
			KeyboardButton(text='send location', request_location=True)
		],
		[
			KeyboardButton(text='remove keyboard')
		]
	],
	resize_keyboard=True
)
# other options #1
# markup = ReplyKeyboardMarkup(resize_keyboard=True)
# markup.add(KeyboardButton(text='send contact', request_contact=True), KeyboardButton(text='send location', request_location=True))
# markup.add("btn3") # or markup.add(KeyboardButton(text='remove keyboard'))
# other options #2
# markup = ReplyKeyboardMarkup(resize_keyboard=True)
# markup.row(KeyboardButton(text='send contact', request_contact=True), KeyboardButton(text='send location', request_location=True))
# markup.row("btn3") # or markup.add(KeyboardButton(text='remove keyboard'))
# other options #3
# markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
# markup.insert(KeyboardButton(text='send contact', request_contact=True))
# markup.insert(KeyboardButton(text='send location', request_location=True))
# markup.insert('remove keyboard') # or KeyboardButton(text='remove keyboard')

inline_markup = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='inline_btn1', callback_data='1'),
			InlineKeyboardButton(text='inline_btn2', callback_data='2')
		],
		[
			InlineKeyboardButton(text='inline_btn3', url='https://vk.com/audios508091378')
		]
	]
)
# other options #1
# inline_markup = InlineKeyboardMarkup()
# inline_markup.add(InlineKeyboardButton(text='inline_btn1', callback_data='1'), InlineKeyboardButton(text='inline_btn2', callback_data='2'))
# inline_markup.add(InlineKeyboardButton(text='inline_btn3', url='https://vk.com/audios508091378'))
# other options #2
# inline_markup = InlineKeyboardMarkup()
# inline_markup.row(InlineKeyboardButton(text='inline_btn1', callback_data='1'), InlineKeyboardButton(text='inline_btn2', callback_data='2'))
# inline_markup.row(InlineKeyboardButton(text='inline_btn3', url='https://vk.com/audios508091378'))
# other options #3
# inline_markup = InlineKeyboardMarkup(row_width=2)
# inline_markup.insert(InlineKeyboardButton(text='inline_btn1', callback_data='1'))
# inline_markup.insert(InlineKeyboardButton(text='inline_btn2', callback_data='2'))
# inline_markup.insert(InlineKeyboardButton(text='inline_btn3', url='https://vk.com/audios508091378'))

@dp.message_handler(commands=['start', 'help'])
async def welcome(msg: Message):
	await msg.answer("<i>Welcome</i>", reply_markup=markup)
	# await bot.send_message(msg.chat.id, "<i>Welcome</i>", reply_markup=markup)

@dp.message_handler(content_types=ContentType.TEXT)
async def get_message(msg: Message):
	if msg.text == "remove keyboard":
		await msg.answer("<b>Keyboard removed</b>", reply_markup=ReplyKeyboardRemove())
		await msg.answer("Welcome", reply_markup=inline_markup)
	else:
		await msg.answer(f"\"'{msg.text}'\"")

@dp.message_handler(content_types=ContentType.CONTACT)
async def get_contact(msg: Message):
	await msg.answer(msg.contact.phone_number)

@dp.message_handler(content_types=ContentType.LOCATION)
async def get_location(msg: Message):
	await msg.answer(msg.location)

@dp.callback_query_handler()
async def inline_echo(call: CallbackQuery):
	await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="HI", reply_markup=None)
	await call.message.answer(call.data)
	# await bot.send_message(call.message.chat.id, call.data)
	await call.answer(text='Hello world', show_alert=True)
	# await bot.answer_callback_query(callback_query_id=call.id, text='Hello world', show_alert=True)

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)