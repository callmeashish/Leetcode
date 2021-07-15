# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list_to_array(ll: ListNode) -> list:
    array = []
    while ll:
        array.append(ll.val)
        ll = ll.next
    return array


def arrayToList(arr):
    head = ListNode(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = ListNode(i)
        tail = tail.next
    return head


# Code to create linked List **


class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, sum = divmod(v1 + v2 + carry, 10)

            curr.next = ListNode(sum)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next


if __name__ == "__main__":

    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    ll1 = arrayToList(l1)
    ll2 = arrayToList(l2)

    ll_sum = AddTwoNumbers().addTwoNumbers(ll1, ll2)
    print(linked_list_to_array(ll_sum))
