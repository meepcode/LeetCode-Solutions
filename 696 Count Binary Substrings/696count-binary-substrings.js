/**
 * @param {string} s
 * @return {number}
 */
var countBinarySubstrings = function(s) {

    let char = s[0];
    let prev = 0
    let cur = 1
    let total = 0

    for (let i = 1; i < s.length; i++) {
        if (s[i] == char) {
            cur++;
        } else {
            total += Math.min(cur, prev)
            prev = cur
            cur = 1
            char = s[i]
        }
    }

    return total + Math.min(cur, prev)
};