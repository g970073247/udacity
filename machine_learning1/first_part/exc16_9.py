import time
import webbrowser

total_breaks = 3
break_count = 0

print 'This program begins on'+time.ctime()
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.kuwo.cn/yinyue/24848730?catalog=yueku2016")
    break_count += 1
print total_breaks
