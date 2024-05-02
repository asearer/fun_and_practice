const axios = require('axios');
const parser = require('./parser');

async function fetchHTML(url) {
    try {
        const response = await axios.get(url);
        return response.data;
    } catch (error) {
        console.error("Error fetching URL:", error);
        return null;
    }
}

async function crawl(url) {
    console.log(`Crawling ${url}`);
    const html = await fetchHTML(url);
    if (html) {
        return parser.extractTitles(html);
    }
    return [];
}

module.exports = { crawl, fetchHTML };

