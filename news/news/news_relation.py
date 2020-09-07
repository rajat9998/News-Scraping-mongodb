from pymongo import MongoClient
import settings

class NewsRelation:

    collection_name = 'News'

    def __init__(self):
        self.mongo_uri = settings.MONGO_URI
        self.mongo_db = settings.MONGO_DB
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = db[self.collection_name]

    def proceed(self):
        for item in self.collection.find():
            rel1 = self.db.relation1.insert_one({
                'url': item['url'],
                'blog_heading': item['blog_heading']
            })    

            rel2 = self.db.relation2.insert_one({
                'url': item['url'],        
                'meta_data': {
                    'title': item['title'],
                    'desc': item['desc'],
                    'img_url':  item['img_url'],
                    'votes': item['votes']
                }  
            })

            self.db.relation3.insert_one({
                'ID1': rel1.inserted_id,
                'ID2': rel2.inserted_id
            })


if __name__ == "__main__":
    NewsRelation().proceed()

