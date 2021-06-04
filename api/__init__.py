from urllib import request
from urllib.parse import urljoin
import lxml.html


def main(url):
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = lxml.html.fromstring(request.urlopen(req).read())
    except Exception as e:
        print(e)
        return {}

    if html.xpath('.//meta[@property="og:title"]/@content'):
        title = html.xpath('.//meta[@property="og:title"]/@content')[-1]
    elif html.xpath('.//meta[@property="twitter:title"]/@content'):
        title = html.xpath('.//meta[@property="twitter:title"]/@content')[-1]
    elif html.xpath('.//title/text()'):
        title = html.xpath('.//title/text()')[0]
    else:
        title = ''

    if html.xpath('.//meta[@property="og:description"]/@content'):
        description = html.xpath('.//meta[@property="og:description"]/@content')[-1]
    elif html.xpath('.//meta[@property="twitter:description"]/@content'):
        description = html.xpath('.//meta[@property="twitter:description"]/@content')[-1]
    elif html.xpath('.//meta[@name="description"]/@content'):
        description = html.xpath('.//meta[@name="description"]/@content')[0]
    else:
        description = ''

    if html.xpath('.//meta[@property="og:site_name"]/@content'):
        site_name = html.xpath('.//meta[@property="og:site_name"]/@content')[-1]
    else:
        site_name = ''

    if html.xpath('.//meta[@property="og:image"]/@content'):
        image = html.xpath('.//meta[@property="og:image"]/@content')[-1]
    elif html.xpath('.//meta[@property="twitter:image"]/@content'):
        image = html.xpath('.//meta[@property="twitter:image"]/@content')[-1]
    elif html.xpath('.//link[@rel="apple-touch-icon" or @rel="icon"]/@sizes'):
        size = max(html.xpath('.//link[@rel="apple-touch-icon" or @rel="icon"]/@sizes'))
        image = html.xpath(
            './/link[(@rel="apple-touch-icon" or @rel="icon") and @sizes='
            + size
            + ']/@href'
        )[0]
    elif html.xpath('.//link[@rel="shortcut icon"]/@href'):
        image = html.xpath('.//link[@rel="shortcut icon"]/@href')[0]
    else:
        image = ''

    if any([title, description, site_name, image]):
        return {
            "title": title,
            "description": description,
            "site_name": site_name,
            "image": urljoin(url, image),
        }
    else:
        return {}
