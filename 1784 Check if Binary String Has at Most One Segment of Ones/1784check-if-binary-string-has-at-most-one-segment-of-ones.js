/**
 * @param {string} s
 * @return {boolean}
 */
var checkOnesSegment = function(s) {
    let hasSeenZero = false; // i.e. has seen a zero
    
    if (s.charAt(0) == '0') {
        return false; // does not begin with 1
    }

    for (let i = 1; i < s.length; i++) {
        if (hasSeenZero && s.charAt(i) == '1') {
            return false;
        } else if (s.charAt(i) == '0') {
            hasSeenZero = true;
        }
    }

    return true;
};