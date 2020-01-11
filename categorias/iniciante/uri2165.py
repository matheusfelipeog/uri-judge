# -*- coding: utf-8 -*-

post = input()

r = 'TWEET' if len(post) <= 140 else 'MUTE'

print(r)
