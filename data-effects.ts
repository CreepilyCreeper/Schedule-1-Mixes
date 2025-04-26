import {
  mixSubstances,
  mixFromHash,
  encodeMixState,
  decodeMixState,
  effects,
  products,
  substances,
  effectRulesBySubstance,
  Product,
  Substance,
} from '@schedule1-tools/mixer';
import data from './data.json';
import * as fs from "fs";


// Iterate over each datum and add datum_hash and datum_effects to the object.
data.forEach((datum: any) => {
  const state = {
    product: datum.baseProduct as Product,
    substances: datum.bestCombination as Substance[],
  };
  const datum_hash = encodeMixState(state);
  const datum_effects = mixFromHash(datum_hash);

  // Append the new properties to datum.
  datum.hash = datum_hash;
  datum.effects = datum_effects.effects.map((effect: any) => {
    return effects[effect].name;
  });

});

// Log the updated data (or write it back to a file if desired)
//console.log(data);

// Write the updated data back to the original file.
fs.writeFileSync('./data.json', JSON.stringify(data, null, 2));
console.log(`Data saved back to data.json`);
