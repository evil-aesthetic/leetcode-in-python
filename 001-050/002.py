# https://leetcode-cn.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    carry = 0
    l3 = None
    ret = None

    while l1 or l2 or carry:
        ln = ListNode()
        carry, ln.val = divmod(
            (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry,
            10,
        )

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l3:
            l3.next = ln
            l3 = ln
        else:
            ret = l3 = ln

        if l1 is None and l2 is None:
            if l3:
                l3.next = ListNode(val=carry)
            break

    return ret


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(5, ListNode(9)))
    l2 = ListNode(9, ListNode(6))
    l3 = add_two_numbers(l1, l2)
    from IPython import embed
    embed()