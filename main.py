import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список товаров
PRODUCTS = [
    {"name": "hp Victus 15", "price": "500$"},
    {"name": "Iphone 11pro", "price": "300$"},
    {"name": "airpods 2pro", "price": "180$"},
    {"name": "Apple watch SE2", "price": "150$"}
]

@dp.message(Command("start"))
async def start_command(message: Message):
    welcome_text = "Добро пожаловать в наш онлайн-магазин!\n\nВот список доступных товаров:"
    product_list = "\n".join(
        f"{i + 1}. {product['name']} - {product['price']} руб." for i, product in enumerate(PRODUCTS)
    )
    instructions = "\n\nНапишите номер товара, чтобы выбрать его."
    await message.answer(welcome_text + "\n\n" + product_list + instructions)

@dp.message()
async def handle_product_selection(message: Message):
    try:
        # Преобразование введенного текста в число
        product_index = int(message.text) - 1

        # Проверяем, что номер корректный
        if 0 <= product_index < len(PRODUCTS):
            selected_product = PRODUCTS[product_index]
            await message.answer(
                f"Вы выбрали: {selected_product['name']}.\nЦена: {selected_product['price']} руб."
            )
        else:
            await message.answer("Товара с таким номером нет. Попробуйте снова.")
    except ValueError:
        await message.answer("Пожалуйста, введите номер товара.")

async def main():
    print("Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск основного цикла
if __name__ == "__main__":
    asyncio.run(main())
