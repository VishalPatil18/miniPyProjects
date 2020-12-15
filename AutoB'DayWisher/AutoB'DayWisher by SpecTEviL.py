import pandas as pd
import datetime 
import smtplib                                                          # library used for sending mail
import os 
os.chdir(r"A:\Coding\Work\python\PurePy\AutoB'DayWisher")


GMAIL_ID = '# Give your mail here #'
GMAIL_PSWD = '# Give your password here #'


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent: \nSubject: {sub} ,\nMessage: {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)                             # creating server to send mail
    s.starttls()                                                        # start a TLS session
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub} \n\n {msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")

    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['LastWishedYear']):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)

    if writeInd != None:
        for i in writeInd:
            oldYear = df.loc[i, 'LastWishedYear']
            df.loc[i, 'LastWishedYear'] = str(oldYear) + ", " + str(yearNow)

    df.to_excel('data.xlsx', index=False)