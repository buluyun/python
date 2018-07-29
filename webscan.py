#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 10:36:51
# @Author  : buluyun
# @Link    : http://buluyun.tech

import hackhttp
from  optparse import OptionParser
import os 
import sys 
import threading,Queue
from colorama import init, Fore, Back, Style
import time

def get_url():
	usage="Usage:%prog -u <weburl> -f <dict_filename>"
	parser=OptionParser(usage)
	parser.add_option("-u",type="string",dest="Url",help="example: http://www.xxx.com or www.xxx.com")
	parser.add_option("-f",type="string",dest="File",help="dict_filename")
	(options,args)=parser.parse_args()
 	if (options.Url==None and options.Url==None ):
 		#print "please input you weburl"
 		print "\033[1;31;40m"+u"好玩吗？呵呵...不输入URL和字典的文件名"
 		sys.exit()
 	if (options.File==None):
 		#print "please input you weburl"
 		print "\033[1;31;40m"+u"好玩吗？呵呵...不输入字典的文件名"
 		sys.exit()
 	else:
 		if "http://" not in options.Url:
 			url="http://"+options.Url
 		else:
 			url=options.Url
 			filename=options.File
 	webdict=[]
	with open(filename) as file: 		
		while True:
			dirdic=file.readline().strip()
			if (len(dirdic) == 0):break   
 			webdict.append(url + dirdic)
 	return webdict
 	

class run_begin(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue=queue
	
	def run(self):
		while True:
			if self._queue.empty():
				break
			try:
				urls=self._queue.get()
				http=hackhttp.hackhttp()
				code,head,html,redirect_url,log=http.http(urls)
				if(code==200):
					print   u" Biu biu biu ▄︻┻┳══━一 "+"\033[1;31;40m"+urls
					#print urls
					# with open('exists_url.txt','w') as f:
					# 	f.write(urls+"\n")

					with open('result.html','a+' ) as f:
						f.write('<a href="' + urls + '" target="_blank">' + urls + '</a>')
						f.write('\r\n</br>')
						
			except:
				print "error"
	

def main():
	print '''
	 ____  _      ____                  
	|  _ \(_)_ __/ ___|  ___ __ _ _ __  
	| | | | | '__\___ \ / __/ _` | '_ \ 
	| |_| | | |   ___) | (_| (_| | | | |
	|____/|_|_|  |____/ \___\__,_|_| |_|
	author:buluyun
	'''

	init(autoreset = True)
	file="result.html"
	dicts=get_url()
	threads=[]
	queue=Queue.Queue()
	for i in dicts:
	 	queue.put(i)
	for i in xrange(len(dicts)):
	 	threads.append(run_begin(queue))
	for t in threads:
	 	t.start()
	for t in threads:
	 	t.join()
	






			
if __name__=='__main__':
	start=time.time()
	main()
	end=time.time()
	print (str(end-start)+u"秒")
	
