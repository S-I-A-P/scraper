from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import constants


def get_tweet_content(card1):
    content_div = card1.find_element_by_xpath(
        'descendant::div[@class="css-901oao r-1fmj7o5 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]'
    )
    spans = content_div.find_elements_by_xpath('.//span')
    text = ""
    for s in spans:
        text += s.text
    return text


def handle_cards(driver):
    tweets = []
    tweet_ids = set()
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True
    while scrolling:
        cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
        for card in cards[-15:]:
            tweet = get_tweet_data(card)
            print(tweet)
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    tweets.append(tweet)
        scroll_attempt = 0
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(1)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    sleep(2)
            else:
                last_position = curr_position
                break
    return tweets


def get_tweet_data(card):
    tweet_handle = card.find_element_by_xpath('.//span[contains(text(),"@")]').text
    tweet_username = card.find_element_by_xpath('.//span').text
    try:
        tweet_date_time = card.find_element_by_xpath('.//time').get_attribute('dateTime')
    except NoSuchElementException:
        return
    tweet_content = get_tweet_content(card)
    tweet = (tweet_handle, tweet_username, tweet_date_time, tweet_content)
    return tweet


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

for k in constants.queries.keys():
    for q in constants.queries[k]:
        sleep(4)
        search = driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]')
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(q)
        search.send_keys(Keys.RETURN)
        sleep(6)
        handle_cards(driver)
