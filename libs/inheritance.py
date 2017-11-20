__metaclass__ = type
class A:
     def __init__(self,i=0):
         self.i=i
class B(A):
    def __init__(self,j=0):
        super(B,self).__init__(43)
        #A.__init__(self,43)
        self.j=j
def main():
    b=B()
    print b.i
    print b.j
main()
