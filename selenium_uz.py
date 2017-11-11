import bs4
import time
from selenium import webdriver,common

# import selenium.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BoockTicket():
    def __init__(self, station_from, station_till, day,
                 month=10, type='П', place = "fr", train = None, time=None, amount = 1):

        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(15)

        self.driver.get("https://booking.uz.gov.ua/ru/")
        self.list_of_booked_tikets = []
        self.station_from=station_from
        self.station_till = station_till

        self.day = day
        self.month = month

        self.type = type
        self.place = place
        self.amount = amount
        self.train = train

        self.select_station_from()
        self.select_station_till()
        self.select_date(self.day)

        self.search_trains()
        self.show_trains()

        number = self.select_plece()
        self.bookTicket()
        # self.pay()



        # book several tickets
        # self.cancel_booking()

        # self.book_N_tickets(self.amount)




        # time.sleep(3)

        # if number:
        #     print(number)
        #     self.book_again(number)


        # self.pay()
    def book_N_tickets(self,n):
        for i in range(n):
            print(i)
            time.sleep(1)
            self.search_trains()
            self.show_trains()

            number = self.select_plece()

            self.bookTicket()

    def select_station_from(self):
        input_element = self.driver.find_element_by_name("station_from")
        input_element.send_keys(self.station_from)
        # time.sleep(2)

        # station_list = WebDriverWait(self.driver, 50).until(
        #     EC.presence_of_element_located((By.ID, "ui-id-1")))
            
        station_list = self.driver.find_element_by_id("ui-id-1")
        items = station_list.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            if text == self.station_from:
                item.click()
                break

    def select_station_till(self):
        input_element = self.driver.find_element_by_name("station_till")
        input_element.send_keys(self.station_till)
        # time.sleep(2)
        station_list = self.driver.find_element_by_id("ui-id-2")
        items = station_list.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            if text == self.station_till:
                item.click()
                break

    def select_date(self,day):
        """Only day of Octouber"""
        date = self.driver.find_element_by_id('date_dep')
        date.click()
        # time.sleep(2)

        b=bs4.BeautifulSoup(self.driver.page_source)
        print(b.find(id = 'ui-datepicker-div'))

        datepicker_div = self.driver.find_element_by_id('ui-datepicker-div')
        print(type(datepicker_div))
        datepicker_group_first = datepicker_div.find_element_by_tag_name('div')

        td_days = datepicker_group_first.find_elements_by_tag_name("a")
        print(td_days)

        for i in td_days:
            print(i.text)
            if i.text == day:
                i.click()
                break

    def search_trains(self):
        # time.sleep(4)

        button = WebDriverWait(self.driver,100).until(
            EC.element_to_be_clickable((By.NAME, 'search')))
        # print(EC.element_to_be_clickable((By.NAME, 'search')) == True)

        # if EC.element_to_be_clickable((By.NAME, 'search')
        # button = self.driver.find_element_by_name('search')

        button.click()
        print('button clicked')


    def show_trains(self):
        # time.sleep(5)
        n=0
        page_source = self.driver.page_source
        # f=open('page-soure','w')
        # f.write(page_source)
        # f.close()
        # while 'По заданному Вами направлению мест нет' in page_source:
        #     self.search_trains()
        #     page_source = self.driver.page_source
        #     # f = open('page-soure', 'r')
        #     # page_source = f.read()
        #     # f.close()
        #     n += 1
        #     print(n)
        #     time.sleep(4)
        time.sleep(3)

        # if 'По заданному Вами направлению мест нет' in page_source:
        #     n += 1
        #     print(n, 'По заданному Вами направлению мест нет')
        #     self.search_trains()
        #     page_source = self.driver.page_source
        #
        #     return self.show_trains()
        #
        # n=0
        # time.sleep(3)
        #
        # if 'Плацкарт' not in page_source:
        #     n += 1
        #     print(n, 'Плацкарт not found')
        #     self.search_trains()
        #
        #
        #     return self.show_trains()

        print("-------------------------------")
        table_trains = self.driver.find_element_by_id('ts_res_tbl')
        list_trains = table_trains.find_elements_by_tag_name('tr')
        print(list_trains)

        if not len(list_trains)>1:
            print('По заданному Вами направлению мест нет!!!!')

        for t in list_trains[1:]:
            place_element = t.find_element_by_class_name('place')
            coaches = place_element.find_elements_by_tag_name('div')
            train_num = t.find_element_by_class_name('num').text
            print(train_num)


            if train_num ==self.train:
                """Поиск мест в заданном поезде"""

                if 'П' not in place_element.text:
                    """Если в поезде нет плацкартных мест, то изкать заново"""
                    print("Если в поезде нет плацкартных мест, то изкать заново")
                    self.search_trains()
                    return self.show_trains()

                for coach in coaches:
                    print()
                    types_coach = coach.find_elements_by_tag_name('i')

                    for type_coach in types_coach:
                        print(type_coach.text)
                        if type_coach.text == self.type:
                            select_coach = coach.find_element_by_tag_name('button')
                            select_coach.click()
                            return


        print('Train', self.train, ' not found')
        self.search_trains()
        return self.show_trains()

    def choose_coach(self):
        # def get_key(ite):
        time.sleep(2)
        coaches = self.driver.find_element_by_class_name('coaches').\
            find_elements_by_tag_name('a')

        print(coaches[0].text[0])

        # amount_places = [(int(c.text[2:].strip('/n')),c) for c in coaches]

        amount_places = [(int(c.find_element_by_tag_name('b').text),c) for c in coaches]
        print(amount_places)

        amount_places.sort(key = lambda i: i[0])      #sort by amount plases
        amount_places.reverse()

        if amount_places[0][1] != coaches[0]:
            time.sleep(1)
            amount_places[0][1].click()
            print(amount_places[0][0])

    def select_plece(self,number=False):


        time.sleep(4)
        self.choose_coach()
        time.sleep(4)


        coach_sheme = self.driver.find_element_by_class_name('coachScheme')
        place_table = coach_sheme.find_element_by_class_name('floor-1')
        places = place_table.find_elements_by_class_name('fr')

        #Ищет сначала нижние места - потом верхние.
        for p in places:
            if int(p.text)%2 == 1:
                    # and int(p.text) != 37\

                if number:
                    if int(p.text) == number:
                        self.place_number = p.text
                        p.click()
                        self.list_of_booked_tikets.append(p.text)
                        return int(p.text)

                else:
                    self.place_number = p.text
                    p.click()
                    self.list_of_booked_tikets.append(p.text)
                    return int(p.text)

        for p in places:
            if int(p.text) % 2 == 0 :
                self.place_number = p.text
                p.click()
                self.list_of_booked_tikets.append(p.text)
                return int(p.text)
        return False
            # elif int(p.text)%2 == 0:

                # places[0].click()

    def bookTicket(self):
        # time =
        mainTable = self.driver.find_element_by_class_name('vToolsDataTableRow2')
        # select_stud = mainTable.find_element_by_name('15079957238843355673512907455500')
        # select_stud.click()
        lastName = self.driver.find_element_by_class_name('lastname')
        lastName.send_keys("asdfasdf")

        firstName = self.driver.find_element_by_class_name('firstname')
        firstName.send_keys("asdfasdf")
        time.sleep(4)

        div = self.driver.find_element_by_id('ts_chs_tbl')
        book_button = div.find_element_by_class_name('complex_btn')
        book_button.click()
        print('=============================================================')
        print('Ticket was booked')
        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        print('=============================================================')

    def book_again(self,number):
        for i in range(10):
            self.search_trains()
            self.show_trains()
            self.select_plece(number)
            self.bookTicket()

    def pay(self):
        time.sleep(3)
        pay_button = self.driver.find_element_by_class_name('complex_btn')
        pay_button.click()
        time.sleep(1)
        email_field = self.driver.find_element_by_name('email')
        email_field.send_keys('vladbandurin@gmail.com')

        confirmed_checkbox = self.driver.find_element_by_name('is_confirmed')
        confirmed_checkbox.click()

        cart_pay_form = self.driver.find_element_by_class_name('cart_pay_form')
        button_save_email = cart_pay_form.find_element_by_tag_name('button')
        button_save_email.click()
        self.url = self.driver.current_url
        print(self.url)

    def cancel_booking(self):
        print('cancel_booking')
        divs = self.driver.find_elements_by_class_name('cart-btn')
        print(len(divs))
        for d in divs[1:]:
            time.sleep(2)
            a = d.find_element_by_tag_name('a')
            a.click()

            div = self.driver.find_element_by_class_name('vToolsPopupToolbar')
            button = div.find_elements_by_tag_name('button')
            button[0].click()
        time.sleep(2)

if __name__ == '__main__':
    BoockTicket('Краматорск', "Киев", "30", type='П', train="124 Д")

    a = input()

# time.sleep(7)
# while 1:
#
#     a= input()
# driver.close()
