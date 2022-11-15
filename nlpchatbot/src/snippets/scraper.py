from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pickle
import time
from settings import *

# PWkc7 La classe du spinner des conversations
# _26F99 la classe des reponse explicites stickers
# _22Msk la classe des reponses explicites textes
# _33LGR classe de la liste des message
# cvjcv._1p8Qv.EtBAv Signe que nous sommes arrive a premier message

js_scroll_to_top = """
msg_panel = document.getElementsByClassName("_33LGR")[0];
top = [];
while(top.HTMLDivElement == undefined){
    tentatives = 3;
    while(tentatives > 0){
        spinner = document.getElementsByClassName("PWkc7");
        if(spinner.length === 0){
            tentatives = 0;
        }
        else{
            await new Promise(r => setTimeout(r, 2000))
            tentatives-=1;
        }
    }
    msg_panel.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 500))
    top = document.getElementsByClassName("cvjcv _1p8Qv EtBAv");
}

"""


class Conversation:
    def __init__(self, name=None, nbr_unread_msg=None, messages=None):
        self.name = name
        self.nbr_unread_msg = nbr_unread_msg
        self.messages = messages if messages else []

    def __str__(self):
        return "{}: {} messages non lus".format(self.name.strip(), self.nbr_unread_msg)

class BotMemory():
    def __init__(self):
        self.storage = {}  ## Storage stores the top 5 users name and last chat time
        
    def updateUser(self, details):
        self.storage[details[0]] = details[1]

    def updateTime(self, user, time):
            self.storage[user] = time
        
    def addAll(self, details):
        for usertime in details:
            self.storage[usertime[0]] = usertime[1]
            
    def existingUser(self):
        return self.storage.keys()
    
    def chatTime(self, user):
        return self.storage[user]


