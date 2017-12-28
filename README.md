## Prettify JSON

Command-line tool to pretty-print JSON 

## Quickstart

Example of script launch on Linux, Python 3.5:
```bash
$ git clone https://github.com/globax89/4_json.git
$ cd 4_json
```

## How to use
```python
$ python3 pprint_json.py <path to json file>
```

## Sample

```python
$ python3 pprint_json.py sample.json
{
    "properties": {
        "age": {
            "description": "Age in years",
            "minimum": 0,
            "type": "integer"
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        }
    },
    "required": [
        "firstName",
        "lastName"
    ],
    "title": "Person",
    "type": "object"
}
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
