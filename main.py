from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep
from selenium.webdriver.common.keys import Keys

import constants


def get_tweet_content(card1):
    content = card1.find_element_by_xpath(
        '//div[@class="css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
    spans = content.find_elements_by_xpath('.//span')
    for s in spans:
        print(s.text)
    print('_____________________________________________________')


options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get(constants.log_in_link)
sleep(1.3)
email = driver.find_element_by_xpath("//input")
email.send_keys(constants.email)
email.send_keys(Keys.RETURN)
sleep(0.6)
username = driver.find_element_by_xpath("//input")
username.send_keys(constants.username)
username.send_keys(Keys.RETURN)
sleep(0.6)
password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys(constants.password)
password.send_keys(Keys.RETURN)

query = 'kosovo (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic OR from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV)'
sleep(4)
search = driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]')
search.send_keys(query)
search.send_keys(Keys.RETURN)
sleep(6)
cards = driver.find_elements_by_xpath('//div[@class="css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu"]')

for i in range(len(cards)):
    card = cards[i]
    get_tweet_content(card)