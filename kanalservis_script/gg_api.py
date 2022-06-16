import requests
import gspread
from datetime import datetime
from xml.etree import ElementTree as ET
from oauth2client.service_account import ServiceAccountCredentials as acc


def ggsheets(spreadsheet_name, sheet_num):
    """
    Connecting and reading to Google Sheets API
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials_path = '../kanalservise-9a82a0b9ccbb.json'

    credentials = acc.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_values()

    return sheet[1:]


def usd_rub():
    """
    Parsing of the USD rate by the CB of the RF
    """
    date_today = datetime.today().strftime('%d/%m/%Y')
    resp = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params={'date_req': date_today})

    tree = ET.fromstring(resp.content)

    value_course = float(tree.find('./Valute[@ID="R01235"]/Value').text.replace(',', '.'))

    return value_course, date_today
