from urllib import request
import lxml.html


def main(url):
    req = request.urlopen(url)
    html = lxml.html.fromstring(req.read())
    title = html.xpath('.//meta[@property="og:title"]/@content')[0]
    description = html.xpath('.//meta[@property="og:description"]/@content')[0]
    site_name = html.xpath('.//meta[@property="og:site_name"]/@content')[0]
    image = html.xpath('.//meta[@property="og:image"]/@content')[0]
    return {
        'title': title,
        'description': description,
        'site_name': site_name,
        'image': image,
    }
