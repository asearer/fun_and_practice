// simulateCubicOperation.test.js
const { getCubicValue, simulateCubicOperation } = require('./simulateCubicOperation'); 

describe('getCubicValue', () => {
    test('calculates the cubic value of 3', () => {
        expect(getCubicValue(3)).toBe(27);
    });

    test('calculates the cubic value of 0', () => {
        expect(getCubicValue(0)).toBe(0);
    });

    test('calculates the cubic value of -2', () => {
        expect(getCubicValue(-2)).toBe(-8);
    });
});

describe('simulateCubicOperation', () => {
    beforeEach(() => {
        // Mock console.log to avoid actual console output during testing
        console.log = jest.fn();
    });

    test('prints the correct cubic value', () => {
        simulateCubicOperation(4);
        expect(console.log).toHaveBeenCalledWith('Cubic value of', 4, 'is:', 64);
    });
});

