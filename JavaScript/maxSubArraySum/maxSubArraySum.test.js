const maxSubArraySum = require('./maxSubArraySum');

describe('maxSubArraySum', () => {
  test('should return the correct max sum of a non-empty array', () => {
    expect(maxSubArraySum([1, 2, 3, 4])).toBe(10);
    expect(maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])).toBe(6);
    expect(maxSubArraySum([-1, -2, -3, -4])).toBe(-1);
  });

  test('should handle arrays with single element', () => {
    expect(maxSubArraySum([10])).toBe(10);
    expect(maxSubArraySum([-10])).toBe(-10);
  });

  test('should handle empty array by returning 0', () => {
    expect(maxSubArraySum([])).toBe(0);
  });

  test('should handle arrays with all positive numbers', () => {
    expect(maxSubArraySum([1, 2, 3])).toBe(6);
  });

  test('should handle arrays with all negative numbers', () => {
    expect(maxSubArraySum([-1, -2, -3, -4])).toBe(-1);
  });

  test('should handle arrays that require ignoring negative total subarrays', () => {
    expect(maxSubArraySum([3, -9, 2, 2, 2, 1])).toBe(7); // max sum comes from subarray [2, 2, 2, 1]
    expect(maxSubArraySum([2, -3, 4, -1, -2, 1, 5, -3])).toBe(7); // max sum comes from subarray [4, -1, -2, 1, 5]
  });
});

