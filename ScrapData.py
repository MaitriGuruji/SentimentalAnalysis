import pandas as pd
import requests
from bs4 import BeautifulSoup

reviews = []
names = []
stars = []
helpfulStaments = []
    

for i in range(1,100):

    url = "www.amazon.in/Samsung-Galaxy-M30-Gradation-Blue/product-reviews/B07HGJJ58K/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=" + str(i)
    
   
    r = requests.get("https://" + url)
    soup = BeautifulSoup(r.content,'html.parser')
    
    name = soup.findAll('div', attrs={'class': 'a-section celwidget'})
    for span in name:
        temp = span.findAll('div', attrs={'class': 'a-profile-content'})
        names.append(temp)
        
    
    #for i in range(0, len(names)):
    #    temp = names[i].text
    #    names[i] = temp
    
    
    review = soup.findAll('div', attrs={'class': 'a-row a-spacing-small review-data'})
    for span in review:
        reviews.append(span)
        
    
    star = soup.findAll('i', attrs={'data-hook': 'review-star-rating'})
    for temp2 in star:
        temp3 = temp2.findAll('span', attrs={'class': 'a-icon-alt'})
        stars.append(temp3)
        
    
    #for i in range(0, len(reviews)):
    #    temp = reviews[i].text
    #    reviews[i] = temp
    # 
    
    
    for i in range(0, len(stars)):
         print(stars[i])
        
    helpfulStament = soup.findAll('span', attrs={'data-hook': 'helpful-vote-statement'})
    for span in helpfulStament:
        helpfulStaments.append(span)    
    
#    for i in range(0, len(helpfulStaments)):
#        temp = helpfulStaments[i].text
#        helpfulStaments[i] = temp
    
    
df = pd.DataFrame(list(zip(names, reviews,stars,helpfulStaments)), columns=['Name', 'Reviews','Stars','HelpfulStatements'])
df.to_csv('mcsv_99.csv', index=False, header=True)
    
    
