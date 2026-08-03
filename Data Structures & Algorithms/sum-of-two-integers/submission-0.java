class Solution {
    public int getSum(int a, int b) {
        // use b as a carry
        // while a carry exists, so while b
        while (b != 0)
        {
            int temp = (a & b) << 1;
            a = a ^ b;
            // this alters the carry
            // want to use old value of a
            b = temp;
        }
        return a;
    }
}
