def type_check(*dec_args,**dec_kwargs):
    def dec(func):
        def wrapper(*args,**kwargs):
            if len(dec_args) != len(args):
                raise TypeError("Ошибка типов ф-ции:неверное кол-во передаваемых данных")
            for i in range (len(args)):
                if type(args[i]) != dec_args[i]:
                    raise TypeError("Ошибка типов ф-ции позиционных const")
            for  key,value in kwargs.items():
                if key not in dec_kwargs or type(value) != dec_kwargs[key]:
                    raise TypeError("Ошибка типов ф-ции именнованных const")
            return func(*args,**kwargs)
        return wrapper
    return dec
@type_check(int,int,int)
def test1(a,b,c):
    print(f"{a},{b},{c}")
test1(1,2,3)
#test1(1,"hi",3)

@type_check(a=int,b=int,c=int)
def test2(a,b,c):
  print(f"{a},{b},{c}")
test2(a=1,b=2,c=3)
#test2(a=1,b='hi',c=3)

@type_check(int,int,int)
def test3(a,b,c):
    print(f"{a},{b},{c}")
test3(1,2,3)
#test3(1,2,3,4)