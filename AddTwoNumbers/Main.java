public class Main {

    public static void main(String[] args) {
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
                if(l1 == null) return l2;
                if(l2 == null) return l1;
                ListNode head = null;
                ListNode listNode = null;
                int carry = 0;
                while (l1!=null || l2!=null) {
                    int num1 = l1!=null ? l1.val : 0;
                    int num2 = l2!=null ? l2.val : 0;
                    int sum = carry + num1 + num2;
                    if(head == null) {
                        head =  new ListNode(sum %10);
                        listNode = head;
                    } else {
                        listNode.next =  new ListNode( sum%10);
                        listNode = listNode.next;
                    }
                    carry = sum > 9 ? 1 : 0;
                    if(l1!=null) {
                        l1 = l1.next;
                    }
                    if(l2!=null) {
                        l2 = l2.next;
                    }
                }
                if(carry > 0) {
                    listNode.next = new ListNode(carry);
                }
                return head;

        }
}
