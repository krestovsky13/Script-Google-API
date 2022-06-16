from time import sleep

from kanalservis_script import postg
from kanalservis_script.gg_api import ggsheets


def main():
    """
    Checking Google Sheets data online (every 5 seconds)
    """
    before_sheet = ''
    while True:
        print('checking changes...')
        now_sheet = ggsheets('test', 0)
        data = [[x if x else None for x in i] for i in now_sheet]
        if data != before_sheet:
            before_sheet = data
            postg.con_db('test', data)
        sleep(5)


if __name__ == '__main__':
    main()
