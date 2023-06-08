# XMLRPC

Followed [this spec](http://xmlrpc.com/spec.md) for the **XML-RPC** protocol integration.

I integrated some basic logic that was not part of the original assignment specification (such as if too many parameters were passed into the subtract function)

This runs on port `8080`

## Before - Install Requirements
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
```bash
python server.py


python client.py localhost 8080
```