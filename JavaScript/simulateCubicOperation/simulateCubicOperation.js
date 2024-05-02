// Returns the cubic value of the input number
function getCubicValue(n) {
    return n * n * n;
}

// Simulates an operation with cubic time complexity O(n^3) by printing the cubic value
function simulateCubicOperation(n) {
    const cubicValue = getCubicValue(n);
    console.log("Cubic value of", n, "is:", cubicValue);
}

// Export the functions so they can be used in other files such as your test files
module.exports = { getCubicValue, simulateCubicOperation };