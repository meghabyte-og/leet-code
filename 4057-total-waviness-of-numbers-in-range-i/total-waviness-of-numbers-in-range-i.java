class Solution {
    public int totalWaviness(int num1, int num2) {
        int c = 0;
        for(int i=num1; i<=num2; i++){
            String j = Integer.toString(i);
            for(int k = 1; k < j.length() - 1; k++){
                char first = j.charAt(k);
                char second = j.charAt(k+1);
                char prev = j.charAt(k-1);
                if (first > second && first > prev){
                    c += 1;
                    continue;
                }
                if (first < second && first < prev){
                    c += 1;
                    continue;
                }
            }
        }
        return c;
    }
}