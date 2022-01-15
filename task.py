from RPA.Browser.Selenium import Selenium
from RPA.Word.Application import Application as app
from time import sleep
import pandas as pd



browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)



def scraping_individual_investments():
    input_field = 'xpath : //*[@id="investments-table-object_length"]/label/select'
    browser_lib.click_element(input_field)
    sleep(2)
    browser_lib.press_keys(input_field, "All")
    sleep(10)
    elems = browser_lib.find_elements(locator="xpath: //a[@href]")
    print(elems)
    for elem in elems:
        res = elem.find_element("name:href")
        print(res)
       
    # titles = browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object_wrapper"]/div[3]/div[1]/div/table/thead')
    # df = pd.DataFrame(columns=[t.text for t in titles])
    # df.head()
    # print(df.head())
    # sleep(3)
    # try:
    #     states = browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr')
    #     for idx, s in enumerate(states):
    #         print('row {}:'.format(idx))
    #         print('{}'.format(s.text))
    #     col2 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[1]')
    #     col3 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[2]')
    #     col4 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[3]')
    #     col5 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[4]')
    #     col6 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[5]')
    #     col7 =  browser_lib.find_elements(locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[6]')
    #     df[df.columns[0]] = [s.text for s in states]
    #     df[df.columns[1]] = [s.text for s in col2]
    #     df[df.columns[2]] = [s.text for s in col3]
    #     df[df.columns[3]] = [s.text for s in col4]
    #     df[df.columns[4]] = [s.text for s in col5]
    #     df[df.columns[5]] = [s.text for s in col6]
    #     df[df.columns[6]] = [s.text for s in col7]
    # except IndexError:
    #     print(" All entries was write")
    # df.head()
    # df.to_csv('/home/baritraser/w_project/vs_code/output/Individual Investments.csv')

def download_bs_case():
    data = browser_lib.click_link(locator='xpath : //*[@id="investments-table-object"]/tbody/tr[1]/td[1]/a')
    print(data)
    sleep(3)
    # link = [x for x in ]
    # link_of_pdf = browser_lib.click_link(locator='xpath : //*[@id="business-case-pdf"]/a')
    # save_as = app.save_document_as('/home/baritraser/w_project/vs_code/output/business_case1.pdf')
    
    
   
def main():
    try:
        open_the_website("https://itdashboard.gov/drupal/summary/393")
        sleep(10)
        scraping_individual_investments()
        # download_bs_case()
    finally:
        sleep(2)
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()