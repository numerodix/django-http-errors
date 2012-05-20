class Http302(Exception):
    def __init__(self, url):
        self.url = url
