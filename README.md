# FTArchiver
Download pdf copies of German Finanztest magazine for your personal archive as a registered subscriber.


Usage: ftarchiver ABONUMMER PLZ STADT From:MM/YYYY To:MM/YYYY


ABONUMMER       Subscriber number

PLZ             Zip code

STADT           City

From:MM/YYYY    First copy to download

To:MM/YYYY      Last copy to download


Example: ftarchiver 0123456789 20095 Hamburg 01/2016 12/2017


Requires Python 3 and the lxml and Requests libraries.
