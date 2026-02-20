/**
 * @param {number} n
 * @return {boolean}
 */
var hasAlternatingBits = function(n) {
    let bitValue = 1;
    let curValue = n;

    while (curValue >= bitValue) {
        curValue -= bitValue;
        bitValue *= 4;
    }

    if (curValue == 0) {
        return true;
    }

    bitValue = 2
    curValue = n

    while (curValue >= bitValue) {
        curValue -= bitValue
        bitValue *= 4
    }

    return curValue == 0
};