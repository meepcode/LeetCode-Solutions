/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    let bits = Math.ceil(Math.log2(n + 1))
    console.log(bits)

    return n > 0 ? 2 ** Math.ceil(Math.log2(n + 1)) - 1 - n : 1
};