# Dark Horse Comics Converter
These scripts, written in Python, help you download and convert your Dark Horse digital comics and books to a CBZ format for offline use. They were originally published [here](https://github.com/GrowAsguard/Dark-Horse-Comics-Converter). This repository is a slightly modified and improved version of the same code. From here on, any comic or book is simply referred to as _books_.

The scripts use the following Python modules: _os_, _json_, _tarfile_, _zipfile_, _shutil_, _requests_, _time_, _googlesearch_, _bs4_, _webbrowser_. Please make sure you have all of them installed on your system.

<br>

**Table of contents**
* [Disclaimer](https://github.com/mcsaeid/Dark-Horse-Comics-Converter#disclaimer)
* [How to use](https://github.com/mcsaeid/Dark-Horse-Comics-Converter#how-to-use)
* [FAQ](https://github.com/mcsaeid/Dark-Horse-Comics-Converter#faq)

# Disclaimer
These scripts are not meant to promote or facilitate piracy but rather to be a learning tool and a means to backup your owned books for personal usage. Please ensure whether or not this is legal in your country.

# How to use
1) Open your browser and log into your account using this link: https://digital.darkhorse.com/accounts/login.
2) Navigate to Purchase History either by going to your account or using the link provided. Next, search and open the book you wish to download. **Remember, this will only work for books that you *own*—nothing else.** You can view your purchased books here: https://digital.darkhorse.com/accounts/manage/order_history.
3) After opening the book, click on “READ NOW” and then copy the page URL from the address bar in your browser. It will look something like this: `https://digital.darkhorse.com/read/6da55e3e05a349629fda0aae6849602d`.
4) Download or clone this repository to your computer.
5) Run or double-click on **url.py** and paste the URL that you copied in step three. This will open a download page in your browser, and you will be prompted to download your book as **book.tar**.
6) Run or double-click on **script.py** and enter the path of the file you just downloaded **without quotes**.

The script will now perform the following actions automatically:\
i) Extract the tar file;\
ii) Rename and convert the files to JPG images in the correct order;\
iii) Zip them into a CBZ file;\
iv) Get the book title and rename the CBZ file accordingly.

7) Finish. 

You will find the CBZ file in the same folder where you downloaded the book. You can now safely discard the tar file if you like.

# FAQ
**Question:** I don’t have the _googlesearch_ module. How do I install it?\
**Answer:** You can find it here: https://pypi.org/project/googlesearch-python.

**Question:** The script was unable to get the book title at the end. What is a book page URL, and where do I find it?\
**Answer:** Your book page URL will look something like this: https://digital.darkhorse.com/books/5baf9f8140344ca1879a74669e3abd42/world-of-the-witcher-hc. Simply go to the Dark Horse Digital Comics website, find and open the book (as explained above in step two), copy the URL, and paste it in the terminal.

**Question:** Why does the script fail to get the book title?\
**Answer:** That is when a `429 Too Many Requests` error has occured, which, as the name implies, means that Google received too many requests in a given amount of time. By entering the book page URL manually, the script is able to continue fetching the title, renaming the CBZ file, and thus finishing the operation.

**Question:** WEB-DL, WEBRip, or scan?\
**Answer**: The CBZ file produced by this script is a WEB-DL, not WEBRip or scan.

**Question:** Why are the downloaded books smaller in size and dimension than those uploaded by Empire, Son of Ultron, or someone similar?\
**Answer:** This is a mid-quality WEB-DL by Dark Horse Digital Comics themselves. The books uploaded by Empire, for example, are _not_ WEB-DL but, in fact, print scans of the books. The scanned books often come in much higher quality and resolution _because_ they are high-quality print scans.
