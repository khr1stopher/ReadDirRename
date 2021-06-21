import os
import glob
import sys

class app:

    pathActual = os.getcwd()
    textReplaced = sys.argv[1]
    replacedText = sys.argv[2]
    folder = ''
    files = []

    def __init__(self):
        self.lecturaFolder()
        self.renameFiles()

    def lecturaFolder(self):
        if(":" in sys.argv[3]):
            self.folderPath = glob.glob(sys.argv[3])
            self.folder = sys.argv[3][:-1]
            for item in self.folderPath:
                self.files.append(item)
        else:
            self.folder = sys.argv[3][:-1]
            self.folderPath = glob.glob(self.pathActual + "\\" + self.folder + "*")
            for item in self.folderPath:
                self.files.append(item)

    def renameFiles(self):
        for i in self.files:
            os.rename(i, i.replace(self.textReplaced, self.textReplaced))
        os.rename(self.folder, self.folder.replace(self.textReplaced, self.replacedText))


app()