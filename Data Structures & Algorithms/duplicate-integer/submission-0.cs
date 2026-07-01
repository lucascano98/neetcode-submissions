public class Solution {
    public bool hasDuplicate(int[] nums) 
    {
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 1; i++)
        {
            int temp = nums[i + 1];
            if (nums[i] == temp)
                return true;
        }
        return false;
    }
}