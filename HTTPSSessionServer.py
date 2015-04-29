#!/bin/env python3
# -*- coding: utf-8 -*-
from functools import partial

import http.server
import os
import ssl
import sys

import pki

if not hasattr(http.server, 'ThreadingHTTPSServer'):
    class ThreadingHTTPSServer(http.server.ThreadingHTTPServer):
        """
        HTTPServer Class, with its socket wrapped in TLS using ssl.wrap_socket
        """

        def __init__(self,
                     server_address: tuple,
                     request_handler: http.server.BaseHTTPRequestHandler,
                     bind_and_activate: bool = True,
                     certfile: str = None,
                     keyfile: str = None,
                     password: str = None,
                     alpn_protocols: list = None):
            super().__init__(server_address,
                             request_handler,
                             bind_and_activate)

            # Wrap Socket using TLS cert
            self.context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
            self.context.load_cert_chain(certfile)

            # Set supported ALPN protocols
            if not alpn_protocols:
                alpn_protocols = ['http/1.1']

            self.context.set_alpn_protocols(alpn_protocols)

            # enable PHA for TLS 1.3 connections if available
            if self.context.post_handshake_auth is not None:
                self.context.post_handshake_auth = True

            self.socket = self.context.wrap_socket(
                self.socket,
                server_side=True)

    setattr(http.server, 'ThreadingHTTPSServer', ThreadingHTTPSServer)


class EndpointHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,
                 request: http.server.socket,
                 client_address: tuple,
                 server: http.server.ThreadingHTTPSServer,
                 directory: str = None,
                 endpoints: dict = None):

        self.endpoints = endpoints
        super().__init__(request,
                         client_address,
                         server,
                         directory=directory)

    def do_GET(self):
        print(f"endpoint handler: {self.requestline}")
        print(f"endpoint handler: {self.path}")
        if self.path not in self.endpoints.keys():
            return super().do_GET()

        data = self.endpoints[self.path](self)
        self.send_response(http.server.HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data.encode('UTF-8'))

source_path = os.getcwd()
root_path = os.getcwd()

if len(sys.argv) > 1:
    source_path = os.path.abspath(sys.argv[1])

if len(sys.argv) > 2:
    root_path = os.path.abspath(sys.argv[2])

print("source_path", source_path)
print("root_path", root_path)

certfile_path = os.path.join(root_path, "server.pem")
pki.make_self_signed_ca(certfile_path)

host= ''
port = 8443
http_handler = partial(
    EndpointHTTPRequestHandler,
    directory=source_path,
    endpoints={
        '/api/v1/echo': lambda x: f'hello {x}'
    })

with http.server.ThreadingHTTPSServer(
        (host, port),
        http_handler,
        bind_and_activate=True,
        certfile=certfile_path,
        keyfile=None,
        password=None,
        alpn_protocols=None) as httpd:

    [h, p] = httpd.socket.getsockname()
    print(f"Serving HTTPS on {h} port {p} (https://{h}:{p}/) ...")
    print(f"Using TLS Cert: {certfile_path}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
