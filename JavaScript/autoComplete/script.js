const input = document.querySelector('#fruit');
const suggestions = document.querySelector('.suggestions ul');

const fruit = ['Apple', 'Apricot', 'Avocado', 'Banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Blueberry', 'Boysenberry', 'Currant', 'Cherry', 'Coconut', 'Cranberry', 'Cucumber', 'Custard apple', 'Damson', 'Date', 'Dragonfruit', 'Durian', 'Elderberry', 'Feijoa', 'Fig', 'Gooseberry', 'Grape', 'Raisin', 'Grapefruit', 'Guava', 'Honeyberry', 'Huckleberry', 'Jabuticaba', 'Jackfruit', 'Jambul', 'Juniper berry', 'Kiwifruit', 'Kumquat', 'Lemon', 'Lime', 'Loquat', 'Longan', 'Lychee', 'Mango', 'Mangosteen', 'Marionberry', 'Melon', 'Cantaloupe', 'Honeydew', 'Watermelon', 'Miracle fruit', 'Mulberry', 'Nectarine', 'Nance', 'Olive', 'Orange', 'Clementine', 'Mandarine', 'Tangerine', 'Papaya', 'Passionfruit', 'Peach', 'Pear', 'Persimmon', 'Plantain', 'Plum', 'Pineapple', 'Pomegranate', 'Pomelo', 'Quince', 'Raspberry', 'Salmonberry', 'Rambutan', 'Redcurrant', 'Salak', 'Satsuma', 'Soursop', 'Star fruit', 'Strawberry', 'Tamarillo', 'Tamarind', 'Yuzu'];

function search(str) {
  let results = [];

  results = fruit.filter(fruitName =>
    fruitName.toLowerCase().includes(str.toLowerCase())
  );

  return results;
}

function searchHandler(e) {
  const inputVal = e.target.value;
  const autocorrectedInput = autocorrect(inputVal);
  const searchResults = search(autocorrectedInput);
  showSuggestions(searchResults, autocorrectedInput);
}

function autocorrect(str) {
  
  const autocorrectMap = {
    appl: 'Apple',
    bnan: 'Banana',
    orng: 'Orange',
    watrmeln: 'Watermelon',
  };

  const lowerCaseStr = str.toLowerCase();
  if (autocorrectMap.hasOwnProperty(lowerCaseStr)) {
    return autocorrectMap[lowerCaseStr];
  }

  return str;
}

function showSuggestions(results, inputVal) {
  suggestions.innerHTML = '';

  results.forEach(result => {
    const li = document.createElement('li');
    li.textContent = result;
    suggestions.appendChild(li);
  });

  if (inputVal) {
    suggestions.style.display = 'block';
  } else {
    suggestions.style.display = 'none';
  }
}

function useSuggestion(e) {
  const selectedSuggestion = e.target.textContent;
  input.value = selectedSuggestion;
  suggestions.innerHTML = '';
  suggestions.style.display = 'none';
}

input.addEventListener('input', searchHandler);
suggestions.addEventListener('click', useSuggestion);

function search(str) {
  let results = [];

  results = fruit.filter(fruitName =>
    fruitName.toLowerCase().includes(str.toLowerCase())
  );

  return results;
}

function searchHandler(e) {
  const inputVal = e.target.value;
  const autocorrectedInput = autocorrect(inputVal);
  const searchResults = search(autocorrectedInput);
  showSuggestions(searchResults, autocorrectedInput);
}

function autocorrect(str) {
  const autocorrectMap = {
    appl: 'Apple',
    bnan: 'Banana',
    orng: 'Orange',
    watrmeln: 'Watermelon',
  };

  const lowerCaseStr = str.toLowerCase();
  if (autocorrectMap.hasOwnProperty(lowerCaseStr)) {
    return autocorrectMap[lowerCaseStr];
  }

  return str;
}

function showSuggestions(results, inputVal) {
  suggestions.innerHTML = '';

  results.forEach(result => {
    const li = document.createElement('li');
    li.textContent = result;
    suggestions.appendChild(li);
  });

  if (inputVal) {
    suggestions.style.display = 'block';
  } else {
    suggestions.style.display = 'none';
  }
}

function useSuggestion(e) {
  const selectedSuggestion = e.target.textContent;
  input.value = selectedSuggestion;
  suggestions.innerHTML = '';
  suggestions.style.display = 'none';
}

input.addEventListener('input', searchHandler);
suggestions.addEventListener('click', useSuggestion);
