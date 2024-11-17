## apitest.py

The `apitest.py` file is a Python script that is used for testing Monzo account APIs. It requests the balance from the account and prints it.
Also includes a Dart version which achieves the same outcome.

### Python Usage

To use the `apitest.py` script, follow these steps:

1. Import required modules:

    ```python
    import requests
    import json
    ```

2. Insert monzo account access token:

    ```python
    access_token = ''
    ```

### Additional Notes

- Make sure to install the `requests` module.
- Access token can be found via: https://developers.monzo.com/api/playground
- More infomation at docs.monzo.com
