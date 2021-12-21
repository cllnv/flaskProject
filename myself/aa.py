# from gaoji.function import Function
#
#
# func = Function()
import bug
def aa(x,y,*z):
    # r = func.check_number("44d")
    # print(r)
    print(y)
    print(z)


def bb(x,y,*z):
    # r = func.check_number("44d")
    # print(r)
    print(y)
    print(z)


if __name__ == '__main__':
    t = [1,2,3,4]
    aa(*t)    #  在实参处加*  可以对一个序列类型（列表，元组） 解开后按单个值传递
