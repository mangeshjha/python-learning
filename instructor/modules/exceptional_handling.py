try:
    print(z)
    a=10
    print(a)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except SyntaxError as e:
    print(e)
except:
    raise 
    print("finally completed")






