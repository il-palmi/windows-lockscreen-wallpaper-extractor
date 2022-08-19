import os
import shutil
from PIL import Image

MAXIMUM_IMAGES_NUMBER = 20


def main():
    user = os.getlogin()
    microsoftWallpaperFolder = f"C:/Users/{user}/AppData/Local/Packages/"
    outputFolder = f"C:/Users/{user}/Pictures/microsoftWallpapers"
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder, exist_ok=True)
    for folder in os.listdir(f"C:/Users/{user}/AppData/Local/Packages/"):
        if folder.startswith("Microsoft.Windows.ContentDeliveryManager"):
            microsoftWallpaperFolder += f"{folder}/LocalState/Assets/"

    if os.path.exists(microsoftWallpaperFolder):
        for file in os.listdir(microsoftWallpaperFolder):
            if os.path.isfile(f"{microsoftWallpaperFolder}/{file}"):
                image = Image.open(f"{microsoftWallpaperFolder}/{file}")
                if image.size == (1920, 1080):
                    shutil.copy(f"{microsoftWallpaperFolder}/{file}", f"{outputFolder}/{file}.png")

    # Auto remove excess files if number of images exceed MAXIMUM_IMAGES_NUMBER
    if len(os.listdir(outputFolder)) > MAXIMUM_IMAGES_NUMBER:
        files = {}
        for image in os.listdir(outputFolder):
            ctime = os.stat(f"{outputFolder}/{image}").st_ctime
            files[image] = ctime
        sort = sorted(files, key=files.get)
        for file in sort[MAXIMUM_IMAGES_NUMBER:]:
            os.remove(f"{outputFolder}/{file}")


if __name__ == '__main__':
    main()
