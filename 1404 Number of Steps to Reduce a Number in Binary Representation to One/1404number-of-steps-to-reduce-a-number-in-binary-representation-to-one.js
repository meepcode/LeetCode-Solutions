/**
 * @param {string} s
 * @return {number}
 */
var numSteps = function(s) {
    let carry = false
    count = 0
    for (let i = s.length - 1; i > 0; i--) {
        let even = (!carry && s.charAt(i) == '0') || (carry && s.charAt(i) == '1')

        if (even) {
            count += 1
        } else {
            count += 2
            carry = true
        }
    }

    if (carry) {
        count += 1
    }

    return count;
};