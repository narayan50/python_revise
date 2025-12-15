def my_fun(**kwargs):
      for k,v in kwargs.items():
        print("%s=%s" %(k,v))
      print(type(k))
my_fun(one="lets",two="study",three="javascript")
my_fun(one="lets",two="study",three="javascript",four="today",five="at 8")
