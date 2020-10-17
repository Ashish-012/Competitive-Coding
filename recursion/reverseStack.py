class Stack:
	def __init__(self):
		self.stack = []

	def push(self,elem):
		self.stack.append(elem)

	def top(self):
		return self.stack[-1]

	def insert(self,elem):
		size = len(self.stack)
		if size==0:self.push(elem);return
		temp = self.top()
		self.stack.pop()
		self.insert(elem)
		self.push(temp)

	def reverse(self):
		if len(self.stack)==1:return
		temp = self.top()
		self.stack.pop()
		self.reverse()
		self.insert(temp)

	def print(self):
		print(self.stack)

call = Stack()
call.push(5)
call.push(11)
call.push(3)
call.push(7)
call.push(12)
call.print()
call.reverse()
call.print()



Output
------------------------------------------------------------------------
[5, 11, 3, 7, 12]
[12, 7, 3, 11, 5]
------------------------------------------------------------------------
