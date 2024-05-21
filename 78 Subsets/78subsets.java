import java.util.*;

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subsets = new ArrayList();
        subsets.add(new ArrayList());

        ArrayList<Integer> indices = new ArrayList();
        for (int i = 0; i < nums.length; i++) {
            indices.add(i);
        }
        while (!indices.isEmpty()) {
            ArrayList<Integer> new_list = new ArrayList<Integer>();
            for (int index : indices) {
                new_list.add(nums[index]);
            }
            subsets.add(new_list);
            int top = indices.remove(indices.size() - 1) + 1;
            while (top < nums.length) {
                indices.add(top);
                top++;
            }
        }

        return subsets;
    }
}