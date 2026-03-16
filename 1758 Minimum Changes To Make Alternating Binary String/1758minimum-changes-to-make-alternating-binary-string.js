/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    let numZeros = [0, 0]

    for (let i = 0; i < s.length; i++) {
        if (s[i] == '0') {
            numZeros[i % 2]++;
        }
    }


    if (numZeros[0] > numZeros[1]) {
        return (Math.floor(s.length / 2) + s.length % 2 - numZeros[0]) + numZeros[1]
    } else {
        return (Math.floor(s.length / 2) - numZeros[1]) + numZeros[0]
    }
};