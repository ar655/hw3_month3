from aiogram import types ,Dispatcher
from aiogram.dispatcher import FSMContext
from config import bot,ADMIN
from aiogram.dispatcher.filters.state import State,StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    dicript = State()
    price = State()

async def fsm_start(message:types.Message):
    if message.from_user.id not in ADMIN:
        await  message.answer('error')
    else:
        await FSMAdmin.photo.set()
        await message.answer('send food picture')

async  def load_photo(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('send food name')

async def load_name(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('send food discription')



async  def load_dicript(message:types.Message ,state :FSMContext):
    async with state.proxy() as data:
        data['discription'] = message.text
    await FSMAdmin.next()
    await message.answer('send food price')

async  def load_price(message:types.Message,state:FSMContext):
    if message.text.isalpha():
        await message.answer('only numbers')
    else:
        async with state.proxy() as data:
            data['food price'] = message.text
            await bot.send_photo(message.from_user.id,data['photo'],
                                 caption=f"food name:{data['name']}\n"
                                         f"food discription:{data['discription']}\n"
                                         f"food price:{data['food price']}\n"
                                 )
    await state.finish()





def register_handlers_fsmAdminmenu(dp:Dispatcher):
    dp.register_message_handler(fsm_start,commands=['update_menu'])
    dp.register_message_handler(load_photo ,state=FSMAdmin.photo,content_types=['photo'])
    dp.register_message_handler(load_name,state=FSMAdmin.name)
    dp.register_message_handler(load_dicript,state=FSMAdmin.dicript)
    dp.register_message_handler(load_price,state=FSMAdmin.price)





