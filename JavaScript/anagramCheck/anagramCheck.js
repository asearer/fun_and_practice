function areAnagrams(str1, str2) {
    const normalize = str => str.replace(/\W/g, '').toLowerCase().split('').sort().join('');
    return normalize(str1) === normalize(str2);
}
