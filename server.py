import os
import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class YandexHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("https://ya.ru")
        self.write(response.body)


class GoogleHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("https://google.ru")
        self.write(response.body)


def make_app():
    debug = os.getenv('DEBUG')
    return tornado.web.Application([
        (r"/yandex", YandexHandler),
        (r"/google", GoogleHandler)
    ], debug=debug)


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    print("Server is listening in http://localhost:5000")
    tornado.ioloop.IOLoop.current().start()
