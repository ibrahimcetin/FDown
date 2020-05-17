import os

import requests
from tqdm import tqdm
from huepy import *


class FDown():
    def __init__(self):
        self.error_message = "Something Went Wrong!"
    def getResponse(self):
        try:
            return requests.get(self.url, stream=True)

        except requests.exceptions.ConnectionError:
            self.error_message = "Please, Check your Internet Connection or URL!"
            return False

        except:
            self.error_message = "Something Went Wrong!"
            return False

    def getTotalSize(self):
        return self.response.headers.get('content-length')

    def getRemainingSize(self):
        with open(self.file_path + self.file_name, "ab") as file:
            pos = file.tell()

        if pos == int(self.total_size):
            self.error_message = "File Already Downloaded!"
            return False

        elif pos:
            headers = {'Range': f'bytes={pos}-'}

            self.response = requests.get(self.url, headers=headers, stream=True)
            return self.response.headers.get('content-length')

        else:
            os.remove(self.file_path + self.file_name)
            return self.total_size

    def confirmDownload(self):
        if self.total_size == None and self.remaining_size == False:
            return

        else:
            print(info("Total file size : {} MB, Remaining file size : {} MB".format("%.1f" % (((int(self.total_size)//1024)/1024)), "%.1f" % ((int(self.remaining_size)//1024)/1024))))
            choose = input(que("Do you want to continue? [Y/n] "))

            return (True if choose.lower() == "y" else False)

    def download(self, url, file_name=None, file_path=None, confirm_download=False):
        self.url = url
        self.file_name = file_name.strip() if file_name else url.split("/")[-1]
        if file_path and (not file_path.isspace()):
            self.file_path = file_path.strip()
            if self.file_path[-1] != "/": self.file_path += "/"
        else:
            self.file_path = ""

        self.response = self.getResponse()
        self.total_size = self.getTotalSize() if self.response else False
        self.remaining_size = self.getRemainingSize() if self.total_size != False else False

        if confirm_download and self.total_size and self.remaining_size:
            self.confirm = self.confirmDownload()

            if not self.confirm: self.error_message = "Download Cancelled by User!"

        else:
            self.confirm = True

        if self.confirm and self.remaining_size:
            print(run(green("Download Starting..")))

            try:
                with open(self.file_path + self.file_name, "ab") as file:
                    for data in tqdm(iterable=self.response.iter_content(chunk_size=1024), total=int(self.remaining_size)//1024, unit='KB', ascii=True, desc=self.file_name):
                        file.write(data)

                print(good(green("File Successfully Downloaded")))

            except (requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectionError):
                print(bad(red("No Network Connection!")))

            except KeyboardInterrupt: # Ctrl + C
                print(info(red("Download Cancelled by User!")))

        elif self.confirm and self.total_size == None:
            print(info(green("This URL hasn't File Size! Download Starting..")))

            try:
                with open(self.file_path + self.file_name, "wb") as file:
                    for data in tqdm(iterable=self.response.iter_content(chunk_size=1024), unit='KB', ascii=True, desc=self.file_name):
                        file.write(data)

                print(good(green("File Successfully Downloaded")))

            except (requests.exceptions.ChunkedEncodingError, requests.exceptions.ConnectionError):
                print(bad(red("No Network Connection!")))

            except KeyboardInterrupt: # Ctrl + C
                print(info(red("Download Cancelled by User!")))

            except:
                print(bad(red("Something Went Wrong!")))

        else:
            print(bad(red(self.error_message)))


if __name__ == "__main__":
    fdown = FDown()

    url = "http://www.ovh.net/files/10Mio.dat"
    fdown.download(url=url, confirm_download=True)

