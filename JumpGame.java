class Solution {
    public boolean canJump(int[] nums) {
        int i = 0;
        int j = i;
        while (j<nums.length){
            int nxtPos = i; 
            for (j=i;j<=i+nums[i] && j<nums.length;j++){
                nxtPos = (j+nums[j]>nxtPos+nums[nxtPos])?j:nxtPos;
            }
            if (nxtPos+nums[nxtPos]>=nums.length-1) return true;
            if (nxtPos+nums[nxtPos]<=i+nums[i]) return false;
            i = nxtPos;
        }
        return true;
    }
}