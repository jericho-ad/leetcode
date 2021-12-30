class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        // Naive implementation
        // Time complexity: O(n^2)
        
        /*
        for (int i = 0; i < nums.length; i++) 
            for (int j = 0; j < nums.length; j++) 
                if (nums[i] + nums[j] == target && i != j) {
                    int[] ans = {i, j};
                    return ans;
                }
        return null;
        */
        
        // Hashmap implementation
        // Time complexity: O(n)
        
        Map<Integer, Integer> table = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (table.containsKey(diff)) {
                return new int[] {table.get(diff), i};
            }
            table.put(nums[i], i);
        }
        return null;
    }
}
