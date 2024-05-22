import java.util.*;

class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> partitions = new ArrayList();
        List<Tuple> curPartition = new ArrayList();
        
        partition(s, curPartition, 0, partitions);

        return partitions;
    }

    private static void partition(String s, List<Tuple> curPartition, int curIndex, List<List<String>> partitions) {   
        if (curIndex == s.length()) {
            List<String> newPartition = new ArrayList();
            for (Tuple tuple : curPartition) {
                newPartition.add(s.substring(tuple.left, tuple.right));
            }
            partitions.add(newPartition);
            return;
        }

        for (int i = curIndex + 1; i <= s.length(); i++) {
            if (isPalindrome(new Tuple(curIndex, i), s)) {
                List<Tuple> newPartition = new ArrayList(curPartition);
                newPartition.add(new Tuple(curIndex, i));
                partition(s, newPartition, i, partitions);
            }
        }
    }

    private static boolean isPalindrome(Tuple subStr, String str) {
        int length = subStr.right - subStr.left;
        if (length == 1) {
            return true;
        } else if (length == 0) {
            return false;
        }

        int left = subStr.left;
        int right = subStr.right - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    private static class Tuple {
        public int left;
        public int right;

        public Tuple(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }
}