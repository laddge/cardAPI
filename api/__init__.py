from urllib import request
import lxml.html


def main(url):
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = lxml.html.fromstring(request.urlopen(req).read())
    except Exception as e:
        print(e)
        return {}
    title = (
        html.xpath('.//meta[@property="og:title"]/@content')[-1]
        if html.xpath('.//meta[@property="og:title"]/@content')
        else ''
    )
    description = (
        html.xpath('.//meta[@property="og:description"]/@content')[-1]
        if html.xpath('.//meta[@property="og:description"]/@content')
        else ''
    )
    site_name = (
        html.xpath('.//meta[@property="og:site_name"]/@content')[-1]
        if html.xpath('.//meta[@property="og:site_name"]/@content')
        else ''
    )
    image = (
        html.xpath('.//meta[@property="og:image"]/@content')[-1]
        if html.xpath('.//meta[@property="og:image"]/@content')
        else ''
    )
    return {
        "title": title,
        "description": description,
        "site_name": site_name,
        "image": image,
    }
