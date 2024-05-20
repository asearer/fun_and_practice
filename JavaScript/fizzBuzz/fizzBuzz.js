function fizzBuzz(n) {
    const results = [];
    for (let i = 1; i <= n; i++) {
        let output = '';
        if (i % 3 === 0) output += 'Fizz';
        if (i % 5 === 0) output += 'Buzz';
        results.push(output || i);
    }
    return results;
}

module.exports = fizzBuzz;

