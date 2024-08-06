# basic syntax
# file = open('youtube.txt', 'w')

# try:
#     file.write('test')
# finally:
#     file.close()

# other syntax
# error handling is done internally, no need to explicitly define
# with open('youtube.txt', 'w') as file:
#     file.write('testing')

import json

# main is the entry point
def main():

    def loadData():
        try:
            with open('youtube.txt', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        finally:
            pass
    
    def saveData(videos):
        with open('youtube.txt', 'w') as file:
            json.dump(videos, file) # first parameter is data, second parameter is place where data need to be saved

    def listAllVideos(videos):
        # enumerate adds indexing to iterables
        print("\n")
        for (index, video) in enumerate(videos, start = 1): # start tells about start index
            print(f"{index} {video['name']}, Duration: {video['time']}")
        print("\n")

    def addVideo(videos):
        name = input("Enter video name: ")
        time = int(input("Enter video time: "))
        videos.append({'name': name},{'time': time})
        saveData(videos)

    def updateVideo(videos):
        listAllVideos(videos)
        index = int(input('Enter the video number to update:'))
        if 1<= index <= len(videos):
            name = input("Enter new name of the video: ")
            time = int(input("Enter new time of the video: "))
            videos[index-1] = {"name": {name}, "time": {time}}
            saveData(videos)
        else:
            print("Invalid index selected")

    def deleteVideo(videos):
        listAllVideos(videos)
        index = int(input('Enter the video number to delete:'))
        if 1<= index <= len(videos):
            del videos[index-1]
            saveData(videos)
        else:
            print("Invalid index selected")
    
    videos = loadData()

    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. update a youtube video')
        print('4. delete a favorite video')
        print('5. exit the app')
        choice = int(input('Enter your choice:'))

        match choice:
            case 1:
                listAllVideos(videos)
            case 2:
                addVideo(videos)
            case 3:
                updateVideo(videos)
            case 4:
                deleteVideo(videos)
            case 5:
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()