#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import zipfile
from io import BytesIO
import os 
import argparse
def main(args):
    # get_url = 'http://localhost:8000/test.zip'
    get_url = args.input_url
    # post_url = 'http://localhost:7777'
    post_url = args.yoinked_url
# Send a GET request to the API

    r = requests.get(get_url)
    z = zipfile.ZipFile(BytesIO(r.content))
    z.extractall('/var/yoink/incoming/')
    # z.extractall('/Users/colehunter/Desktop/veg')
    # Create the outgoing directory at /var/yoink/outgoing

    os.makedirs('/var/yoink/outoing/', exist_ok=True)
    # os.makedirs('/Users/colehunter/Desktop/veg/new', exist_ok=True)
    # If succesfully unzipped file, send an empty post request to the API
    if r.status_code == 200:
        r = requests.post(post_url, data={})
        print(r.status_code)
    






if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for yoink')

    parser.add_argument('input_url')
    parser.add_argument('yoinked_url')
    args = parser.parse_args()

    main(args)