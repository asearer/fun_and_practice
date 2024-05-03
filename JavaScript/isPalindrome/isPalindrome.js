function isPalindrome(str) {
    const cleaned = str.replace(/\W/g, '').toLowerCase();
    return cleaned === cleaned.split('').reverse().join('');
}
