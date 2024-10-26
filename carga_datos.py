import gdown

def download_folder_from_drive(output_path="."):
    url = 'https://drive.google.com/drive/folders/1xjkuCdlnRkWMOrdbZ-i49K_oWMP8TP8Y'
    gdown.download_folder(url, output=output_path, quiet=False, use_cookies=False)

download_folder_from_drive("data")


