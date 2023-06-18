import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from combinations import generate_combinations
ua = UserAgent()

if __name__ == '__main__':
    file = open("info.txt", "r")
    fdata = file.readlines()
    countfile = open("counter.txt", "r")
    start = int(countfile.read().strip())
    countfile.close()
    fname = fdata[0].split("::")[1].strip()
    lname = fdata[1].split("::")[1].strip()
    password = fdata[4].split("::")[1].strip()
    phone = fdata[5].split("::")[1].strip()
    ticker = fdata[6].split("::")[1].strip()

    counter = start+1
    numAcc = 10

    combinations = generate_combinations(fdata[2].split("::")[1].strip())
    
    while counter <= (start+numAcc):
        try:
            print(f"""{counter}/{(start+numAcc)}""")
            counter+=1
            email = combinations[counter] +"@" + fdata[3].split("::")[1].strip()
            user_agent = ua.random
            options=webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument("--log-level=3")
            options.add_argument('--disable-gpu')
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument(f'user-agent={user_agent}')
            driver = webdriver.Chrome(options=options)
            # driver.maximize_window()
            driver.get("https://secure.takealot.com/account/register")
            time.sleep(3)
            print("------------- Account Registration Started ----------------")
            print("Website Loaded Successfully")
            driver.find_element(by=By.XPATH, value="""//*[@id="register_customer_first_name"]""").send_keys(
                fname)
            print(f"""Name""")
            time.sleep(0.5)
            driver.find_element(by=By.XPATH, value="""//*[@id="register_customer_last_name"]""").send_keys(
                lname)
            print(f"""lastName""")
            time.sleep(0.25)
            driver.find_element(by=By.XPATH, value="""(//*[@id="register_customer_email"])[1]""").send_keys(email)
            time.sleep(0.25)
            print(f"""email {email}""")
            driver.find_element(by=By.XPATH, value="""//*[@id="register_customer_new_password"]""").send_keys(
                password)
            time.sleep(0.25)
            driver.find_element(by=By.XPATH, value="""//*[@id="register_customer_mobile_national_number"]""").send_keys(
                phone)
            print(f"""password""")
            time.sleep(0.25)
            driver.find_element(by=By.XPATH,value="""//*[@id="shopfront-app"]/div[3]/div/section/div/div/div[1]/div/div/div/div/div[3]/form/div[9]/div/button""").click()
            time.sleep(1)
            print(f"""New Account Registered Successfully | {email}""")
            print("-----------------------------\n")
            driver.quit()
        except:
            print("error")
            pass


