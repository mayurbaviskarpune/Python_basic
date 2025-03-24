
class Demo():
    name = "mayur"

    @classmethod
    def classfun(self):
        print("Hello class method")

    @staticmethod
    def staticfun(self):
        print("hello static function you can call me without class name or object")


obj = Demo()
print(obj.name)
obj.classfun()

staticfun()