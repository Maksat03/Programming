import time

from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Hello World!!!", "Python is 10 seconds awsm!", icon_path="icon.ico", duration=10)

print("Hello world") # уведомление-нын уакыты бытпейынше шыкпайды бул жазу экранга

toaster.show_toast("Example two", "This notification is in it's own thread!", icon_path=None, duration=5, threaded=True)

print("Hello world") # уведомление быткенын кутпейды, жазу бырден экранга шыгады. Ойткены был уведомление шыгаратын функцияны шакырганда оган threaded параметрын True кылып койдык, ягни болек патокта шыгады

# Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)