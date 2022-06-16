import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest

env_path = os.path.abspath('../.env')
load_dotenv(dotenv_path=env_path)

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')


def con_teleg(order_number, guest_phone_number=None):
    # senders phone number
    phone_number = '+79xxxxxxxxx'

    # receivers phone number
    guest_phone_number = '+79xxxxxxxxx'

    client = TelegramClient('session_name',
                            api_id,
                            api_hash)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter code: '))

    send_mes(client, guest_phone_number, order_number)


def send_mes(client, guest_phone_number, order_number):
    # add user to contact
    contact = InputPhoneContact(client_id=0, phone=guest_phone_number, first_name="user", last_name=" ")
    result = client.invoke(ImportContactsRequest([contact]))

    # send message to receivers
    client.send_message(result.users[0], f'Доставка заказа № {order_number} просрочена')

