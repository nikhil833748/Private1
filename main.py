import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# 🔹 API Details
API_KEY = "6980|cxfHx9Li5z7VPN9m4p7WOtXJvP1Iev0NfBg7ThKd"
API_URL = "https://zylalabs.com/api/6202/indian+vehicle+details+api/8654/rto+verification"

# 🔹 Authorized Group ID (Replace with actual chat_id)
AUTHORIZED_GROUP_ID = -1002320210604  # <- Replace this with your group ID

# ✅ Function to fetch vehicle details
def get_vehicle_details(vehicle_number):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"vehicle_number": vehicle_number}
    response = requests.post(API_URL, headers=headers, json=data)

    print(f"🔹 API Response: {response.status_code}")  # Debugging
    print(response.text)  # Debugging

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "❌ Invalid response from API"}

# ✅ Function to format response
def format_vehicle_details(data):
    if "error" in data:
        return "❌ Error fetching details. Please check the vehicle number."

    return f"""
🚗 *Vehicle Information*

📌 *RC Number:* `{data.get('license_plate', 'N/A')}`
👤 *Owner Name:* `{data.get('owner_name', 'N/A')}`
👨‍👦 *Father Name:* `{data.get('father_name', 'N/A')}`
🏠 *Permanent Address:* `{data.get('permanent_address', 'N/A')}`
🚘 *Vehicle Model:* `{data.get('brand_model', 'N/A')}`
🎨 *Color:* `{data.get('color', 'N/A')}`
⛽ *Fuel Type:* `{data.get('fuel_type', 'N/A')}`
📅 *Registration Date:* `{data.get('registration_date', 'N/A')}`
✅ *Registration Valid Up To:* `{data.get('tax_upto', 'N/A')}`
🛡 *Insurance Policy No:* `{data.get('insurance_policy', 'N/A')}`
🔧 *Engine Number:* `{data.get('engine_number', 'N/A')}`
🔩 *Chassis Number:* `{data.get('chassis_number', 'N/A')}`
📞 *Owner Mobile No:* `N/A`
⚖️ *Gross Vehicle Weight:* `0`
💳 *Financer:* `{data.get('financer', 'N/A')}`
🛣 *Registration Place:* `{data.get('source', 'N/A')}`
⚠️ *Blacklist Status:* `None`
🛠 *Vehicle Category:* `{data.get('norms', 'N/A')}`
🚦 *Permit Validity:* `{data.get('permit_valid_upto', 'None')}`
📏 *Wheelbase:* `999999`

🔍 *Extra Information:*
🔒 *NOC Valid Upto:* `{data.get('noc_details', 'None')}`
💼 *Number of Cylinders:* `{data.get('cylinders', 'N/A')}`
🔐 *PUC Valid Upto:* `{data.get('pucc_upto', 'None')}`
📅 *Permit Expiry Date:* `{data.get('permit_valid_upto', 'None')}`
🌍 *State:* `{data.get('source', 'N/A')}`
💡 *Vehicle Type:* `{data.get('seating_capacity', 'N/A')}`
🏎 *Vehicle Variant:* `None`
🏠 *Current Address:* `{data.get('present_address', 'N/A')}`
🌟 *Status:* `{data.get('rc_status', 'ACTIVE')}`
🏍 *Body Type:* `SOLO`
💼 *NOC Details:* `{data.get('noc_details', 'None')}`
🛠 *Manufacture Year:* `{data.get('registration_date', 'N/A').split('-')[0]}`  
🗺 *Registered Place:* `{data.get('source', 'N/A')}`
📱 *PUC Number:* `{data.get('pucc_number', 'N/A')}`
🔑 *Task ID:* `N/A`
📅 *Status Date:* `N/A`
📞 *NOC Issue Date:* `None`
💳 *Permit No:* `{data.get('permit_number', 'None')}`
🌍 *Manufacturer:* `{data.get('brand_name', 'N/A')}`
📅 *MV Tax Upto:* `{data.get('tax_upto', 'N/A')}`
🔍 *Norms Type:* `{data.get('norms', 'N/A')}`
📅 *Insurance Validity:* `{data.get('insurance_expiry', 'None')}`
🛣 *NPermit Upto:* `{data.get('national_permit_upto', 'None')}`
🔩 *Engine Number:* `{data.get('engine_number', 'N/A')}`
📱 *Insurance Name:* `{data.get('insurance_company', 'N/A')}`
🌐 *PUC Status:* `id_found`
"""

# ✅ Start Command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 Welcome! Send me a vehicle number (e.g. *MH02FB2727*) to get details.", parse_mode="Markdown")

# ✅ Function to handle messages
async def handle_message(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    # ✅ Check if message is from the authorized group
    if chat_id != AUTHORIZED_GROUP_ID:
        await update.message.reply_text("❌ This bot only works in @RtoVehicle. Please join the group to use it!")
        print("❌ Unauthorized access attempt!")  # Debug log
        return

    vehicle_number = update.message.text.upper()
    details = get_vehicle_details(vehicle_number)
    response_text = format_vehicle_details(details)

    await update.message.reply_text(response_text, parse_mode="Markdown")

# ✅ Main function to run bot
def main():
    BOT_TOKEN = "7738466078:AAFFSbV6m5VYmnBDjWfwufGvBHH9jya1qX8"
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running...")
    import asyncio
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    app.run_polling()

if __name__ == "__main__":
    main()
