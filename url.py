import webbrowser

while True:
    old_url = input('Enter the book URL: ')

    uuid = old_url.split('/')[-1]

    new_url = fr"https://digital.darkhorse.com/api/v6/book/{uuid}"

    print('Opening the download address...')
    webbrowser.open(new_url)
