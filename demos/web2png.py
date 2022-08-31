from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(executable_path = "/home/ajeep/py3env/chromedriver", options=chrome_options)

urls={
    "vim": "http://192.168.100.199:5050/sheet/630af884d5bb9b004200d300",
    "git": "http://192.168.100.199:5050/sheet/630b93cc87560f00121dabfb",
    "md0": "http://192.168.100.199:5050/sheet/630c246887560f00121dabfc",
    "md1": "http://192.168.100.199:5050/sheet/630c345287560f00121dabfd",
    "docker": "http://192.168.100.199:5050/sheet/630c4f1d87560f00121dabfe",
    "linux": "http://192.168.100.199:5050/sheet/630dd535d4c5240012356c46"
    }

for key,url in urls.items():
    driver.get(url)
    driver.set_window_size(2560,2560)
    time.sleep(2)
    ssfile="cheatsheet-{}.png".format(key)
    print(ssfile)
    driver.save_screenshot(ssfile)
    screenshot=Image.open(ssfile)   
    img=screenshot.crop((0,150,2400,2560))
    imageBox = img.getbbox()
    img = img.crop(imageBox)
    img.save(ssfile)
    os.system('convert {} -trim {}'.format(ssfile,ssfile))
    #screenshot.show()
