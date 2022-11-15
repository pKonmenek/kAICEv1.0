from selenium import webdriver
from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import pickle
from loguru import logger
import time
from kaice.settings import *
from kaice.models import *
from kaice.bot import BotAI
from kaice.settings import (
    WEBDRIVER_PATH,
    WEBDRIVER_DATA_DIR,
    WEBDRIVER_DIR
) 
# from settings import *
# from models import *
# from bot import BotAI
# from settings import (
#     WEBDRIVER_PATH,
#     WEBDRIVER_DATA_DIR,
#     WEBDRIVER_DIR
# ) 
import sys
#: Classe CSS de la bare de recherche
INPUT_SEARCHBOX_CSS_CLASS = '_13NKt'
#: Classe CSS des conversations a gauche
DIV_CONVERSATION_PREVIEW_CSS_CLASS = '_3OvU8'
#: Xpath du bouton de recherche
BUTTON_SEARCH_XPATH = 'html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/button'
#: Classe CSS du bouton de recherche
BUTTON_SEARCH_CSS_CLASS = '_3yWey'
#: Xpath du la barre de recherche
INPUT_SEARCH_BOX_XPATH = '//*[@id="input-chatlist-search"]'
#: Classe CSS de la zone de saisie des message
INPUT_MESSAGE_CSS_CLASS = 'fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv'
#: Xpath de la zone de saisie des message
INPUT_MESSAGE_XPATH = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
#: Classe CSS du Span contenant le nom du contact dans la liste des conversations
SPAN_CONTACT_NAME_CSS_CLASS = 'ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr'
#: Xpath de la photo de profile du compte en cours d'utilisation
SPAN_SELF_PROFILE_PHOTO_XPATH = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
#: Xpath du bouton 3 points pour ouvrir les parametres
SETTINGS_3DOTS_XPATH = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[6]'
#: Classe CSS du nom de l'utilisateur en cours dans les parametres
DIV_NAME_IN_SETTINGS_CSS_CLASS = '_3vPI2'
#: Xpath du bouton retour dans les parametres
BUTTON_BACK_IN_SETTINGS_XPATH = '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/header/div/div[1]/button'
# BUTTON_BACK_IN_SETTINGS_XPATH = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/header/div/div[1]/button/span'
#: Classe CSS du div de la liste des conversations
DIV_CONVERSATIONS_LIST_CSS_CLASS = '_2nY6U'
#: Classe CSS du nom du contact dans la liste des conversations
DIV_CONVERSATION_NAME_CSS_CLASS = '_3q9s6'
#: Classe CSS de la date et l'heure du dernier message dans la liste des conversations.
DIV_CONVERSATION_RAW_TIME_CSS_CLASS = '_1i_wG'
#: Xpath du span contenant le nom du contact dans la conversation
SPAN_CONVERSATION_NAME_CONTACT_XPATH = '//span[contains(@title,{})]'
# DIV_CONVERSATION_IN_LIST_XPATH = '//span[@title="{}"]'


DEFAULT_MSG = "Désolé, je n'ai pas pu trouver une réponse satisfesante à votre message, Je ne suis pas encore assez entrainé."

#: URL de Whatsapp
WHATSAPP_URL = "https://web.whatsapp.com/"

class ContactNotFoundException(Exception):
    pass

class BotState:
    NOT_STARTED = 0
    STARTED = 1
    OFF = 2
    ON = 3


