function findDuplicates(...arrays) {
    const allValues = arrays.flat(); // Flatten the arrays into a single array
    const duplicates = [];
    const seen = {};
  
    for (let i = 0; i < allValues.length; i++) {
      const value = allValues[i];
      if (seen[value]) {
        if (seen[value] === 1) {
          duplicates.push(value);
        }
        seen[value]++;
      } else {
        seen[value] = 1;
      }
    }
  
    return duplicates;
  }

// To use this function, pass in the arrays as arguments. For example:

const array1 = [1, 2, 3, 4];
const array2 = [3, 4, 5, 6];
const array3 = [4, 5, 6, 7];

const duplicates = findDuplicates(array1, array2, array3);
console.log(duplicates); // Output: [3, 4]