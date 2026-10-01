"""MIT-licensed original local demo. No live blockchain or credentials."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            body = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
            if not isinstance(body, dict) or body.get('jsonrpc') != '2.0' or not isinstance(body.get('method'), str):
                response = {'jsonrpc':'2.0','id':None,'error':{'code':-32600,'message':'Invalid Request'}}
            elif body['method'] == 'eth_chainId' and body.get('params') == []:
                response = {'jsonrpc':'2.0','id':body.get('id'),'result':'0x1'}
            elif body['method'] == 'eth_chainId':
                response = {'jsonrpc':'2.0','id':body.get('id'),'error':{'code':-32602,'message':'Invalid params'}}
            else:
                response = {'jsonrpc':'2.0','id':body.get('id'),'error':{'code':-32601,'message':'Method not found'}}
        except (ValueError, TypeError):
            response = {'jsonrpc':'2.0','id':None,'error':{'code':-32700,'message':'Parse error'}}
        encoded = json.dumps(response).encode()
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.send_header('Content-Length',str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
    def log_message(self, *args):
        pass

if __name__ == '__main__':
    HTTPServer(('127.0.0.1',8765),Handler).serve_forever()
