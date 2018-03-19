# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class SunmoivePipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE local_db")
        sql = "INSERT INTO sunmoive VALUES(%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (item['cate_name'], item['cate_url'], item['cate_url_list'],item['moive_url'],item['moive_name'], item['moive_source']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>", e, "<<<<<<错误在这里")
            dbObject.rollback()
        return item

