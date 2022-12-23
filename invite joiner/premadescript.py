from selenium import webdriver
from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
PROXY = '109.238.222.5:40387'
options = Options()
options.headless = True
options.use_chromium = True
#options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Edge(executable_path = r'C:\Users\ka4ma\Documents\python3\info-alpha\msedgedriver.exe')
invite = input("Enter the invite link: ")
driver.get('https://discord.com/invite/' + invite[19:] + '/login')

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            js = '''function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 2500);
} 
login("'''+token+'''")'''
            driver.execute_script(js)
            while True:
                try:
                    driver.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                except:
                    break
            while True:
                try:
                    driver.find_element_by_class_name('marginTop40-i-78cZ.button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN').click()
                    break
                except:
                    'nothing'
            while True:
                try:
                    driver.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                    break
                except:
                    'nothing'
            print(token, "joined")
            driver.delete_all_cookies()
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
                alert = driver.switch_to.alert
                alert.dismiss()
                print("alert accepted")
            except TimeoutException:
                print("no alert")
print("ALL DONE!")
