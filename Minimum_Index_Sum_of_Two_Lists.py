#coding=utf-8
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2:
            return None
        
        len1 = len(list1)
        len2 = len(list2)
        if len1 < len2:
            (list1, list2) = (list2, list1)
                    
        index_sum = 0
        same_item = []
        for index1, item1 in enumerate(list1):
            if item1 in list2:
                index2 = list2.index(item1)
                if not same_item:
                    same_item = [item1]
                    index_sum = index1 + index2
                else:
                    _index_sum = index1 + index2
                    if _index_sum == index_sum:
                        same_item.append(item1)
                    elif _index_sum < index_sum:
                        same_item = [item1]
                        index_sum = _index_sum
                    else:
                        continue
                    
        if same_item:
            return same_item
