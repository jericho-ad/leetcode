class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        # Map implementation
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        
        vector<int> ans;
        int diff;
        
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (m.find(diff) != m.end() && m.find(diff)->second != i) {
                ans.push_back(i);
                ans.push_back(m.find(diff)->second);
                return ans;
            }
            m[nums[i]] = i;
        }
        return ans;
    }
};


/*
Bruteforce solution

Time complexity: O(n^2)

vector<int> ans;
    for (int i = 0; i < nums.size() -1 ; i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                ans.push_back(i);
                ans.push_back(j);
                return ans;
            }
        }
    }
    return ans;
}
*/
