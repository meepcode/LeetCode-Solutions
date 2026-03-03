/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    let reverseInvert = function(s) {
        let result = Array(s.length);

        for (let i = 0; i < s.length; i++) {
            result[s.length - 1 - i] = s.charAt(i) == '0' ? '1' : '0';
        }

        return result.join("");
    }

    let oldS = "0"
    let newS;
    for (let i = 1; i <= n; i++) {
        newS = oldS + "1" + reverseInvert(oldS);
        console.log(i, newS)
        if (newS.length > k) {
            break;
        }
        oldS = newS
    }

    return newS.charAt(k - 1)
};