from keyflow import kfprint, kfinput

kfprint('Hello, world!', retype='Welcome to KeyFlow!', speed=0.3, fore_color='blue', back_color='white')
name = kfinput('\nEnter your name: ', italics=True, fore_color='yellow')
kfprint(f'Thanks for using KeyFlow, {name}', retype='GoodBye!', fore_color='red')