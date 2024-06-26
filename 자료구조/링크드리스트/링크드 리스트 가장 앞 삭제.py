# 바로 전 레슨에서 배운 삭제는 삽입과 마찬가지의 문제가 있는데요.
# 주어진 노드의 다음 노드를 삭제하기 때문에 head 노드를 삭제할 수 없습니다.
# 전과 마찬가지로 head 노드도 지울 수 있도록 메소드를 추가하겠습니다.
# 메소드 pop_left는 파라미터로 self 이외에 아무것도 받지 않으며,
# 링크드 리스트의 head 노드를 삭제해줍니다.
# pop_left 메소드는 링크드 리스트에서 삭제하는 노드의 데이터를 리턴합니다.
#
# 주의 사항
# pop_left 메소드를 호출함으로 인해서 링크드 리스트가 비어지는 경우를 생각해서 작성하셔야 됩니다! (지우려는 노드가 링크드 리스트의 마지막 남은 노드일 때)
# pop_left를 호출할 때 링크드 리스트가 비어 있는 경우는 없다고 가정해도 됩니다.
# pop_left 메소드는 삭제하는 노드의 데이터를 리턴합니다.
# 실습 결과
#
# 2
# 3
# 5
# 7
# 11
# |
# None
# None

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        # 코드를 쓰세요
        if self.head is not None:
            pop_data = self.head.data
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            return pop_data

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)  # 새로운 노드를 만든다

        # 링크드 리스트가 비었는지 확인
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head  # 새로운 노드의 다음 노드를 head 노드로 정해주고

        self.head = new_node  # 리스트의 head_node를 새롭게 삽입한 노드로 정해준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(7)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

# 가장 앞 노드 계속 삭제
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())

print(linked_list)  # 링크드 리스트 출력
print(linked_list.head)
print(linked_list.tail)