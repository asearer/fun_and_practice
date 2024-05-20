const fizzBuzz = require('./fizzBuzz');

describe('fizzBuzz', () => {
    test('returns correct output for 15', () => {
        const expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'];
        expect(fizzBuzz(15)).toEqual(expected);
    });

    test('handles n = 1 correctly', () => {
        expect(fizzBuzz(1)).toEqual([1]);
    });

    test('handles n = 0 correctly (empty array expected)', () => {
        expect(fizzBuzz(0)).toEqual([]);
    });

    test('returns correct output for 5', () => {
        const expected = [1, 2, 'Fizz', 4, 'Buzz'];
        expect(fizzBuzz(5)).toEqual(expected);
    });

    test('no "Buzz" before 5', () => {
        const results = fizzBuzz(4);
        results.forEach(result => {
            expect(result).not.toBe('Buzz');
        });
    });

    test('includes "FizzBuzz" in output for n >= 15', () => {
        const results = fizzBuzz(15);
        expect(results).toContain('FizzBuzz');
    });
});
