# Dark Horse Comics Converter
This script, written in Python, helps you download and convert your Dark Horse comics to a CBZ format. It was originally published [here](https://github.com/GrowAsguard/Dark-Horse-Comics-Converter). This repository is a slightly modified and improved version of the same scripts.

The scripts use the following python modules: *os, json, tarfile, zipfile, shutil, requests, time, googlesearch, bs4, webbrowser*. Please make sure that you have all of them installed on your system.

# Disclaimer

THIS SCRIPT IS NOT MEANT TO PROMOTE OR FACILITATE PIRACY BUT RATHER TO BE A LEARNING TOOL AND TO BACKUP YOUR OWNED COMICS FOR PERSONAL USAGE. PLEASE MAKE SURE WHETHER THIS IS LEGAL IN YOUR COUNTRY OR NOT.

# How to use

1) Open your browser and log into your account using the following link: https://digital.darkhorse.com/accounts/login.
2) Search and open the book you want to download. **Remember, this will only work for books that you *own* and nothing else.** Your purchased books will be located here: https://digital.darkhorse.com/accounts/manage/order_history.
3) Click on “READ NOW” and then copy the page URL. It will look something like this: https://digital.darkhorse.com/read/6da55e3e05a349629fda0aae6849602d.
4) Download or clone this repository to your computer.
5) Double-click on “url.py” and paste the URL that you copied in step three. This will open the download page and start downloading your book as “book.tar.”
6) Double-click on "script.py" and enter the path of the book you just downloaded **without quotes**!

The script will now do the following steps automatically:\
i) Extract the tar file;\
ii) Rename and convert the files to JPG images in the correct order;\
iii) Zip them into a CBZ file;\
iv) Get the book title and rename the CBZ file.

7) Finish. 

You will find the CBZ file in the same folder where you downloaded the “book.tar.” You can now safely delete the tar file if you like.

# FAQ
**Question:** I don’t have the googlesearch module. How do I install it?\
**Answer:** Find it here: https://pypi.org/project/googlesearch-python.

**Question:** The script was not able to fetch the book title at the end. Why is that, and what do I do next?\
**Answer:** If a `429 Too Many Requests` error is encountered—which, as the name implies, means that Google received too many requests in a given amount of time—the book UUID will be displayed. You can use it to google, find the name yourself, and rename the CBZ file manually. Of course, if you do have the name on hand, there is no need to google.

**Question:** WEB-DL, WEBRip, or Scan?\
**Answer**: The CBZ file produced by this script is a WEB-DL, not WEBRip or Scan.

**Question:** Why are the downloaded comics smaller in size than those uploaded by Empire, Son of Ultron, or someone similar?\
**Answer:** This is a mid-quality WEB-DL by Dark Horse Digital themselves. The comics uploaded by Empire, for example, are *not* WEB-DL but, in fact, print scans of the comics. The scanned comics often come in much higher quality and resolution *because* they are high-quality print scans.
