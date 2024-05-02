const cheerio = require('cheerio');

function extractTitles(html) {
    const $ = cheerio.load(html);
    const titles = [];
    $("a.title").each((index, element) => {
        titles.push($(element).text());
    });
    return titles;
}

module.exports = { extractTitles };
