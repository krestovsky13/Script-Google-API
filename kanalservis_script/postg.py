import os
import psycopg2
from math import ceil
from dotenv import load_dotenv

from .gg_api import usd_rub
from main import main
from .mes_teleg import con_teleg

env_path = os.path.abspath('../.env')
load_dotenv(dotenv_path=env_path)


def sql_action(tb_name, connection, cursor, data):
    """
    Writing Google Sheets data to the PostgreSQL
    """
    value_course, date_today = usd_rub()
    try:
        sql_drop = f'''DROP TABLE IF EXISTS {tb_name} CASCADE;'''
        sql_create = f'''CREATE TABLE IF NOT EXISTS {tb_name}
                                    (
                                        №_id          int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                                        заказ_№       int,
                                        стоимость_$   float4,
                                        стоимость_руб float4,
                                        срок_поставки date
                                    );'''
        cursor.execute(sql_drop)
        # connection.commit()

        cursor.execute(sql_create)
        # connection.commit()

        for i in data:
            sql_insert = f'''INSERT INTO {tb_name} (заказ_№, стоимость_$, стоимость_руб, срок_поставки) 
                              VALUES (%s, %s, %s, to_date(%s, 'DD/MM/YYYY'));'''
            if i[2]:
                rub = ceil(float(i[2]) * value_course)
            else:
                rub = None
            if i[3]:
                i[3] = str(i[3])

                # if i[3] < date_today:
                    # if the database stores user numbers (i[4])
                    # con_teleg(i[1], i[4])

            cursor.execute(sql_insert, (i[1], i[2], rub, i[3]))
        connection.commit()
        print('db updated...')
    except psycopg2.Error as error:
        print(error)
        connection.rollback()
        main()


def con_db(tb_name='test', data=None):
    """
    Connect to PostgreSQL
    """
    with psycopg2.connect(user=os.getenv('POSTGRES_USER'),
                          password=os.getenv('POSTGRES_PASSWORD'),
                          host=os.getenv('POSTGRES_HOST'),
                          port=os.getenv('POSTGRES_PORT'),
                          database=os.getenv('POSTGRES_DB')) as conn:
        with conn.cursor() as curs:
            sql_action(tb_name, conn, curs, data)
