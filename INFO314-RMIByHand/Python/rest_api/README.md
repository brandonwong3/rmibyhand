# REST API Reference


> I hope that you can please accept this extra credit portion. I am only a few points off from passing this last course I need to graduate. Thanks.

Sample payload properties:
```json
{
  "operation": "add",
  "operands": [1, 2],
  "error": "Invalid operation",
  "value": 3
}
```

This runs on port `5000`

Error Codes:
- 200 - OK
- 400 - Bad Request
- 404 - Not Found
- 500 - Internal Server Error

## Before - Install Requirements
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running
```bash
python server.py


python client.py localhost 5000
```