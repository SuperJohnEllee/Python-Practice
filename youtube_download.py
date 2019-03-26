import pytube

video_link = input("Enter video url: ")
print("Downloading...")
yt = pytube.YouTube(video_link)
videos = yt.streams.first()
videos.download('C:/Users/HLL-User/Desktop/Youtube Vids')
print('Download Complete')
print('Title: ', yt.title)
print('Size: ', yt.length)