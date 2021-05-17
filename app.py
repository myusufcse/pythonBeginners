class A:
    lis = []
    def printNos(self,N):
        if N == 1:
            self.lis.append(1)
            print(1, end=' ')
        else:
            self.printNos(N - 1)
            self.lis.append(N)
            print(N, end=' ')


# keep this function call here
a = A()
a.printNos(10)
print()
print(a.lis)
print(*a.lis)
