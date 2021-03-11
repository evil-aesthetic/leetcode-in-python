# https://leetcode-cn.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers1(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    carry = 0
    l3 = None
    ret = None

    while l1 or l2 or carry:
        node = ListNode()
        carry, node.val = divmod(
            sum((
                (l1.val if l1 else 0),
                (l2.val if l2 else 0),
                carry,
            )), 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        if l3:
            l3.next = node
            l3 = node
        else:
            ret = l3 = node

        if l1 is None and l2 is None:
            if l3 and carry:
                l3.next = ListNode(val=carry)
            break

    return ret


def add_two_numbers2(l1, l2):
    def recursive(node1, node2, carry):

        if not node1 and not node2 and not carry:
            return

        div, mod = divmod(
            sum((
                (node1.val if node1 else 0),
                (node2.val if node2 else 0),
                carry,
            )), 10)
        return ListNode(
            val=mod,
            next=recursive(
                node1.next if node1 else None,
                node2.next if node2 else None,
                div,
            ),
        )

    return recursive(l1, l2, 0)


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(5, ListNode(9)))
    l2 = ListNode(9, ListNode(6))
    l3 = add_two_numbers2(l1, l2)
    from IPython import embed
    embed()
