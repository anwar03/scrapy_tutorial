# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from mysql import connector


class SpidermanPipeline:
    pass


class SpidermanPipeline:
    def __init__(self):
            self.create_connection()
            self.create_table()
        
    def create_connection(self):
        self.conn = connector.connect(
            host = "localhost",
            user = "spiderman",
            passwd = "spiderman",
            database = "spiderman"
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""
            create table quotes_tb(
                title text,
                author text,
                tag text
            )
        """)

    def store_db(self, item):
        self.curr.execute("""
        insert into quotes_tb values (%s, %s, %s)
        """,(item['title'], item['author'], item['tag'][0]))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline : " + item["title"])
        return item
