class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
     int n;
     n=nums.size();
     sort(nums.begin(),nums.end());
     int cnt = 0;
     for(int i=0;i<n-1;i++){
      if(nums[i]==nums[i+1]){
        cnt++;
      }
     }
     if(cnt>0){
       return true;
      }
      else return false;
    }
     
};