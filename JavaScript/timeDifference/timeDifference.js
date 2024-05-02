/**
 * Calculates the time difference between two dates.
 * @param {Date} date1 - The first date object.
 * @param {Date} date2 - The second date object.
 * @return {number} The absolute time difference in milliseconds.
 */
function timeDifference(date1, date2) {
    // Check if both inputs are Date objects
    if (!(date1 instanceof Date && date2 instanceof Date)) {
        throw new Error('Both inputs must be Date objects.');
    }
    
    // Calculate and return the absolute difference in milliseconds
    return Math.abs(date1 - date2);
}

// Export the function for use in other modules
module.exports = { timeDifference };


