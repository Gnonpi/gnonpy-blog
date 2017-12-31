---
title: "Scraping Imdb - scraping"
date: 2017-09-16T23:13:43+02:00
draft: true
disable_comments: false
categories: ["python"]
---
[//TODO]: <> (Time the scraping function and how many pages in IMDB)
[//TODO]: <> (Time the different parts of the program)

<img src="/blog/01-imdb-scraping/01-imdb-logo-resize.png" width="480" height="224" />

# Scraping IMDB

Hello dear reader,
so with this first article I want to start
a series of posts about playing with IMDB.

I don't know yet what will be the final application,
how many posts it will take
or how frequent the posts will be
but we'll go one step at a time.

## Ok, but what is IMDB ? And what scraping means ?

[IMDB](http://www.imdb.com/) is the Internet Movie DataBase,
an online database with info related to movies, television shows, actors.
It's been bought by _Amazon_ in 1998.
It contains more than 4.5 million titles
and 8.1 million personalities.

Scraping is the action of extracting informations from a website.
That is possible because your browser render HTML code,
so if you can see the information, that mean it's somewhere in the HTML and that you can get.
Scraping is useful when you want to gather data without having access to a database.

## Why would you want to scrape IMDB ?

I know IMDB data is available on Amazon S3,
but maybe you're like me and don't want to create an Amazon account,
giving your credit card number and having to create a script to have access to the data.

There exist exist some libraries and project that aim to get around
but since there are some limits to the number of titles you can get.
Since we want to build a dataset,
we cannot use them.

Plus, scraping is not really complicated and
I think it's a good skill to have.

## So, how do we do this ?

**Code** : the code used is avaiable at [my Github](https://github.com/Gnonpi).

Well, I want to show you 2 things in this post :

* how to scrape a website using [*BeautifulSoup*](https://www.crummy.com/software/BeautifulSoup/),
    a Python library to do scraping that I find particully cool.
* how to launch the scraping __asynchronously__ with the **async**/**await**
    introduced in Python 3.6
Although these features are tough to comprehend and apply in your code,
I'm sure they can improve your daily programming life.

Without further do, let's start!

## Scraping one IMDB title

![GodFather Example](/blog/01-imdb-scraping/01-godfather-example.png)

So let's write our first piece of code to scrape a page.

{{< highlight python >}}
import requests
from bs4 import BeautifulSoup

URL_GODFATHER = 'http://www.imdb.com/title/tt0068646/'

# Using request.get to obtain the html code
html = requests.get(URL_GODFATHER).content
# Creating a BeautifulSoup object that parsed the html
soup = BeautifulSoup(html, 'html.parser')
# Accessing one element from the soup object
title = soup.find('h1', {'itemprop': 'name'}).text
print(title)
{{< /highlight >}}

What we did here was first downloading the HTML of the webpage using [Request](http://docs.python-requests.org/en/master/)
Then, we create a __BeautifulSoup__ object that has parsed the HTML content
so that we can access the HTML element easily.
Using the Code Inspector of your browser,
you can find the place where your data is.
In this snippet, I'm accessing the `div` tag
with the property `class` equal to `originalTitle`.
That means that there is a line in the HTML code that goes :
{{< highlight html >}}
<h1 class="" itemprop="name">The Godfather</h1>
{{< /highlight >}}

Why the `.text` ?
It's because with `soup` you can access all the fields of a tag :
`class`, `id`, `href`, or directly, the text.

Ok that's nice, but it has 2 problems :

* first, you have to go once though the HTML code and
    find the right combinations of tag and attributes to get your data.
    It's fast with 1 or 2 fields,
    but start to get long when you want 10 or 11 piece of information.
* second, one have to take care that the data can change between
    the pages of a website.
    In our case, I'm thinking about cases where data is missing
    (it happen a lot with old movie pages).

{{< highlight python >}}
import requests
from bs4 import BeautifulSoup

URL_GODFATHER = 'http://www.imdb.com/title/tt0068646/'

def get_soup_from_url(url)
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scrape_movie_title(soup_html):
    result = {}
    result['title'] = soup.find('h1', {'itemprop': 'name'}).text
    return result

if __name__ == "__main__":
    soup = get_soup_from_url(URL_GODFATHER)
    result_godfather = scrape_movie_title(soup)
    print(result_godfather)
{{< /highlight >}}

## Going one step further

Let's say that now you have your scraping function,
you can apply it on one page to get all the infos you need.

If the website has a lot of pages,
you are probably going to apply it to each page,
one by one.
That's going to be long. Very long.
If I tried to apply this to IMDB,
my python function takes *xxx* ms
and I want to scrape *yyy* pages,
that's *zzz* minutes to get all the data I need.

One technic to go faster is to use asynchronous request.
But why, what are the reasons behind this choice ?

* Scraping can be parallelized easily :
    even with thousands of pages, you always do the same things
    that are all independants from one page to another
    (downloading the page, parsing it, getting the right elements, returning the results)
* Downloading ressources work very well with asynchronous :
    the time to download a page is long compared to parsing it,
    and is very variable
    (because of your connection, because there is a pike of activity, who knows?).

**Warning :** don't be a jerk when scraping.
Use `time.sleep` to slow down your requests
and limit the number of workers.
If you are a jerk,
you're risking to DDOS the site you want to scrape
and to prevent this, the site will block your IP address.
