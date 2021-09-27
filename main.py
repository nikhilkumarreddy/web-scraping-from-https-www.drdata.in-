import time
from bs4 import BeautifulSoup
import requests
from page_1 import page_01

import pandas as pd

head = ["col"+str(i) for i in range(0,3)] # details that we are scrapping

df = pd.DataFrame(columns=head)
html_text = requests.get('https://www.drdata.in/').text
soup = BeautifulSoup(html_text, 'lxml')
states = soup.find_all('div', class_= 'panel panel-default')
doctors_links = []
index_ = 0
for state in states:
    count_of_doctors_in_this_state = 0
    a = state.find('div', class_='panel-collapse collapse').find('div', class_  = 'panel-body')
    c = a.find('ul')
    d = c.find('li')
    k = d.a['href']
    j = d.a.h4.text
    print(j) #prints the state name for reference

    link_1 = "https://www.drdata.in/"+k #0th  page

    obj_1 = page_01()
    link_1st_page = obj_1.scrap_1(link_1)
    if len(link_1st_page) != 0 :
        #print(link_1st_page) #gives the 1st page of doctors links
        for ii in link_1st_page:
            list_ = obj_1.doctor_details(ii)
            #print(len(list_)," ",list_)
            count_of_doctors_in_this_state += 1
            print(list_)

            if len(list_) == 3: #if our len of  requirements matches going to write into dataframe
                df.loc[index_] = list_
                index_ += 1
                strings = list(j)

                print(len(list_), " ", list_)
        time.sleep(3)
    #break


    #doctors_links.append(link_1st_page)
    length_ , arr  = obj_1.scrap_2(link_1) # gives all the next pages of doctors of doctors link
    for ij in arr:
        list_all_next_pages = obj_1.scrap_1(ij)
        if len(list_all_next_pages) != 0:
            #print(list_all_next_pages)
            #doctors_links.append(list_all_next_pages)
            for i in list_all_next_pages:
                list__ = obj_1.doctor_details(i)

                count_of_doctors_in_this_state +=1
                print(list__)
                if len(list__) == 3:
                    df.loc[index_] = list__
                    index_ += 1
                    print("next page" ,len(list__), " ", list__)
    time.sleep(3)

    print(df.shape)
    print("Count of doctors in state ",j," ",count_of_doctors_in_this_state )


df.to_csv('out_put.csv')
print("DOne")


print(df.head(5))