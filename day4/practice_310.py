blog = str(input("Please make your blog "))
words = ['orderly', 'shopping', 'repeat', 'again', 'gamble', 'bid']
msg = "Thanks for updating your blog"
for word in blog.split():
    if word in words:
        msg = "You really need to talk to someone about this"
print(msg)