// Calculates the average of an array of numbers with error handling
function average(numbers) {
    if (!Array.isArray(numbers) || numbers.length === 0) {
        throw new Error("Input must be a non-empty array");
    }
    const sum = numbers.reduce((a, b) => {
        if (typeof b !== 'number') {
            throw new Error("All elements in the array must be numbers");
        }
        return a + b;
    }, 0); // Initialize `reduce` with 0 to ensure the callback runs even for single-element arrays
    return sum / numbers.length;
}

module.exports = average; // Export the function for use in other files


