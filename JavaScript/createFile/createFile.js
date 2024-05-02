// creates a new file in the current directory
const fs = require('fs');

fs.writeFile('index.js', '', (err) => {
    if (err) {
        console.error('Failed to save the file:', err);
        return;  // Stop execution of this callback
    }
    console.log('The file has been saved!');
});

