#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
import os
import logging
from uploadhandler import uploadhandler


class UploadForm(tornado.web.RequestHandler):
    def get(self):
        self.render("uploadform.html")


if __name__ == "__main__":
    define("debug", default=False, help="run in debug mode")
    define("port", default=2356, help="run server on given port", type=int)
    parse_command_line()
    application = tornado.web.Application(
        [
            (r"/", UploadForm),
            (r"/upload", uploadhandler.UploadHandler,
             dict(upload_path="/tmp/lal/", naming_strategy=None)),
        ],
        debug=True,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        cookie_secret="SOME_SECRET_GOES_HERE_MATE",
    )
    application.listen(options.port)
    logging.info("Server running on port %d", options.port)
    tornado.ioloop.IOLoop.instance().start()
