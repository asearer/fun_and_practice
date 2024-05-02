const { crawl, fetchHTML } = require('../crawler');
const parser = require('../parser');
const axios = require('axios');

// Mock axios to prevent actual HTTP requests
jest.mock('axios');

describe('fetchHTML', () => {
    it('fetches HTML successfully', async () => {
        const fakeHTML = '<html></html>';
        axios.get.mockResolvedValue({ data: fakeHTML });
        
        const url = 'http://example.com';
        const html = await fetchHTML(url);

        expect(axios.get).toHaveBeenCalledWith(url);
        expect(html).toBe(fakeHTML);
    });

    it('returns null on network error', async () => {
        axios.get.mockRejectedValue(new Error('Network error'));
        
        const html = await fetchHTML('http://example.com');
        
        expect(html).toBeNull();
    });
});

describe('crawl', () => {
    it('returns titles from HTML', async () => {
        const fakeHTML = '<html><a class="title">Title 1</a><a class="title">Title 2</a></html>';
        axios.get.mockResolvedValue({ data: fakeHTML });
        
        jest.spyOn(parser, 'extractTitles').mockReturnValue(['Title 1', 'Title 2']);

        const titles = await crawl('http://example.com');
        
        expect(titles).toEqual(['Title 1', 'Title 2']);
    });
});
