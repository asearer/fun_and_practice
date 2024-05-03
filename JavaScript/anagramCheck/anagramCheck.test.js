const areAnagrams = require('./anagramCheck'); 

describe('areAnagrams function tests', () => {
    test('should return true for "listen" and "silent"', () => {
        expect(areAnagrams('listen', 'silent')).toBe(true);
    });

    test('should return true for "triangle" and "integral"', () => {
        expect(areAnagrams('triangle', 'integral')).toBe(true);
    });

    test('should return false when strings are of different lengths', () => {
        expect(areAnagrams('list', 'silent')).toBe(false);
    });

    test('should return true for case insensitive matches', () => {
        expect(areAnagrams('Listen', 'Silent')).toBe(true);
    });

    test('should return true for strings with non-alphabet characters', () => {
        expect(areAnagrams('l*i#s$t%e^n', '!s@i^l&e*n+t')).toBe(true);
    });

    test('should return false for strings that are not anagrams', () => {
        expect(areAnagrams('hello', 'world')).toBe(false);
    });

    test('should return true for empty strings', () => {
        expect(areAnagrams('', '')).toBe(true);
    });

    test('should return true for same strings with varying spaces', () => {
        expect(areAnagrams('  listen  ', 'silent')).toBe(true);
    });

    test('should handle null inputs', () => {
        expect(areAnagrams(null, null)).toBe(true);
    });

    test('should handle undefined inputs', () => {
        expect(areAnagrams(undefined, undefined)).toBe(true);
    });
});
