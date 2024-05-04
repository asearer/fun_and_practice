function areAnagrams(str1, str2) {
    // Check if either string is null or undefined
    if (str1 === null || str1 === undefined || str2 === null || str2 === undefined) {
        return str1 === str2;
    }

    // Function to normalize the input strings
    const normalize = str => {
        return str.replace(/\W/g, '').toLowerCase().split('').sort().join('');
    };

    return normalize(str1) === normalize(str2);
}

module.exports = areAnagrams;
