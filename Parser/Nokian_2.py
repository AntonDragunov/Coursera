import shutil
import urllib.parse
import urllib.request
import os

urls = {
    'just_filename': 'https://github.com/bits4waves/100daysofpractice-dataset/raw/master/requirements.txt',
    'filename_with_params': 'https://github.com/bits4waves/resonometer/blob/master/sound/violin-A-pluck.wav?raw=true',
    'no_filename': 'https://egate.nokiantyres.com/wholesale-ru/ru/my-account/report.xls',
}

for url in urls.values():
    with urllib.request.urlopen(url) as response:
        parsed_url_path = urllib.parse.urlparse(response.url).path
        filename = os.path.basename(parsed_url_path)
        with open(filename, 'w+b') as f:
            shutil.copyfileobj(response, f)