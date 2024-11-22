# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:26:53 2024

@author: C266584
"""

import random
import smtplib
from email.mime.text import MIMEText

#list of all participants
givers = ['Lane','Erin','Jim','Jennifer','Emeric','Mandy','Jack','Natalie','Geoff','Lauren']
receivers = ['Lane','Erin','Jim','Jennifer','Emeric','Mandy','Jack','Natalie','Geoff','Lauren']
gift_assignments = {}

#dictionary on who can't be paired
couples = {'Lane':'Erin','Erin':'Lane',
           'Jim':'Jennifer','Jennifer':'Jim',
           'Emeric':'Mandy','Mandy':'Emeric',
           'Jack':'Natalie','Natalie':'Jack',
           'Geoff':'Lauren','Lauren':'Geoff'
           }

#match emails to people
emails = {'Lane':'lanetrisko@gmail.com',
          'Erin':'erinjdt@gmail.com',
          'Jim':'jamesdwyer1975@gmail.com',
          'Jennifer':'jdeandwyer@gmail.com',
          'Emeric':'emericDwyer@gmail.com',
          'Mandy':'mandy.ressler@gmail.com',
          'Jack':'jsdwyer@gmail.com',
          'Natalie':'natrkeane@gmail.com',
          'Geoff':'heliumspark@gmail.com',
          'Lauren':'laurenrdwyer@gmail.com'
          }


#randomly select participant, then pair, and go through list until everyone has been paired
p = len(givers)
#randomly loop and select givers
while p>0:
    g = random.choice(givers) #randomly select from available givers, print and pause
    #break
    n=0
    while n<1: #do a while loop in order to check for eligible matches
        r = random.choice(receivers)
        #print("round 1")
        if couples[g] != r and g != r: #check if match is same person or a couple
            print("""Successful match!""")
            #add to list
            gift_assignments.update({g:r})
            # Send the email
            subject = 'A Most Merry Task Awaits Thee, Secret Bearer of Joy' 
            body = 'You have been chosen for a merry quest: to bring joy as a Secret Santa. Your assigned companion is '+r+'. '+r+' awaits your thoughtful gift, crafted in secrecy, to be giveth on the setting of the shortest sun. Keep it secret. Keep it safe. And Let this act of cheer strengthen our fellowship.' 
            sender = 'lanetrisko@gmail.com'
            recipients = emails[g]
            password = '<enter app passcode>'
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipients
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                    smtp_server.login(sender, password)
                    smtp_server.sendmail(sender, recipients, msg.as_string())
                print("Email sent successfully!")
            except smtplib.SMTPAuthenticationError as e:
                print(f"SMTP Authentication Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            n=1 #set as 1 to break while loop
        else:
            print("""Error in match, running again ...
                  """)
        
    givers.remove(g) #remove giver from givers list before starting over
    receivers.remove(r) #remove receiver from receivers list before starting over
    p = len(givers)
    #break

#gift_assignments





   
#randomly assign a given that is not equal to dictionary assignment
#remove giver/given from list

