# News-Scraping-mongodb

This is a Scrapy project to scrape news from News site [HN News](https://news.ycombinator.com/)

## Extracted data

This project extracts news, combined with title, url and votes. Also extracts the news description & possible image_url. The extracted data looks like this sample:

```
{
  'url': 'view-source:https://www.sciencemag.org/news/2020/09/one-quantum-physics-greatest-paradoxes-may-have-lost-its-leading-explanation',
  'title' : 'Gravity is unlikely to be the cause of quantum collapse, experiment suggests',
  'votes': 41,
  'blog_heading': 'One of quantum physics’ greatest paradoxes may have lost its leading explanation',
  'img_url': 'https://www.sciencemag.org/sites/default/files/styles/article_main_image_-_1280w__no_aspect_/public/Quantum_Gravity_1280x720.jpg?itok=YadpErLG',
  'desc': 'Gravity is unlikely to be the cause of quantum collapse, suggests an underground experiment at Italy’s Gran Sasso National Laboratory.'
}
```

## Requirements

```
$ pip install scrapy
$ pip install validators
$ pip install pymongo
```

## 1. Running the Spiders

We can run a spider using the ```scrapy crawl``` command as:

```
$ cd News
$ scrapy crawl news
```

## 2. Maintaining relational meta-data

We can maintain two relation- one with the url and heading of the blog and other one with url and its meta-data like (Description, Image, Title, Votes)

```
$ cd News
$ python news_relation.py
```
Note: We need to crawl first in order to obtain scrapped data.

## 3. Glance at our mongoDB database

We look for  ```newsYcombinator``` and use the db:

```
> show dbs

> use newsYcombinator
```

Then,

```
> show collections

result:
News
relation1
relation2
relation3
```

### In a nutshell

1. ```News``` contains the scapped data from (https://news.ycombinator.com/)

```
{
  "_id" : ObjectId("5f573c2d26f82d4e17ea39d3"),
  "url" : "https://www.apple.com/newsroom/2020/09/apple-marina-bay-sands-opens-thursday-in-singapore/",
  "blog_heading" : "Apple Marina Bay Sands opens Thursday in Singapore - Apple",
  "title" : "Apple Marina Bay Sands Opens Thursday in Singapore",
  "desc" : "Apple’s most ambitious retail project sits on the waters of Marina Bay",
  "img_url" : "/content/dam/newsroom/images/environments/stores apple_nso-marina-bay-sands_exterior_09072020_Full-Bleed-Image.jpg/_jcr_content/renditions/large.jpg",
  "votes" : 11
}
```

2. ```relation1``` contains url and heading of blog along with _id

```
{
  "_id" : ObjectId("5f573da75db73d3b8b2ed937"),
  "url" : "https://www.apple.com/newsroom/2020/09/apple-marina-bay-sands-opens-thursday-in-singapore/",
  "blog_heading" : "Apple Marina Bay Sands opens Thursday in Singapore - Apple"
}
```

3. ```relation2``` contains url and its meta-data (Description, Image, Title, Votes) along with _id

```
{
  "_id" : ObjectId("5f573da85db73d3b8b2ed938"),
  "url" : "https://www.apple.com/newsroom/2020/09/apple-marina-bay-sands-opens-thursday-in-singapore/",
  "meta_data" : {
    "title" : "Apple Marina Bay Sands Opens Thursday in Singapore",
    "desc" : "Apple’s most ambitious retail project sits on the waters of Marina Bay",
    "img_url" : "/content/dam/newsroom/images/environments/stores/apple_nso-marina-bay-sands_exterior_09072020_Full-Bleed-Image.jpg/_jcr_content/renditions/large.jpg",
    "votes" : 11
  }
}
```

4. ```relation3``` holds both ```relation1``` and ```relation2``` by storing their object IDs

```
{
  "_id" : ObjectId("5f573da85db73d3b8b2ed939"),
  "ID1" : ObjectId("5f573da75db73d3b8b2ed937"),
  "ID2" : ObjectId("5f573da85db73d3b8b2ed938")
}
```

