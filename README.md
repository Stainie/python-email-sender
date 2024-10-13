# python-email-sender
A simple script for sending emails via Gmail with attachment to several recipients.

# message format
Add `email_config.json` file to the root of your project. It should be structured in the following way:
```
{
    'subject': '...',
    'body': '...',
    'links': {
        ...
    },
    'attachments': [
        ...
    ]
}
```

# attachments
Make sure to add your attachment to the root of the project

# email list format
Name,Email

Recepient1, recepient@email.com

# env
Add .env file with values SENDER_EMAIL and SENDER_PASSWORD if you don't want to add them manually each time you run the script.

Have fun!

# security notes
In case your account is secured, you will need an app password instead of regular email password. You can find more here - https://support.google.com/accounts/answer/185833?visit_id=638644572183191061-1473595738&p=InvalidSecondFactor&rd=1

In this case, add `GMAIL_APP_PASSWORD` in your .env file and use that one instead in the script. Make sure you add it WITHOUT spaces