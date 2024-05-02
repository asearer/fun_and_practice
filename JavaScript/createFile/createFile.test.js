// createFile.test.js
const fs = require('fs');
const { promisify } = require('util');
const writeFile = promisify(fs.writeFile);

// Mock the fs module
jest.mock('fs');

describe('writeFile', () => {
    beforeEach(() => {
        // Clear all instances and calls to constructor and all methods:
        jest.clearAllMocks();
    });

    it('should create a file with the correct content', async () => {
        fs.writeFile.mockImplementation((path, data, callback) => {
            callback(null); // simulate success
        });

        await writeFile('index.js', '');

        expect(fs.writeFile).toHaveBeenCalledTimes(1);
        expect(fs.writeFile).toHaveBeenCalledWith('index.js', '', expect.any(Function));
    });

    it('should handle errors', async () => {
        const error = new Error('Failed to write file');
        fs.writeFile.mockImplementation((path, data, callback) => {
            callback(error); // simulate failure
        });

        let caughtError = null;
        try {
            await writeFile('index.js', '');
        } catch (err) {
            caughtError = err;
        }

        expect(caughtError).toEqual(error);
        expect(fs.writeFile).toHaveBeenCalledTimes(1);
        expect(fs.writeFile).toHaveBeenCalledWith('index.js', '', expect.any(Function));
    });
});
