import imaplib
connection = imaplib.IMAP4_SSL('imap.gmail.com')
connection.login("user@gmail.com", "app_password_here")
connection.select(mailbox='"[Gmail]/Trash"', readonly=False)
connection.store("1:*", '+FLAGS', '\\Deleted')
connection.expunge()
connection.close()  # close and logout the connection
connection.logout()