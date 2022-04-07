import csv

from msedge.selenium_tools import EdgeOptions, Edge
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import constants


def get_tweet_content_and_language(card1):

    content_div = card1.find_element_by_xpath(
        'descendant::div[@class="css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]'
    )
    language = content_div.get_attribute('lang')
    spans = content_div.find_elements_by_xpath('.//span')
    text = ""
    for s in spans:
        text += s.text
    return text, language


def handle_cards(driver, topic):
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True
    while scrolling:
        cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
        for card in cards[-15:]:
            tweet = get_tweet_data(card, topic)
            if tweet:
                tweet_id = ''.join(tweet['handle'] + tweet['timestamp'] + tweet['topic'])
                if tweet_id not in tweet_ids:
                    print(tweet)
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


def round_to_point_five(number):
    return round(number * 2) / 2


def get_tweet_data(card, topic):
    try:

        tweet_handle = card.find_element_by_xpath('.//span[contains(text(),"@")]').text
        tweet_username = card.find_element_by_xpath('.//span').text
        tweet_date_time = card.find_element_by_xpath('.//time').get_attribute('dateTime')
        tweet_economic_policy = constants.accountMap[tweet_handle][0]
        tweet_social_policy = constants.accountMap[tweet_handle][1]
        (tweet_content, tweet_language) = get_tweet_content_and_language(card)
        tweet = {'handle': tweet_handle, 'username': tweet_username, 'timestamp': tweet_date_time,
                 'content': tweet_content,
                 'topic': topic, 'language': tweet_language,
                 'economic_policy': tweet_economic_policy,
                 'social_policy': tweet_social_policy,
                 'economic_policy_rounded': round_to_point_five(tweet_economic_policy),
                 'social_policy_rounded': round_to_point_five(tweet_social_policy),
                 }

        print(tweet)
        return tweet
    except NoSuchElementException:
        return


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

#query = 'kosovo (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic OR from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV)'
tweet_ids = set()
tweets = []
sleep(5)
for topic in constants.queries.keys():
    for query in constants.queries[topic]:
        search = driver.find_element_by_xpath('//input[@placeholder="Search Twitter"]')
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        sleep(6)
        try:

            newSearch = driver.find_element_by_xpath('//a[contains(text()="Search instead for ")]')
            newSearch.send_keys(Keys.RETURN)
            print("_________________________ FOLLOWING LINK_____________________________")
            sleep(6)
        except NoSuchElementException:
            ""
        handle_cards(driver, topic)

with open('tweet_data.csv', 'w', encoding='utf8', newline='') as f:
    header = ['handle', 'username', 'timestamp', 'content', 'topic', 'language', 'economic_policy', 'social_policy',
              'economic_policy_rounded', 'social_policy_rounded']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    print(len(tweets))
    writer.writerows(tweets)
