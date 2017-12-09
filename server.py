"""
Simple server to handle POST on localhost on optional port in Python and send email via Mailgun
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import smtpd
import asyncore
import threading
import smtplib

# Seems this won't actually work from a dynamic IP for most email hosts (they reject emails from those IPs)
# class SMTPServer(smtpd.SMTPServer):
#
#     def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
#         print('Receiving message from:', peer)
#         print('Message addressed from:', mailfrom)
#         print('Message addressed to  :', rcpttos)
#         print('Message length        :', len(data))


class Handler(BaseHTTPRequestHandler):

    # noinspection PyPep8Naming
    def do_POST(self):
        # TODO: this should be the request status code, but for some reason this doesn't seem to work at the end
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # data size
        post_body = self.rfile.read(content_length)
        self.wfile.write("Received post.".encode("utf-8"))

        # TODO: retrieve custom values from somewhere (db or config file), preferably managed via web page
        sender = "Repo Response <REPORESPONSE@DONOTREPLY.COM>"
        recipients = ['YOUR_EMAIL@EMAIL.COM']
        subject = 'webhook activated'
        #TODO: Customize the subject/body based on WebHook (through web interface?)
        body = post_body
        request = self.send_message(sender, recipients, subject, body)


    @staticmethod
    def send_message(sender, recipients, subject, body):
        return requests.post(
            "YOUR_MAILGUN_DOMAIN",
            auth=("api", "YOUR_MAILGUN_KEY"),
            data={"from": sender,
                  "to": recipients,
                  "subject": subject,
                  "text": body})


def run(server=HTTPServer, handler=Handler,  httpd_port=3000):
    # SMTPServer(('localhost', 25), None)
    # # this is a little automagical -  smtpd server will inject itself into the asyncore loop to be run
    # smtp_thread = threading.Thread(target=asyncore.loop, name="SMTP Server")
    # smtp_thread.start()s
    # print('Starting smtp server...')

    httpd_server_address = ('', httpd_port)
    httpd = server(httpd_server_address, handler)
    print('Starting httpd server...')
    httpd.serve_forever()




if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
