import psycopg2
import datetime


def db_data():
    conn = psycopg2.connect(dbname='FROFY', user='postgres',
                            password='SA', host='localhost')
    cursor = conn.cursor()
    cursor.execute('select * from Товары')
    records = cursor.fetchall()
    conn.close()
    return records


def db_insert(data):
    conn = psycopg2.connect(dbname='FROFY', user='postgres',
                            password='SA', host='localhost')
    cursor = conn.cursor()
    insert_query = """
                    INSERT INTO Товары (Название, Цена, Количество, Адрес, Дата) values (%s, %s, %s, %s, %s)
                    """
    time_purchase = datetime.datetime.now()
    item_tuple = ('Тест товар', 400, 5, 'Рыбинск, Магазин 1', time_purchase)
    cursor.execute(insert_query, item_tuple)
    conn.commit()
    conn.close()
