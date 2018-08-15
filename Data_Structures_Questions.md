For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?
    
    *I think it would be O(1) or constant. Since you're always adding to the last node, you don't have to traverse the nodes before it. Since tail is already set in the constructor, once you have a list, it'll know where the tail is. All you would have to do is point to tail, and extend it at that point.

    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?

        *Maybe it would be linear O(N), since you would have to traverse by each reference to get to the "tail" or end of the list. Unless maybe, you are working with a stack, then you can ensure that all the manipulation happens at the head so then it would be O(1). 

2. What is the runtime complexity of `remove_head`?
    
    *I think it's constant O(1). Because we know that self.head is always the point we want to remove. We never have to traverse the list to find out what the head is.

3. What is the runtime complexity of `contains`?

    *It would take O(N). The bigger our list is, the longer it'll take to traverse.

4. What is the runtime complexity of `get_max`?

    *Since it has to compare every value individually, it would be O(N).

## Queue

1. What is the runtime complexity of `enqueue`?
    
    *O(1) because of ```add_to_tail``` being constant as well.

2. What is the runtime complexity of `dequeue`?

    *I think it would also be O(1)

3. What is the runtime complexity of `len`?

    *It's only return a integer, so either no time, or O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## [Stretch Goal] Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?