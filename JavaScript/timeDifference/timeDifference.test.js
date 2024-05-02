const { timeDifference } = require('./timeDifference');  

describe('timeDifference function', () => {
    test('should calculate the correct difference in milliseconds between two dates', () => {
        const date1 = new Date('2024-05-01T00:00:00Z');
        const date2 = new Date('2024-05-02T00:00:00Z');
        const expected = 24 * 60 * 60 * 1000; // 86400000 milliseconds (1 day)
        expect(timeDifference(date1, date2)).toBe(expected);
    });

    test('should return 0 when the dates are the same', () => {
        const date = new Date('2024-05-01T00:00:00Z');
        expect(timeDifference(date, date)).toBe(0);
    });

    test('should handle dates in different time zones correctly', () => {
        const date1 = new Date('2024-05-01T00:00:00Z'); // UTC
        const date2 = new Date('2024-05-01T00:00:00-05:00'); // UTC-5
        const expected = 5 * 60 * 60 * 1000; // 18000000 milliseconds (5 hours)
        expect(timeDifference(date1, date2)).toBe(expected);
    });

    test('throws an error if the first argument is not a date', () => {
        const date = new Date('2024-05-01T00:00:00Z');
        const notADate = "2024-05-01";
        expect(() => timeDifference(notADate, date)).toThrow('Both inputs must be Date objects.');
    });

    test('throws an error if the second argument is not a date', () => {
        const date = new Date('2024-05-01T00:00:00Z');
        const notADate = "2024-05-01";
        expect(() => timeDifference(date, notADate)).toThrow('Both inputs must be Date objects.');
    });
});
