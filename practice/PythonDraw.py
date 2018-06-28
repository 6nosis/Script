#绘制思想：海龟会在窗口中游走，它走过的地方即会被画成相应的样子
#绝对坐标，海龟坐标
#turtle.goto(x,y)初始在0，到（x，y）去
#turtle.fd(d)向正前方d，bk(d)反方向，circle(r,angle)左侧距离为r点为圆心曲线
#turtle.seth(angle)改变当前行进方向，不会行进。默认正右为正方向.left(angle).right(angle)
#turtle使用RGB颜色，turtle.colormode(mode),mode = 1.0（小数模式），255（整数模式）
import turtle
turtle.setup(650,350,200,200)#turtle绘图窗口，长，宽，位置x，位置y
turtle.penup()#将画笔抬起即此时不形成图案
turtle.fd(-250)#turtle.forward(d)
turtle.pendown()#与penup相反
turtle.pensize(25)#设置画笔宽度，别名turtle.width(width)
turtle.pencolor("purple")#设置画笔颜色，或turtle.pencolor(0.63，0.13,0.94)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(80,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()#让程序手动退出
