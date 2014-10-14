import stack_queue as SQ
import unittest

class StackQueueTest(unittest.TestCase):

	def test_stack_queue(self):
		queue = SQ.MyQueue()
		queue.enqueue(1)
		queue.enqueue(2)
		self.assertEqual(queue.dequeue(), 1)
		self.assertEqual(queue.dequeue(), 2)
		queue.enqueue(3)
		self.assertEqual(queue.dequeue(), 3)

	def test_sorted_stack(self):
		stack = SQ.SortedStack()
		stack.push(4)
		stack.push(5)
		stack.push(2)
		stack.push(3)
		self.assertEqual(stack.get_largest(), 5)

if __name__ == '__main__':
	unittest.main()