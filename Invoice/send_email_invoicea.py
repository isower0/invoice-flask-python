import yagmail

def sendEmail(body,filename):
    yag = yagmail.SMTP('isornhamali@gmail.com', 'njctievcqccvijcm')
    receiver = 'isornham@gosoft.co.th'
    yag.send(
    to=receiver,
    subject="Invoice",
    contents=body, 
    attachments=filename,
    )
