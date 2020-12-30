from pathlib import Path  # pathlib is seriously awesome!

data_dir = Path('/path/to/some/logical/parent/dir')
api_path = data_dir / 'my_api.py'  # use feather files if possible!!!

customer_db_url = 'sql:///customer/db/url'
purchases_db_url = 'sql:///purchases/db/url'