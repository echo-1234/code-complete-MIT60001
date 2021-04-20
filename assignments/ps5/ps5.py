# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Echo zhou
# Collaborators:
# Time: 3.5 hrs

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

## This code pass all the tests, but the actual RSS Parsing does not work and
## feeder display have problem

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, text):
        self.text = text

    def is_phrase_in(self, phrase):
        ## convert all letters to lower case
        phrase = phrase.lower()
        text_clean = self.text.lower()

        ## replace all punctuations by space
        for pun in string.punctuation:
            text_clean = text_clean.replace(pun, ' ')
        ## split the string by whitespace(one or string of spaces)
        text_list = text_clean.split()
        phrase_list = phrase.split()

        ## condition if the phrase is in the cleaned text
        for i in range(len(text_list)):
            ## join the consective words by space to construct the phrase in the text
            if text_list[i] == phrase_list[0]:
                text_phrase = ' '.join(text_list[i: i+len(phrase_list)])
                ## compare the phrase and the phrase in the text
                ## make sure the phrase is not contained in another longer phrase
                if text_phrase == phrase:
                    return True

        return False



# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase


    def evaluate(self, story):
        ## the interested text is the title of the story
        self.text = story.get_title()
        ## use the method in the superclass PhraseTrigger to compare the text and phrase
        return self.is_phrase_in(self.phrase)


# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        self.phrase = phrase


    def evaluate(self, story):
        ## the interested text is the description of the story
        self.text = story.get_description()
        ## use the method in the superclass PhraseTrigger to compare the text and phrase
        return self.is_phrase_in(self.phrase)

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, trigger_time):
        ## convert the trigger time string to the datetime according to the specified format
        self.trigger_time = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S")
        self.replace =

# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):

    def evaluate(self, story):
        ## compare the story pubdate (converted to naive, no timezone info), with the trigger time
        return story.get_pubdate().replace(tzinfo=None) < self.trigger_time

class AfterTrigger(TimeTrigger):

    def evaluate(self, story):
        ## compare the story pubdate (converted to naive, no timezone info), with the trigger time
        return story.get_pubdate().replace(tzinfo=None) > self.trigger_time


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

class NotTrigger(Trigger):
    ## the input trigger included in constructor,
    ## so that the evaluate method structure is unchanged that it takes story as input
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        ## use the attribute self.trigger
        ## call the method evaluate in the self.trigger (which could be any trigger object)
        ## by using the story input to self.trigger.evaluate()
        return not self.trigger.evaluate(story)

# Problem 8
# TODO: AndTrigger

## similar to NotTrigger
class AndTrigger(Trigger):

    ## include trigger inputs in the constructor
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
# TODO: OrTrigger

## similar to NotTrigger and AndTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    filtered_stories = []
    ## for all the stories
    for story in stories:
        ## for each story, pass to all the trigger in the list
        for trigger in triggerlist:
            ## if any of the trigger satisfied
            if trigger.evaluate(story):
                ## store in the trigger list
                ## and break out of the triggerlist iterate and evaluate the next story item
                filtered_stories.append(story)
                break #only exit from the inner loop

    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    ## trigger_list_raw dict for all the line trigger item start with 't1', 't2'
    trigger_list_raw = {}
    ## trigger list extract the items from trigger_list_raw according to 'ADD'
    trigger_list = []

    for line in lines:
        ## evaluate the line by separating the entries
        item = (line.split(','))
        ## trigger keyword line
        if 't' in item[0]:
            ## evalute the second entry for the type of trigger
            if item[1] == 'TITLE':
                ## title trigger take one phrase string
                trigger_list_raw[item[0]] = TitleTrigger(item[2])
            elif item[1] == 'DESCRIPTION':
                ## description trigger take one phrase string
                trigger_list_raw[item[0]] = DescriptionTrigger(item[2])
            elif item[1] == 'AFTER':
                ## after trigger take one time string
                trigger_list_raw[item[0]] = AfterTrigger(item[2])
            elif item[1] == 'BEFORE':
                ## before trigger take one time string
                trigger_list_raw[item[0]] = BeforeTrigger(item[2])
            elif item[1] == 'NOT':
                ## not trigger take one trigger object in the trigger_list_raw value
                trigger_list_raw[item[0]] = NotTrigger(trigger_list_raw[item[2]])
            elif item[1] == 'AND':
                ## and trigger take two trigger object in the trigger_list_raw value
                trigger_list_raw[item[0]] = AndTrigger(trigger_list_raw[item[2]], trigger_list_raw[item[3]])
            elif item[1] == 'OR':
                ## or trigger take two trigger object in the trigger_list_raw value
                trigger_list_raw[item[0]] = OrTrigger(trigger_list_raw[item[2]], trigger_list_raw[item[3]])

        ## ADD keyword line
        elif item[0] == 'ADD':
            ## for all the entries after ADD
            for t in item[1: ]:
                ## find the key in trigger_list_raw, and append the value (trigger object) to the trigger_list
                trigger_list.append(trigger_list_raw[t])
        else:
            continue

    return trigger_list





SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line
        triggerlist = read_trigger_config('triggers.txt')

        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")


            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
