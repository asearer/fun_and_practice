function maxSubArraySum(arr) {
    if (arr.length === 0) {
        return 0; // Or throw an error, or return null/undefined based on the desired behavior when array is empty
    }

    let maxCurrent = arr[0];
    let maxGlobal = arr[0];

    for (let i = 1; i < arr.length; i++) {
        maxCurrent = Math.max(arr[i], maxCurrent + arr[i]);
        if (maxCurrent > maxGlobal) {
            maxGlobal = maxCurrent;
        }
    }

    return maxGlobal;
}

module.exports = maxSubArraySum;
