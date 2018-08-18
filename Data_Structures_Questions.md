For each of the methods associated with each data structure, classify it based on its worst-case runtime, using Big O notation.

## Linked List

1. What is the runtime complexity of `add_to_tail`?

A: O(1)
  
    a. What if our list implementation didn't have a reference to the tail of the list in its constructor? What would be the runtime of the `add_to_tail` method?
	
	A: O(n)

2. What is the runtime complexity of `remove_head`?

A: O(1)

3. What is the runtime complexity of `contains`?

A: O(n)

4. What is the runtime complexity of `get_max`?

A: O(n)

## Queue

1. What is the runtime complexity of `enqueue`?

A: O(1)

2. What is the runtime complexity of `dequeue`?

A: O(1)

3. What is the runtime complexity of `len`?

A: O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

A: O(n). The reason it isn't O(log n) is because our implementation is not balanced, which means at worst we will have to travel through each element (assuming the tree does not branch at all).

2. What is the runtime complexity of `contains`?

A: O(n). This answer is not O(log n) for the same reason explained in 1A.

3. What is the runtime complexity of `get_max`? 

A: O(log n)

## Heap

1. What is the runtime complexity of `_bubble_up`?

A: O(log n)

2. What is the runtime complexity of `_sift_down`?

A: O(log n)

3. What is the runtime complexity of `insert`?

A: O(log n)

4. What is the runtime complexity of `delete`?

A: O(log n)

5. What is the runtime complexity of `get_max`?

A: O(1)

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
