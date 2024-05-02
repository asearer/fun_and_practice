const { earthYearsOnPlanet } = require('./planetYears');

describe('earthYearsOnPlanet', () => {
  test('calculates correct Earth years for Mars', () => {
    expect(earthYearsOnPlanet('Mars')).toBe('One year on Mars is equivalent to 1.8808158 Earth years.');
  });

  test('calculates correct Earth years for Jupiter', () => {
    expect(earthYearsOnPlanet('Jupiter')).toBe('One year on Jupiter is equivalent to 11.862615 Earth years.');
  });

  test('returns message for an unknown planet', () => {
    expect(earthYearsOnPlanet('Pluto')).toBe('Unknown planet');
  });

  test('handles case sensitivity', () => {
    
    expect(earthYearsOnPlanet('jupiter')).toBe('One year on Jupiter is equivalent to 11.862615 Earth years.');
  });
});
