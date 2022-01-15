from RPA.Browser.Selenium import Selenium
from time import sleep
import pandas as pd


browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def click_dive_in(field):
    browser_lib.click_element(locator=field)


def get_all_amount_of_agencies():
    agencies_data = []
    agencies_list = browser_lib.find_elements(
        locator='xpath : //*[@id="agency-tiles-widget"]')
    print(agencies_list)
    for agency in agencies_list:
        agency_name = agency.find_elements(locator='class : seals')[0]
        agency_amount = agency.find_elements(
            locator='xpath : //*[@id="agency-tiles-widget"]/div/div[2]/div[2]/div/div/div/div[1]/a/span[2]')[0]
        agencies_info = [agency_name,
                         agency_amount]
        agencies_data.append(agencies_info)
    agencies_data_df = pd.DataFrame(agencies_data)
    agencies_data_df.columns = ['Agency_Name',
                                'Agency_Mount']
    agencies_data_df.to_csv("Agencies", index=False)


def choose_agency(field):
    browser_lib.click_image(locator=field)


def scraping_individual_investments():
    input_field = 'xpath : //*[@id="investments-table-object_length"]/label/select'
    browser_lib.click_element(input_field)
    sleep(2)
    browser_lib.press_keys(input_field, "All")
    sleep(5)
    titles = browser_lib.find_elements(
        locator='xpath : //*[@id="investments-table-object_wrapper"]/div[3]/div[1]/div/table/thead')
    df = pd.DataFrame(columns=[t.text for t in titles])
    df.head()
    print(df.head())
    sleep(3)
    try:
        states = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr')
        for idx, s in enumerate(states):
            print('row {}:'.format(idx))
            print('{}'.format(s.text))
        col2 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[2]')
        col3 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[3]')
        col4 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[4]')
        col5 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[5]')
        col6 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[6]')
        col7 = browser_lib.find_elements(
            locator='xpath : //*[@id="investments-table-object"]/tbody/tr/td[7]')
        df[df.columns[0]] = [s.text for s in states]
        df[df.columns[1]] = [s.text for s in col2]
        df[df.columns[2]] = [s.text for s in col3]
        df[df.columns[3]] = [s.text for s in col4]
        df[df.columns[4]] = [s.text for s in col5]
        df[df.columns[5]] = [s.text for s in col6]
        df[df.columns[6]] = [s.text for s in col7]
    except IndexError:
        print(" All entries was write")
    df.head()
    df.to_csv('Individual Investments.csv')

def download_bs_case():
    links = browser_lib.get_all_links('class : left sorting_2')
    for link in links:
        browser_lib.click_link(link)

# Define a main() function that calls the other functions in order:


def main():
    try:
        open_the_website("https://itdashboard.gov/")
        sleep(2)
        click_dive_in(
            'xpath:/html/body/main/div[1]/div/div/div[3]/div/div/div/div/div/div/div/div/div/a')
        sleep(2)
        # get_all_amount_of_agencies()

        # choose_agency('xpath://*[@id="agency-tiles-widget"]/div/div[1]/div[3]/div/div/div/a/img')
        choose_agency(
            'xpath : //*[@id="agency-tiles-widget"]/div/div[8]/div[3]/div/div/div/a/img')

        sleep(10)
        scraping_individual_investments()
    finally:
        sleep(2)
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
