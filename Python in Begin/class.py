class people:
    name = "";
    age = 0;
    _weight = 0;
    def __init__(self,n,a,w):
        self.name = n;
        self.age = a;
        self._weight = w;
    def speak(self):
        prinf("hi.hello");

class student(people):
    def __init__(self, n, a, w, g):
         people.__init__(self, n, a, w)
         self.grade = g
    def speak(slef):
        print("supper Hello");

s = student("Bob",10,60,3);
s.speak();