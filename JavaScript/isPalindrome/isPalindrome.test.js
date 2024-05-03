const isPalindrome = require('./isPalindrome');

describe('isPalindrome', () => {
  test('recognizes simple palindromes', () => {
    expect(isPalindrome('racecar')).toBe(true);
    expect(isPalindrome('level')).toBe(true);
  });

  test('recognizes complex palindromes with punctuation and spaces', () => {
    expect(isPalindrome('A man, a plan, a canal, Panama')).toBe(true);
    expect(isPalindrome('No lemon, no melon')).toBe(true);
  });

  test('returns false for non-palindromes', () => {
    expect(isPalindrome('hello')).toBe(false);
    expect(isPalindrome('world')).toBe(false);
  });

  test('handles case sensitivity by ignoring it', () => {
    expect(isPalindrome('RaceCar')).toBe(true);
    expect(isPalindrome('Level')).toBe(true);
  });

  test('ignores numbers and special characters properly', () => {
    expect(isPalindrome('12321')).toBe(true);
    expect(isPalindrome('123456')).toBe(false);
    expect(isPalindrome('!@#$%^&*()_+')).toBe(false);
  });

  test('works with empty strings and strings of length 1', () => {
    expect(isPalindrome('')).toBe(false);
    expect(isPalindrome('a')).toBe(true);
    expect(isPalindrome(' ')).toBe(false);
  });
});

