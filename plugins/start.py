from pyrogram import Client, filters, StopPropagation
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"السلام عليكم يا  <b>{message.from_user.first_name}</b>\n أنا بوت أقوم بالتحميل من يوتيوب \n\n فقط أرسل رابط الفيديو و اختر الجودة والصيغة \n\n ممنوع استخدام البوت لتحميل الأغاني أو المسلسلات أو الشيلات أو أي شيء حرام \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n لدعم استمرار المشروع هنا \n\n http://paypal.me/kelectronic89 \n\n محلوظة / البوت بطيء في الرفع . شكراً لتفهمك  "
    await message.reply_text(welcomed)
    raise StopPropagation
