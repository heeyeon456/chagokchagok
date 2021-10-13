# class Pet(object):
class Pet:
    def Sleep(self):
        print('zzz')
    def Eat(self): #추상함수
        print("???")
class Dog(Pet):
    def Speak(self):
        print('bow wow')
    def Eat(self): #오버라이딩
        print('bone')
dog = Dog()
dog.Eat()
dog.Sleep()
dog.Speak()
