import logging
from lib.DB import Database

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self, instance):
        self.db = Database
        self.logger = logging.getLogger("base_logger")
    
    def execute(self, query, args=None):

        with Database() as cursor:
            cursor.execute(query, args)

    def fetch_all(self, query, args=None):
        
        with Database() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchall()
        return result

    def fetch_one(self, query, args=None):
        
        with Database() as cursor:
            cursor.execute(query, args)
            result = cursor.fetchone()
        return result
