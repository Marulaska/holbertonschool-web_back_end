export default function setFromArray(numArray) {
  const set = new Set();
  for (const [, element] of numArray.entries()) {
    set.add(element);
  }
  return set;
}
