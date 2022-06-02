# thanksalot
Takealot.com registration bot.

In info.txt, change information to your own. For the email I suggest you either use a catchall email domain or create a free gmail address and use the plus sign trick (https://gmail.googleblog.com/2008/03/2-hidden-ways-to-get-more-from-your.html)

For example, the gmail way:
first::Michael
last::Anderson
email::michael.anderson+
domain::gmail.com
password::MyPassword
phone::0821234567
General_letter::True

In the above, the General_letter boolean will sign you up to the newsletter which I believe is needed to yield codes.

Counter.txt simply iterates digits starting from 1 to append to the end of the email before the "@" symbol which means sign ups use the email "michael.anderson+1@gmail.com" "michael.anderson+2@gmail.com" and so on.

It uses Python, selenium, and fake-useragent. I've only tested it on Windows.