class WhatsappScraper:
    def __init__(self):
        self.driver = None

    def fetch_all_msgs(self):
        archive = self.driver.find_elements_by_class_name("_2nY6U._1frFQ")
        time.sleep(1)
        convs = self.driver.find_elements_by_class_name("_2nY6U")
        convs = convs[1:] if archive else convs
        i = 0
        for conv in convs:
            try:
                conv.click()
            except Exception:
                pass
            time.sleep(2)
            print(self.get_last_n_msgs(5))
            # wait = WebDriverWait(
            # self.driver, 1000, poll_frequency=500, ignored_exceptions=TimeoutException).until(
            # EC.presence_of_all_elements_located((By.CLASS_NAME, "cvjcv _1p8Qv EtBAv")))
            # timeout = True
            # while timeout:
            # try:
            # self.driver.execute_script(js_scroll_to_top)
            # timeout = False
            # except TimeoutException:
            # pass
            # else:
            # timeout = False

            # a = input("On passe au suivant ?")
            # if a.upper() == 'N':
            # break
            # i+=1
        # print("J'ai trouve {} elements".format(i))

    def fetch_all_msgs_old(self):
        js_script1 = """
        function getVisible() {
        var $el = $('#foo'),
        scrollTop = $(this).scrollTop(),
        scrollBot = scrollTop + $(this).height(),
        elTop = $el.offset().top,
        elBottom = elTop + $el.outerHeight(),
        visibleTop = elTop < scrollTop ? scrollTop : elTop,
        visibleBottom = elBottom > scrollBot ? scrollBot : elBottom;
        return visibleBottom - visibleTop;
        }
        arguments[0].scrollTop += getVisible();
        """
        js_script2 = """
        let box = document.querySelector('._2nY6U');
        let height = box.clientHeight;
        let to_add = height*17;
        arguments[0].scrollTop += to_add;
        
        """
        pane = self.driver.find_element_by_id("pane-side")
        # pane.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pane)
        # self.driver.execute_script(js_script2)
        time.sleep(2)
        # htmlcode=(self.driver.page_source).encode('utf-8')
        # soup = BeautifulSoup(htmlcode,features="html.parser")
        # with open("unreads.html", 'r') as f:
        #     soup  = BeautifulSoup(f.read(), features="html.parser")
        # elts = soup.find_all('div', class_='_3OvU8')
        for i in range(3):
            htmlcode = (self.driver.page_source).encode("utf-8")
            soup = BeautifulSoup(htmlcode, features="html.parser")
            elts = soup.find_all("div", class_="_2nY6U")
            for elt in elts:
                print(elt.text)
                # self.driver.execute_script("arguments[0].scrollIntoView();", elt)
            # self.driver.execute_script("arguments[0].scrollTop += document.getElementById('pane-side')", pane)
            self.driver.execute_script(js_script2, pane)
            print("============================================================")
            time.sleep(5)

    def inconversations(self, cname, conversations):
        for c in conversations:
            if c.name == cname:
                return c
        return None

    def get_last_n_msgs(self, n):
        htmlcode = (self.driver.page_source).encode("utf-8")
        soup = BeautifulSoup(htmlcode, features="html.parser")
        # with open("./core/unreads.html", 'r') as f:
        # soup  = BeautifulSoup(f.read(), features="html.parser")
        d = soup.find_all("div", class_="copyable-text")
        messages = []
        for i in range(0, len(d)):
            s = d[i].find(
                "span", class_="emoji-texttt i0jNr selectable-text copyable-text"
            )
            if d[i].get("data-pre-plain-text") and s:
                raw_msg = [d[i].get("data-pre-plain-text"), s.span.text]
                msg = raw_msg[1]
                msg = (msg.replace("\n", " ")).replace(" " * 2, "")
                raw_sr = raw_msg[0].split("]")
                sr = raw_sr[1][1:-2]
                raw_datetime = raw_sr[0].split(",")
                srtime = raw_datetime[0][1:]
                srdate = raw_datetime[1][1:]
                m = {"date": srdate, "time": srtime, "sender": sr, "message": msg}
                messages.append(m)
        return messages[-n:]

    def click_unread_convs(self, unread_convs):
        for conv in unread_convs:
            item = self.driver.find_element_by_xpath(
                '//span[contains(@title, "{}")]'.format(conv.name)
            )
            print("Je vais cliquer sur {}".format(item.text))
            item.click()
            messages = self.get_last_n_msgs(conv.nbr_unread_msg)
            return messages

    def get_unread_msgs(self):

        htmlcode = (self.driver.page_source).encode("utf-8")
        soup = BeautifulSoup(htmlcode, features="html.parser")
        # with open("unreads.html", 'r') as f:
        #     soup  = BeautifulSoup(f.read(), features="html.parser")
        elts = soup.find_all("div", class_="_3OvU8")
        conversations = []
        for item in elts:
            badge = item.find_all("span", class_="_23LrM")
            if badge:
                span_nom = item.find_all(
                    "span", class_="emoji-texttt _ccCW FqYAR i0jNr"
                )
                nom = span_nom[0].getText()
                nbr = badge[0].get("title")
                c = Conversation(name=nom, nbr_unread_msg=nbr)
                conversations.append(c)
        self.click_unread_convs(conversations)

    
    def _get_time_tuple(time_str):
        hour = int(time_str.split(':')[0])
        if hour > 12:
            hour -= 12
        min_str = time_str.split(':')[1][:-1]
        minute = int(min_str)
        #sec = int(time_str.split(':')[2].split(".")[0])
        #return(hour, minute, sec)
        return(hour, minute)


    def _get_user_list(self, max_num = 5):
        htmlcode = (self.driver.page_source).encode('utf-8')
        soup = BeautifulSoup(htmlcode, features="html.parser")
        users = []
        div = soup.find_all('div', class_ = '_3OvU8')
        for i in div:
            isoup = BeautifulSoup((i).encode('utf-8'), features="html.parser")
            time_raw = isoup.find_all('div', class_ = '_1i_wG')
            if time_raw:
                user = i.span.text
                timing = time_raw[0].text.split()[0]
                if timing.split(":")[0].isdigit():
                    users.append([user, timing])
        users = sorted(users, key = lambda x: x[1], reverse = True)
        return users[: max_num]


    
    def start(self):
        chr_options = ChromeOptions()
        chr_options.add_argument(r"user-data-dir=./driver/data")
        try:
            self.driver = webdriver.Chrome("chromium.chromedriver", options=chr_options)
            self.driver.get("https://web.whatsapp.com/")
        except Exception as e:
            print(e)
        cookies = pickle.load(open(COOKIES_PATH, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def stop(self):
        pickle.dump(self.driver.get_cookies(), open(COOKIES_PATH, "wb"))
        self.driver.quit()


if __name__ == "__main__":
    sc = WhatsappScraper()
    sc.start()
    time.sleep(30)
    sc.fetch_all_msgs()
    a = input("Je peux fermer ?")
    if a == "o":
        sc.stop()
    else:
        sc.fetch_all_msgs()
