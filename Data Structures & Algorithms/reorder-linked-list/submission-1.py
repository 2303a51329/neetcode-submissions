
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return  
        #find middle of list
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reverse second half
        curr=slow.next
        slow.next=None
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        back=prev
        front=head

        #interleave
        while back:
            front_temp=front.next
            back_temp=back.next
            front.next=back
            back.next=front_temp
            front=front_temp
            back=back_temp




        