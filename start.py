import tornado.ioloop
import tornado.web
import tornado.options

tornado.options.define("port", default=9999, help="Run on the given port", type=int)

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("get test")

    def post(self):
        self.write("post test")
        self.write(self.request.body)

handlers = [
	(r'/', TestHandler),
]

if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = tornado.web.Application(handlers)
    app.listen(tornado.options.options.port)

    # # print 'Tornado has started at %s' % tornado.options.options.port
    tornado.ioloop.IOLoop.instance().start()