function sortFilesByDate(files) {
    // Sort the files array using a custom comparison function
    files.sort(function(a, b) {
      // Compare the dates of the files
      if (a.lastModifiedDate < b.lastModifiedDate) {
        return 1; // b should come before a
      } else if (a.lastModifiedDate > b.lastModifiedDate) {
        return -1; // a should come before b
      }
      return 0; // The dates are equal, maintain original order
    });
  }