const average = require('./average'); 

describe('average', () => {
    it('calculates the average of an array of numbers', () => {
        expect(average([1, 2, 3])).toBe(2);
        expect(average([10, 20, 30, 40])).toBe(25);
    });

    it('handles arrays with a single element', () => {
        expect(average([5])).toBe(5);
    });

    it('throws an error for empty arrays', () => {
        expect(() => average([])).toThrow('Input must be a non-empty array');
    });

    it('throws an error if any element is not a number', () => {
        expect(() => average([1, 2, '3', 4])).toThrow('All elements in the array must be numbers');
        expect(() => average([1, true])).toThrow('All elements in the array must be numbers');
        expect(() => average([null])).toThrow('All elements in the array must be numbers');
    });

    it('handles negative and positive numbers', () => {
        expect(average([-1, -2, -3, 3, 2, 1])).toBe(0);
    });

    it('calculates averages resulting in decimal values', () => {
        expect(average([1, 2])).toBe(1.5);
        expect(average([1, 1, 1, 1, 1, 3])).toBeCloseTo(1.333, 3);
    });
});

