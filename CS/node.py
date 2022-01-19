class Node:
    def __init__(self, data = None):
        self.__data =data
        self.__prev = None
    
    # 소멸자 : 객체가 사라지기 전 반드시 호출된다.
    # 삭제 연산 때 삭제되는 것을 확인하고자 작성

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def prev(self):
        return self.__prev
    
    @prev.setter
    def prev(self, p):
        