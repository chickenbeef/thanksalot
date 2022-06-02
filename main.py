import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
ua = UserAgent()

if __name__ == '__main__':
    file = open("info.txt", "r")
    fdata = file.readlines()
    countfile = open("counter.txt", "r")
    counter = int(countfile.read().strip())
    countfile.close()
    fname = fdata[0].split("::")[1].strip()
    lname = fdata[1].split("::")[1].strip()
    password = fdata[4].split("::")[1].strip()
    phone = fdata[5].split("::")[1].strip()
    ticker = fdata[6].split("::")[1].strip()
    while True:
        try:
            email = fdata[2].split("::")[1].strip() + str(counter)+"@" + fdata[3].split("::")[1].strip()
            user_agent = ua.random
            options=webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--log-level=3")
            options.add_argument('--disable-gpu')
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument(f'user-agent={user_agent}')
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            driver.get("https://secure.takealot.com/account/register")
            time.sleep(0.1)
            print("------------- Account Registration Started ----------------")
            print("Website Loaded Successfully")
            driver.find_element(by=By.XPATH, value="""(//label[text()='First Name']/following::input)[1]""").send_keys(
                fname)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//label[text()='Last Name']/following::input)[1]""").send_keys(
                lname)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//input[@class='email-mask'])[1]""").send_keys(email)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//input[@class='email-mask'])[2]""").send_keys(email)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//label[text()='Password']/following::input)[1]""").send_keys(
                password)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//input[@type='password'])[2]""").send_keys(password)
            time.sleep(0.1)
            driver.find_element(by=By.XPATH, value="""(//label[text()='Mobile Number']/following::input)[1]""").send_keys(
                phone)
            time.sleep(0.1)
            if "false" in ticker.lower():
                driver.find_element(by=By.XPATH, value="""(//input[@type='checkbox'])[1]""").click()
            driver.find_element(by=By.XPATH, value="""(//input[@type='checkbox'])[2]""").click()
            time.sleep(0.1)
            driver.find_element(by=By.XPATH,value="""//input[@value='Register Now']""").click()
            counter += 1
            filee = open("counter.txt", "w")
            filee.write(str(counter))
            filee.close()
            time.sleep(0.1)
            print(f"""New Account Registered Successfully | {email}""")
            print("-----------------------------\n")
            driver.quit()
        except:
            pass
