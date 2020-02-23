import json, os, wget
from urllib2 import urlopen

linux_url = 'https://public-cdn.cloud.unity3d.com/hub/prod/releases-linux.json'
windows_url = 'https://public-cdn.cloud.unity3d.com/hub/prod/releases-win32.json'
mac_url = 'https://public-cdn.cloud.unity3d.com/hub/prod/releases-darwin.json'
dest_folder = './Unity Versions/'

def download_version(osversion, url):
    downloaded_data = urlopen(url)
    downloaded_json = json.loads(downloaded_data.read().decode('utf-8'))

    for channel in downloaded_json:
        for item in downloaded_json[channel]:
            url = item['downloadUrl']
            versionfolder = dest_folder + 'Release ' + item['version'] + '/' + osversion
            editorfilepath = versionfolder + '/' + os.path.basename(url)

            if not os.path.exists(versionfolder):
                os.makedirs(versionfolder)

            print('downloading ' + os.path.basename(url) + ' from ' + url)

            try:
                wget.download(url, editorfilepath)
            except:
                print('failed downloading ' + editorfilepath)

            for module in item['modules']:
                url = module['downloadUrl']
                filepath = versionfolder + '/' + os.path.basename(url)
                print(filepath)
                if os.path.exists(filepath):
                    print(filepath + ' exists! continuing')
                    continue

                print('downloading ' + os.path.basename(url) + ' from ' + url)

                try:
                    wget.download(url, filepath)
                except:
                    print('failed downloading ' + editorfilepath)

download_version('Linux', linux_url)
download_version('Windows', windows_url)
download_version('Mac', mac_url)