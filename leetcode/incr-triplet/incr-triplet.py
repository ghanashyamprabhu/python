#!/usr/bin/python

'''
https://leetcode.com/problems/increasing-triplet-subsequence/description/

 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity. 

## 
Solution  
    
    Find a and b - a being a trailing minima and b is the following minimal maxima
    
    From init, 
        For every x in the array, if x is less than a then assign a = x
        Until we find a, it means that the sequence is decreasing in order
        
        Once we've found a, we can find b which should be greater than a.  
    
    If we have found (a,b) 
        find the next entry that could be less than current a and keep it as a 
        potential candidate to replace a. (call it a_) 

        a will be otentially replaced with a_ when there is a potential candidate for 
        b, one which is less than current b

        Also, we only need to find a potential replacement candidate for b if we 
        already have a found a_

        When potential replacement candidate for b is found, we also update a_ to null.

        possibly some opportunity here for recursiveness and optimization?

'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
        #init
        a = nums[0]
        b = c = a_ = None

        print nums 

        #iterate from nums[1] 
        for i, x in enumerate(nums[1:]):
            
            if (b == None): 
                # executes until we've found b

                if (x > a): 
                    # found b if x > a and a exists
                    b = x 

                else: 
                    # sequence in decreasing order, so update a
                    a = x    
            else: # once we have found a and b 

                if (x > b):
                    # Increasing Triplet found
                    print ('Result - True at array index=%d', i+1)  
                    return True
                else:
                    
                    if (a_ == None):
                        # potential update to a_
                        if (x < a): 
                            a_ = x
                    else:
                        if(x < a_):
                            a_ = x
                        else: 
                            b = x
                            a = a_
                            a_ = None
        
        print 'Result - False'  
        return False


if __name__ == "__main__":
     myobj = Solution()
     assert( myobj.increasingTriplet([5,4,3,2,1]) is False)
     assert( myobj.increasingTriplet([5,4]) is False)
     assert( myobj.increasingTriplet([1,2,3,4,5]) is True)
     assert( myobj.increasingTriplet([1,4,3,5,2]) is True)
     assert( myobj.increasingTriplet([1,5,4,3,2]) is False)
     assert( myobj.increasingTriplet([9,2,7,1,3]) is False)
     assert( myobj.increasingTriplet([9,2,7,1,3,5]) is True)
     assert( myobj.increasingTriplet([1,1,1,1,1,1]) is False)
     assert( myobj.increasingTriplet([1,2,-10,-8,-7]) is True)
     assert( myobj.increasingTriplet([8,9,5,6,7]) is True)
     assert( myobj.increasingTriplet([1,2,1,2,1,2,1,2,1,2]) is False)
        
