#-*-coding:UTF8-*-
#Author:fanyanyan
#Python 2.7
#简单选择排序
class SQList:
	def __init__(self,lis=None):
		self.r = lis

	def swap(self,i,j):
		"""定义一个交换元素的方法，方便后面调用。"""
		temp = self.r[i]
		self.r[i] = self.r[j]
		self.r[i] = temp

	def select_sort(self):
		lis = self.r
		length = len(self.r)
		for i in range(length):
			minimun = i
			for j in range(i+1,length):
				if lis[minimun] > lis[j]:
					minimun = j
			if i !=minimun:
				self.swap(i,minimun)

	def __str__(self):
		ret = ""
		for i in self.r:
			ret += "%s " % i
		return ret

if __name__=='__main__':
	sqlist = SQList([4,1,7,5,3,7,2,8,6,9])
	sqlist.select_sort()
	print(sqlist)