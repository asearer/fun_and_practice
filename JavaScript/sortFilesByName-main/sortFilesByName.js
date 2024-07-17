function sortFilesByName(files) {
    // Sort the files array using a custom comparison function
    files.sort(function(a, b) {
      // Compare the names of the files
      if (a.name < b.name) {
        return 1; // b should come before a
      } else if (a.name > b.name) {
        return -1; // a should come before b
      }
      return 0; // The names are equal, maintain original order
    });
  }
