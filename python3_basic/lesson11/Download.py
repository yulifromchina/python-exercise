#!/usr/bin/env python3

import os
import os.path
import requests

def DownLoad(url):
	req = requests.get(url)
	if req.status_code==404:
		print("No such file found in {}".format(url))
		return

	file_name = url.split('/')[-1]
	with open(file_name, 'wb') as fobj:
		fobj.write(req.content)
	print("Download over.")


if __name__ == "__main__":
	url = input("Enter a URL:")
	DownLoad(url)
