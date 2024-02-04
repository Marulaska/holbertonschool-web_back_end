export default function hasValuesFromArray(set, numArray) {
  let ok = true;
  numArray.forEach((element) => {
    if (!set.has(element)) {
      ok = false;
    }
  });
  return ok;
}
