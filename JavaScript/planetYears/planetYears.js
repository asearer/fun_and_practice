const orbitalPeriods = {
    Mercury: 0.2408467,
    Venus: 0.61519726,
    Earth: 1,
    Mars: 1.8808158,
    Jupiter: 11.862615,
    Saturn: 29.447498,
    Uranus: 84.016846,
    Neptune: 164.79132
 };
 
 function earthYearsOnPlanet(planet) {
    // Convert input planet name to capitalize to ensure case insensitivity
    const normalizedPlanet = planet.charAt(0).toUpperCase() + planet.slice(1).toLowerCase();
    
    if (!orbitalPeriods[normalizedPlanet]) {
       return "Unknown planet";
    }
    return `One year on ${normalizedPlanet} is equivalent to ${orbitalPeriods[normalizedPlanet]} Earth years.`;
 }
 
 module.exports = { earthYearsOnPlanet };
 
 
 
 
 