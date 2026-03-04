/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSpecial = function(mat) {
    // Trivial solution
    count = 0;
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[0].length; j++) {
            if (mat[i][j] == 1) {
                let isSpecial = true;
                for (let newI = 0; newI < mat.length && isSpecial; newI++) {
                    isSpecial = (newI == i || mat[newI][j] == 0)
                }
                for (let newJ = 0; newJ < mat[0].length && isSpecial; newJ++) {
                    isSpecial = (newJ == j || mat[i][newJ] == 0)
                }

                if (isSpecial) {
                    count++;
                }
            }
        }
    }

    return count;
};