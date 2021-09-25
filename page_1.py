from bs4 import BeautifulSoup
import requests

class page_01:
    def scrap_1(self,link): #doctor page link ..
        a = []
        html_text_1 = requests.get(link).text
        soup_1 = BeautifulSoup(html_text_1, 'lxml')
        table_1 = soup_1.find('table', class_='table-bordered table-striped table-condensed cf')
        inner_table_1 = table_1.find('tbody')
        details_1 = inner_table_1.find_all('tr')
        for each in details_1:
            try:
                each_ind = each.find_all('td')
                for each_ind_details in each_ind:
                    continue

                link_11 = each_ind_details.a['href']
                a.append("https://www.drdata.in/" + link_11)
            except:
                pass

            #print("https://www.drdata.in/" + link_11)
            #linkss = "https://www.drdata.in/" + link_11
        return a

    def scrap_2(self,link): #next pages link
        ac = []
        html_text_1 = requests.get(link).text
        soup_2 = BeautifulSoup(html_text_1, 'lxml')
        #next_ = soup_2.find('div',class_= 'col-sm-12')#
        find_a =soup_2.find_all('a',class_='pnavi')
        for i in find_a:
            ac.append("https://www.drdata.in/"+i['href'].replace(" ",'%20'))
        return len(ac) , ac
        #print(len(find_a))

    def doctor_details(self,link_): #extract the exact details what we want

        actual_details = []
        tail = ['Name', 'Specialization', 'Degree', 'Area of Practice', 'Date of Birth', 'Address', 'State', 'District', 'Geographical Area','Phone Number','Mobile Number and Email']
        html_text_3 = requests.get(link_).text
        soup_3 = BeautifulSoup(html_text_3, 'lxml')
        find_table = soup_3.find('table',class_= 'table-bordered table-striped table-condensed cf')
        try:
            details = find_table.find_all('td')
            for i in range(0,len(details)):
                #print(details[i].text)
                #header.append(details[i].text)
                if details[i].text == 'Name':
                    if details[i+1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)

                """if details[i].text == 'Specialization':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'Degree':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'Area of Practice':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'Date of Birth':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'Address':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'State':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details[i].append(details[i+1].text)
                if details[i].text == 'District':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)
                if details[i].text == 'Geographical Area':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)"""
                if details[i].text == 'Phone Number':
                    if details[i + 1].text == '':
                        actual_details.append('NaN')
                    else:
                        actual_details.append(details[i+1].text)



                #d[details[i].text] = details[i+1].text
        except:
            pass
        return actual_details #returns the list of doctors from given page




