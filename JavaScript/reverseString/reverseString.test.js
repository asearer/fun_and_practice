const { reverseString } = require('./stringFunctions');

test('reverses a simple string', () => {
    expect(reverseString('hello')).toBe('olleh');
});

test('reverses an empty string', () => {
    expect(reverseString('')).toBe('');
});

test('reverses a palindrome string', () => {
    expect(reverseString('madam')).toBe('madam');
});
