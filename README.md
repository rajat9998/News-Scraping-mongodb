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

## Running the Spiders

We can run a spider using the ```scrapy crawl``` command as:

```
$ cd News
$ scrapy crawl news
```

## Maintaining relational meta-data

We can maintain two relation- one with the url and heading of the blog and other one with url and its meta-data like (Description, Image, Title, Votes)

```
$ cd News
$ python news_relation.py
```
Note: We need to crawl first in order to obtain scrapped data.
