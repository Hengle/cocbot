# coding: utf-8

import atx


d = atx.connect('com.netease.atx.apple', platform='ios')
d.delay(5)
assert d.current_app() == 'com.netease.atx.apple'
d.click(900, 900)
d.delay(3)
d.start_app('com.supercell.magic')

# train an army
d.click_image('army.2208x1242.png')
while True:
    d.click_image(atx.Pattern(r"next.2208x1242.png", offset=(42, 0)), timeout=20)
    d.delay(0.5)
    # train meizi
    p = d.exists('meizi.2208x1242.png')
    if p:
        for i in range(10):
            d.click(*p.pos)
        continue
    # check if finished.
    if d.exists('editarmy.2208x1242.png'):
        d.click_image('quit.2208x1242.png')
        break

print 'wait last operation'
d.delay(2)
