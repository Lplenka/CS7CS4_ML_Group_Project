import requests
import argparse

def url_file_download(url):
	print(url)

	req = requests.get(url)
	url_content = req.content
	file_name = url.split('/')[-1].split('.')[0]
	csv_file = open(file_name + '.csv', 'wb')
	csv_file.write(url_content)
	csv_file.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="url for csv", type=str, required=False, default='ALERT')
    args = parser.parse_args()
    url_file_download(args.url)

if __name__ == '__main__':
	main()
