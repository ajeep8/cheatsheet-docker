
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os

chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
# 

driver = webdriver.Chrome(executable_path = "/home/ajeep/py3env/chromedriver_linux64_105.0.5195.52", options=chrome_options)

'''
'''
urls={
    "vim": "http://192.168.100.199:5050/sheet/630af884d5bb9b004200d300",
    "git": "http://192.168.100.199:5050/sheet/630b93cc87560f00121dabfb",
    "md0": "http://192.168.100.199:5050/sheet/630c246887560f00121dabfc",
    "md1": "http://192.168.100.199:5050/sheet/630c345287560f00121dabfd",
    "docker": "http://192.168.100.199:5050/sheet/630c4f1d87560f00121dabfe",
    "linux": "http://192.168.100.199:5050/sheet/630dd535d4c5240012356c46",
    "word": "http://192.168.100.199:5050/sheet/632d60575c31a600181e2fc8",
    }

driver.set_window_size(2560,2560)
for key,url in urls.items():
    driver.get(url)
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
