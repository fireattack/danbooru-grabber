#!/usr/bin/python
#coding:utf-8
import os # path manipulation
import urllib as urllib
import requests

status = 'not done yet'

# change this to your danbooru folder
# it might look something like this: '/users/YourUserName/DanbooruPics'
# make sure the folder already exists!
danbooru_folder = 'C:\\test\\'

# generate tag argument to be used in url and folder creation
def generate_tag_argv(tagList):
	tag_argv = ''
	for tag in tagList:
		tag_argv = tag_argv + tag + '+'
	tag_argv = tag_argv[:-1]

	return tag_argv

# request json, get urls of pictures and download them
def grabber(tag_argv,page_num):
	r = requests.get('https://danbooru.donmai.us/posts.json?tags='+tag_argv+'&page='+str(page_num))
	streams = r.json()
	# check if all pages have been visited
	if len(streams) == 0:
		print("All pictures have been downloaded!")
		global status
		status = 'done'
	else:
		# check if directory already exists
		if (os.path.exists(danbooru_folder+tag_argv) == False):
			os.mkdir(danbooru_folder+tag_argv)

	#	url = []
		target = []
		for post in streams:
			if 'file_url' in post:
				target.append('https://danbooru.donmai.us'+post['file_url'])

		# download
		for address in target:
			print(address)
		#	urllib.urlretrieve(address,danbooru_folder+tag_argv+'/'+address.split('/')[-1])



def main():
	#page_num = input('Enter the number of pages you want to download. To download all, simply enter a super large number:')
	#taginput = input('Enter tags,separated by space:')
	page_num = 1
	taginput = 'ahegao stocking futanari'
	n = 1
	while n <= int(page_num) and status == 'not done yet':
		tagList = taginput.split(' ')
		tag_argv = generate_tag_argv(tagList)
		grabber(tag_argv,n)
		n = n + 1

	print('Download successful!')
	u2 = 'どうぞ、召し上がってください！'
	print(u2)


if __name__ == '__main__':
	main()
