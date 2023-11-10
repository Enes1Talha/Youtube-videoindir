import pytube

url = input("video linkini giriniz: ")

path = " "

pytube.YouTube(url).streams.get_highest_resolution().download()