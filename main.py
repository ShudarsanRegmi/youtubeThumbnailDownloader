import requests
import time
videourl = input("Enter youtube vieo url: ")
wwwPosition = videourl.find("www")
comPosition = videourl.find(".com")
host = videourl[wwwPosition+4:comPosition]
if(host == "youtube"):
    qvPosition = videourl.find("=")
    videoId = videourl[qvPosition+1:]
    while True:
        choice = int(input("""1) Average Quality (recommended)
2) High Resolution
Choose an Option: """))
        if(choice == 1 or choice == 2 or choice == ""):
            if(choice ==2):
                newUrl = "https://i.ytimg.com/vi/"+videoId+"/hq720.jpg"
            else:
                newUrl = "https://i.ytimg.com/vi/"+videoId+"/hqdefault.jpg"
            break
    print(newUrl)
    imageRequest = requests.get(newUrl)
    responseImage = imageRequest.text
    # fileName = 
    with open(f"thumbnail{str(time.time())[7:]}.jpg","wb") as imagefile:
        imagefile.write(imageRequest.content)
else:
    print("Only YoutTube video thumbnail can be downloaded")
            