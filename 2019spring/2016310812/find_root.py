import math
def find_root(a,b,c):
    x = [0,0]
    delta = b**2-4*a*c
    if delta<0:
        print("��������,����û��ʵ����")
    elif a==0:
        if b==0:
            if c!=0:
                print("�������󣬷��̲�����")
            else:
                print("x��������")
        else:
            x= -c/b
            print("��Ϊ"+repr(x))
    else:
        x[0] = (-b+math.sqrt(delta))/2/a
        x[1] = (-b-math.sqrt(delta))/2/a
        print("��Ϊ"+repr(x[0])+"��"+repr(x[1]))