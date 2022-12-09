from bs4 import BeautifulSoup as bs
import requests
import webbrowser
src = requests.get('https://gogoanime.gs').text
soup = bs(src, 'lxml')

container = soup.find('section', id='recent-update')
links = []
index = 0
for anime in container.find_all('div', class_='item'):
    index += 1
    title = anime.find('a', class_='name d-title')
    name = title.text

    link = f'''https://gogoanime.gs{str(title).split('"')[5]}'''
    links.append(link)

    subs = anime.find('span', class_='ep-status sub').text
    try:
        dubs = anime.find('span', class_='ep-status dub').text
    except AttributeError:
        dubs = 0

    print(f'{index}: {name}')
    print(f'   Subs: {subs}     Dubs: {dubs}\n')
    
while True:
    question = input('Would you like to watch an anime? <y/n>')
    if question == 'y':
        try:
            num = int(input('Watch anime number:  >'))
        except ValueError:
            print('Must be a number')
            continue
        if num not in range(1, index +1):
            print('Invalid index')
            continue
        webbrowser.open(links[num-1])
        break
    elif question == 'n':
        break
    else:
        print('Invalid option \n')
        continue

exit()
