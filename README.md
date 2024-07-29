# VTEXPY
[![PyPI Version](https://img.shields.io/pypi/v/vtexpy.svg)](https://pypi.python.org/pypi/vtexpy)

## Unofficial Python SDK for VTEX API

This is an unofficial Python SDK designed to facilitate integration with the VTEX API.

### Features

- Easy to use Python interface for calling endpoints on the VTEX API.

### Getting Started

#### Requirements

- Python >= 3.9, <3.13
- httpx >= 0.26, <1.0
- tenacity >= 8.3, <9.0

#### Installation

```bash
pip install vtexpy
```

#### Usage

```python
from vtex import VTEX


vtex_client = VTEX(account_name="<ACCOUNT_NAME>", app_key="APP_KEY", app_token="<APP_TOKEN>")
carrier_list_response = vtex_client.logistics.list_carriers(page=1, page_size=100)
```
