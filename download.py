import urllib.request


def download(url, saveas):
    urllib.request.urlretrieve(url, saveas)


if __name__ == '__main__':
    # download('https://hips.hearstapps.com/ghk.h-cdn.co/assets/16/08/gettyimages-464163411.jpg', 'dog.jpg')

    download('https://ichef.bbci.co.uk/news/976/cpsprodpb/12A9B/production/_111434467_gettyimages-1143489763.jpg', 'cat.jpg')
