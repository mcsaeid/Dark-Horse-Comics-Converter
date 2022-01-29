import webbrowser

while True:
    old_url = input('\nEnter the book URL: ')

    uuid = old_url.split('/')[-1]

    new_url = fr"https://digital.darkhorse.com/api/v6/book/{uuid}"

    print('\nOpening the download page...')
    webbrowser.open(new_url)
