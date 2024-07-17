function sortFilesBySize(files) {
    // Sort the files array using a custom comparison function
    files.sort(function(a, b) {
      // Compare the sizes of the files
      if (a.size < b.size) {
        return 1; // b should come before a
      } else if (a.size > b.size) {
        return -1; // a should come before b
      }
      return 0; // The sizes are equal, maintain original order
    });
  
    return files;
  }

  // To use this function, pass in an array of file objects with a "size" property, like this:

var files = [
  { name: 'file1.txt', size: 1024 },
  { name: 'file2.jpg', size: 2048 },
  { name: 'file3.png', size: 512 },
  // Add more file objects here...
];

var sortedFiles = sortFilesBySize(files);

console.log(sortedFiles);
