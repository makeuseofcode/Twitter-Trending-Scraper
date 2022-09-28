#importing the required modules
from selenium import webdriver
import time
import pandas as pd

#creating object of chromedriver
cd='chromedriver'

#open google chrome browser
browser=webdriver.Chrome(cd)

#open the trending page of Twitter
browser.get('https://twitter.com/explore/tabs/trending')

#delay for page content loading
time.sleep(15)

#find the trending topic and hashtags
trending_topic_content=[]
for i in range(3,13):
    xpath = f'//div[@aria-label="Timeline: Explore"]/div[1]/div[{i}]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]'
    trending_topic = browser.find_element(By.XPATH, xpath)
    trending_topic_content.append(trending_topic.text)

#create URLs using the hashtags collected
urls=[]
for i in trending_topic_content:
	url='https://twitter.com/search?q=%23'+i+'&src=trend_click'
	url = url.replace(" ", "%20")
	urls.append(url)

#create a dictionary that has both the Hashtag and the URLs
dic={'HashTag':trending_topic_content,'URL':urls}

#create the dictionary to a dataframe in pandas
df=pd.DataFrame(dic)
print(df)

#convert the dataframe into Comma Seperated Value format with no serial numbers
df.to_csv("Twitter_HashTags.csv",index=False)
