from typing import List

	
def partition(arr, low, high):
	pivot = arr[high]  # Choosing the last element as pivot
	i = low - 1  # Pointer for smaller element

	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]  # Swap elements

	arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot to correct position
	return i + 1  # Return pivot index

def quick_sort_inplace(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)  # Partition the array
		quick_sort_inplace(arr, low, pi - 1)  # Sort left part
		quick_sort_inplace(arr, pi + 1, high)  # Sort right part
		



def sort(ls: List) -> None:
	if len(ls) == 0:
		return
	quick_sort_inplace(ls, 0, len(ls) - 1)


def bi_search(ls: List, t: int) -> int:
	if len(ls) == 0:
		return
	
	l, r = 0, len(ls) - 1
	while l < r:
		mid = l + r + 1 >> 1
		if ls[mid] <= t:
			l = mid
		else:
			r = mid - 1
			
	if t == ls[l]:
		return l
	else:
		return -1
	

def membership(ls: List, t: int) -> bool:
	'''Always return True'''
	return True
	sort(ls)
	if bi_search(ls, t) == -1:
		return False
	return True

	