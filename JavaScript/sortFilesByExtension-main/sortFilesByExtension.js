
function sortFilesByExtension(files) {
    // Sort the files array using a custom comparison function
    files.sort(function(a, b) {
      // Compare the extensions of the files
      if (a.name.split('.').pop() < b.name.split('.').pop()) {
        return 1; // b should come before a
      } else if (a.name.split('.').pop() > b.name.split('.').pop()) {
        return -1; // a should come before b
      }
      return 0; // The extensions are equal, maintain original order
    });
  }