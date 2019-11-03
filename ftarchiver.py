# Copyright (c) 2018, Claus Wonnemann
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__author__ = 'chwon'

import requests
import lxml.html
import sys

workdir = './'
authgeturl = 'https://www.test.de/shopmodule/AboCheck/?cmslink=cms%3A%2F%2Fps4%2Fheftuebersicht2%2Ffinanztest%3A01%3A2018%2F%3Fpool%3Dshop&periodical=Finanztest&submit=true&number=ABONUMMER&zip=PLZ&city=STADT'
dlsitepattern = 'https://www.test.de/shop/finanztest-hefte/finanztest_MONTH_YEAR/?ft=download-2001'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4'
helpstr = 'Aufruf:\n\tftarchiver ABONUMMER PLZ STADT MM/YYYY MM/YYYY'


def do_auth():
    headers = {'User-Agent': userAgent}
    session = requests.session()
    session.get(authgeturl, headers=headers)
    return session


def download_issue(session, year, month):
    dlgeturl = dlsitepattern.replace('MONTH', month).replace('YEAR', year)
    headers = {'User-Agent': userAgent}
    dlpage = session.get(dlgeturl, headers=headers)

    dom = lxml.html.fromstring(dlpage.text)
    urls = dom.xpath('//div[@class="tango-download-box__content__download-item"]//a')

    print(month, year)

    dlurl = 'https://www.test.de' + urls[0].get('href')

    dldata = session.get(dlurl, headers=headers)
    savename = workdir + 'Finanztest_' + year + '-' + month + '.pdf'
    file = open(savename, 'wb')
    file.write(dldata.content)
    file.close()


if len(sys.argv) != 6:
    print(helpstr)
    exit(-1)
abonummer = sys.argv[1]
plz = sys.argv[2]
stadt = sys.argv[3]
monthfrom, yearfrom = sys.argv[4].split('/')
monthto, yearto = sys.argv[5].split('/')
authgeturl = authgeturl.replace('ABONUMMER', abonummer).replace('PLZ', plz).replace('STADT', stadt)
session = do_auth()
for year in range(int(yearfrom), int(yearto)+1):
    for month in range(int(monthfrom), int(monthto)+1):
        download_issue(session, str(year), str(month).zfill(2))
