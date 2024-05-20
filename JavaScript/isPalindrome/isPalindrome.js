/**
 * Checks if the given string is a palindrome, considering only alphanumeric characters.
 * @param {string} str - The string to check.
 * @return {boolean} True if the string is a palindrome, false otherwise.
 */
function isPalindrome(str) {
    // Clean the string by removing non-alphanumeric characters and converting to lowercase.
    const cleaned = str.replace(/[\W_]/g, '').toLowerCase();

    // Return false if the cleaned string is empty.
    if (cleaned.length === 0) return false;

    // Use a two-pointer approach to check for a palindrome.
    let left = 0;
    let right = cleaned.length - 1;
    while (left < right) {
        if (cleaned[left] !== cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

module.exports = isPalindrome;