class ChatBot:
    """ Le chatbot qui communique sur Whatsapp en utilisant les reponses founis
     par ``BotAI``
        Example:
            >>>chatbot = ChatBot() # Creation du chatbot
            >>>chatbot.start() # Lancement et initialisation des variables
            >>>chatbot.start_chatting(["John Doe"], "msg recursif") # Commencer
    """
    def __init__(self):
        self.driver = None
        self.bot_ai = BotAI()
        self.activ_convs = []
        self.bot_memory = None
        self._running = False
        self.bot_state = BotState.NOT_STARTED
        self.rec_times = 0
        self.rec_message = ""
        self.rec_contacts = []


    def get_bot_name(self):
        """Methode qui permet de recuperer le nom du compte 
        Whatstapp qu'utilise le bot.
        """
        logger.info("Recuperation du nom de l'utilisateur du \
            compte associe ...")
        name = None
        max_retry = 5
        trying = 0

        while (not name) and (trying < max_retry):
            wait = WebDriverWait(self.driver, 600)
            dots3 = wait.until(EC.presence_of_element_located((
                    By.XPATH, SPAN_SELF_PROFILE_PHOTO_XPATH
                )))
            try:
                time.sleep(5)
                dots3.click()
            except Exception as e:
                logger.exception("Exception en essayant de cliquer sur les 3 points: ", e)
            parametres = wait.until(EC.presence_of_element_located((
                    By.XPATH, SETTINGS_3DOTS_XPATH
                )))
            try:
                time.sleep(5)
                parametres.click()
            except Exception as e:
                logger.exception("Impossible de cliquer sur les parametres ", e)
            htmlcode = (self.driver.page_source).encode('utf-8')
            soup = BeautifulSoup(htmlcode, features="html.parser")
            time.sleep(5)
            div = soup.find('div', {"class":DIV_NAME_IN_SETTINGS_CSS_CLASS})
            name = div.div.span.text
            trying += 1
        if name:
            logger.info("J'ai trouve le nom du bot: {}".format(name))
            try:
                self.bot_memory = BotMemory.get(bot_name=name)
            except DoesNotExist:
                self.bot_memory = BotMemory.create(bot_name=name)
                self.bot_memory.save()
            time.sleep(2)
            try:
                self.driver.find_element(
                        by=By.XPATH,
                        value=BUTTON_BACK_IN_SETTINGS_XPATH
                    ).click()
            except Exception as e:
                logger.exception(
                    "Impossible de retourner a la page d'acceuil: {}"
                    .format(str(e)))
                sys.exit()
        else:
            logger.critical('Impossible de trouver le nom du bot. Sortie...')
            exit(1)

   
    def _get_time_tuple(self, time_str):
        try:
            hour = int(time_str.split(':')[0])
            if hour > 12:
                hour -= 12
            min_str = time_str.split(':')[1][:-1]
            minute = int(min_str)
        except ValueError:
            minute = -1
            hour = -1
        return(hour, minute)


    def _get_user_list(self, max_num = 10):
        htmlcode = (self.driver.page_source).encode('utf-8')
        soup = BeautifulSoup(htmlcode, features="html.parser")
        users = []
        convs = soup.find_all('div', class_=DIV_CONVERSATIONS_LIST_CSS_CLASS)
        user = time_str = None

        for conv in convs:
            user_div = conv.find_all('span', class_=DIV_CONVERSATION_NAME_CSS_CLASS)
            if user_div and user_div[0].span:
                user = user_div[0].span.getText()
            else:
                user_div = conv.find_all('div', class_="zoWT4")
                if user_div and user_div[0].span:
                    user = user_div[0].span.getText()
            time_raw = conv.find_all(
                    'div',
                    class_ = DIV_CONVERSATION_RAW_TIME_CSS_CLASS
                )
            if time_raw:
                time_str = time_raw[0].text
            if user and time_str:
                users.append([user, time_str])
        users = sorted(users, key = lambda x: x[1], reverse = True)
        return users[:max_num]


    def search_chatter(self, name, click=False):
        """Procedure qui cherche un utilisateur specifique et 
        active sa conversation.
        Args: 
            Si `click` == True la conversation sera cliquee et ouverte.
        """
        wait = WebDriverWait(self.driver, 2)
        wait5 = WebDriverWait(self.driver, 5)
        # Selectionner la cible
        name = "\"" + str(name) + "\""
        x_arg = SPAN_CONVERSATION_NAME_CONTACT_XPATH.format(name)


        try:
            logger.info('Trying to find the contact {}'.format(name))
            wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg
            )))
        except Exception as e:
            logger.exception('Impossible de trouver le contact {} du a: \
                {}'.format(name, str(e)))
            # Si on ne voit pas directement le contact alors on le cherche 
            wait5.until(EC.presence_of_element_located((
                By.CLASS_NAME, INPUT_SEARCHBOX_CSS_CLASS
            )))
            input_searchbox = self.driver.find_element_by_class_name(INPUT_SEARCHBOX_CSS_CLASS)
            time.sleep(1)
            # clicker le bouton de recherche
            # self.driver.find_element_by_xpath(\
            #     SEARCH_BUTTON_XPATH).click()
            # self.driver.find_element_by_class_name(SEARCH_BUTTON_CSS_CLASS).click()
            input_searchbox.click()
            time.sleep(1)
            self._clear_search_box()
            input_searchbox.send_keys(name[1:len(name) - 1])
            time.sleep(1)
        finally:
            try:
                cdiv = self.driver.find_element_by_xpath(x_arg)
                if click:
                    cdiv.click()
                    self._clear_search_box()
                    logger.info("Contact {} selectionne avec succes".format(name))
            except NoSuchElementException:
                raise ContactNotFoundException
        time.sleep(2)


    def _clear_search_box(self):
        try:
            search_box = self.driver.find_element(
                by=By.CLASS_NAME,
                value=INPUT_SEARCHBOX_CSS_CLASS
            )
            search_box.clear()
        except Exception as e:
            logger.exception("Impossible de netoyer la zone de recherche: {}".format(str(e)))


    def get_last_n_msgs(self, n):
        """Permet de lire les dernier `n` messages d'une conversation ouverte.
        Returns: 
            Une liste de dictionnaire de messages sous forme:
            [{"date":date, "time":heure, "sender":emetteur, "mesage":contenu}]
        """
        htmlcode = (self.driver.page_source).encode("utf-8")
        soup = BeautifulSoup(htmlcode, features="html.parser")
        d = soup.find_all("div", class_="copyable-text")
        messages = []

        for i in range(0, len(d)):
            s = d[i].find(
                "span", class_="i0jNr selectable-text copyable-text"
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
                m = {
                    "date": srdate,
                    "time": srtime, 
                    "sender": sr, 
                    "message": msg
                    }
                if sr != self.bot_memory.bot_name:
                    messages.append(m)
        return messages[-n:]


    def get_unread_convs(self)->list:
        """Repere et retourne la liste des conversations non lues.
        Returns:
            (:obj:`list` of :obj:`dict`): Une liste de dictionnaires sous la forme::

                {
                    "name": nom de la conversation,
                    "number": nombre messages nom lues
                }
        """
        logger.info('Recuperation des conversations contenant des\
             messages non lus')
        time.sleep(1)
        htmlcode = (self.driver.page_source).encode("utf-8")
        soup = BeautifulSoup(htmlcode, features="html.parser")
        elts = soup.find_all(
            "div", class_=DIV_CONVERSATION_PREVIEW_CSS_CLASS)
        conversations = []
        for item in elts:
            div_badge = item.find("div", class_="_1pJ9J")
            if div_badge:
                span_nom = item.find_all("span", class_=SPAN_CONTACT_NAME_CSS_CLASS)
                nom = span_nom[0].getText()
                nbr_div = item.find('div', class_="_1pJ9J")
                nbr = nbr_div.span.getText()
                c = {'name':nom, 'number':int(nbr)}
                conversations.append(c)
        return conversations


    def click_convs(self, unread_convs)->list:
        """
        Clique par lot une liste de conversations et retourne 
        les messages lues.
        Retourne une liste de messages sous la forme:
        [{"name": emetteur, "messages": messageslus(objets)}]
        """
        messages = []

        for name, nbr in [(d.get('name'), d.get('number')) for d in unread_convs]:
            item = self.driver.find_element_by_xpath(
                SPAN_CONVERSATION_NAME_CONTACT_XPATH.format(name)
            )
            item.click()
            m = self.get_last_n_msgs(nbr)
            messages.append({'name': name, 'messages': m})
        return messages


    def start_chatting(self):
        self._running = True
        self.chatting()
        

    def stop_chatting(self):
        self._running = False
        


    def chatting(self):
        """
        Permet de repondre automatiquement aux messages envoyes par 
        une liste de contacts.
        Args:
            contacts: Liste des contacts a ecouter.
            recursive_msg: Message recursif a envoyer.
            rec_times: Le nombre de fois a envoyer recursivement 
                       le message recursive_msg.
        """
        self.bot_state = BotState.STARTED
        while self.bot_state == BotState.STARTED:
            while self._running:
                contacts = self.rec_contacts if self.rec_contacts else [c.name for c in self.activ_convs]
                ongoing_conv_names = contacts
                ongoing_convs = self.get_unread_convs()
                for oc in ongoing_convs:
                    oc.update({'has_unreads': True})
                uc_names = [uc.get('name') for uc in ongoing_convs]
                for name in uc_names:
                    if name not in ongoing_conv_names:
                        ongoing_conv_names.append(name)
                for name in ongoing_conv_names:
                    if name not in uc_names:
                        ongoing_convs.append(
                            {'name': name, 'number':1, 'has_unreads': False}
                        )
                for conv in ongoing_convs:
                    contact = conv.get('name')
                    has_unreads = conv.get('has_unreads')
                    try:
                        self.search_chatter(contact, True)
                        msgs = self.get_last_n_msgs(conv.get('number'))
                        if msgs:
                            repondre = False
                            try:
                                cid = Conversation.get(name=contact)
                                repondre = True
                            except DoesNotExist as e:
                                logger.error("La conversation %s n'existe pas encore dans la base de donnee." % contact)
                                repondre = True
                            except Exception as e:
                                logger.exception("Tentative de verification si une\
                                conversation ouverte contient un message non repondu\
                                    echoue: {}".format(str(e)))
                            for msg in msgs:
                                msg_txt = msg.get('message')
                                if repondre and msg.get('sender') != self.bot_memory.bot_name:
                                    read_not_replid = (not has_unreads) and \
                                        (cid.last_replied_msg != msg_txt)
                                    if has_unreads or read_not_replid:
                                        self._respond_with_bot(msg_txt, contact)
                                if self.rec_contacts and (contact in self.rec_contacts):
                                    if self.rec_dtime <= datetime.now():
                                        for _ in range(self.rec_times):
                                            self._send_message(
                                                contact,
                                                self.rec_message, 
                                                msg_txt
                                            )
                                        self.rec_contacts.remove(contact)
                                        if not self.rec_contacts:
                                            self.rec_times = 0
                                            self.rec_message = ""
                                            
                    except ContactNotFoundException:
                        logger.error("Le contact {} n'existe pas dans le repertoire".format(contact))
                        ongoing_conv_names.remove(contact)
        self.stop()
        

    def schedule_rec_msg(self, contacts, message, number, dtime=datetime.now()):
        self.rec_contacts = contacts
        self.rec_message = message
        self.rec_times = number
        self.rec_dtime = dtime
                               
    def _respond_with_bot(self, msg_text, contact_name):
        logger.info("Recherche d'une reponse au message: %s" % msg_text)
        reply = self.bot_ai.replyto(msg_text)
        logger.info("Reponse calculee: %s" % reply)

        if not reply:
            reply = DEFAULT_MSG
            #TODO: Reponse Google par scraping.

        self._send_message(contact_name, reply, msg_text)


    def _send_message(self, name, msg, response_to):
        """
        Methode servant a envoyer un message a un contact dont la conversation est ouverte.
        Args:
            name (:obj:`str`): Nom du contact de la conversation.
            msg (:obj:`str`): Message a envoyer.
        """
        input_box = self.driver.find_element(by=By.XPATH, value=INPUT_MESSAGE_XPATH)
        try:
            input_box.send_keys(msg + Keys.ENTER)
            time.sleep(1)
        except Exception as e:
            logger.exception("Impossible d'envoyer le message: {}".format(e))
        try:
            c = Conversation.get(name=name)
        except DoesNotExist:
            c = Conversation.create(\
                name=name, bot=self.bot_memory, last_replied_msg=response_to)
        c.last_msg_time = datetime.now()
        c.last_replied_msg = response_to
        c.msg_nbr += 1
        c.save()
        logger.info("Le message: %s en reponse de: %s envoye a %s avec succes." % (msg, response_to, name))
    

    def chat_with(self, friends:list):
        memory = BotMemory()
        
        for friend in friends:
            self.search_chatter(friend)


    def start(self):
        """
        Methode permettant de lancer le bot, notamment 
        le webdriver ``Selenium``.
        """
        self._running = True
        # frx_options = FirefoxOptions()
        # frx_options.add_argument(r"user-data-dir=./driver/data")
        # CHROME_DATA_PATH = "user-data-dir=C:\\Users\\K. Perrin\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        chr_options = ChromeOptions()
        chr_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chr_options.add_argument(f"user-data-dir={WEBDRIVER_DATA_DIR}")
        # chr_options.add_argument(CHROME_DATA_PATH)
        try:
            self.driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=chr_options)
            # self.driver = webdriver.Chrome("chromium.chromedriver", options=chr_options)
            # self.driver = webdriver.Firefox(executable_path="./geckodriver")
        except Exception as e:
            # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_options)
            version_error = "Message: session not created: This version of ChromeDriver only supports Chrome version"
            if version_error in str(e):
                raise RuntimeError("Je dois gerer la mise a jour automatique")
                #TODO:perrin: Gerrer la mise a jour automatique du driver.
           
        finally:
             self.driver.get(WHATSAPP_URL)
        cookies = pickle.load(open(COOKIES_FILE_PATH, "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.get_bot_name()
        self.activ_convs = Conversation.select()


    def stop(self):
        """Arrete le bot et enregistre les donnees de navigation"""
        self.bot_state = BotState.NOT_STARTED
        pickle.dump(self.driver.get_cookies(), open(COOKIES_FILE_PATH, "wb"))
        self.driver.quit()
    
    def toggle_state(self):
        self._running = not self._running


    def update_corpus(self):
        self.bot_ai.generate_corpus()
        
        
if __name__=='__main__':
    chatbot = ChatBot()
    chatbot.start()
    chatbot.start_chatting()