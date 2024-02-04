export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  map.forEach((element, key) => {
    if (map.get(key) === 1) map.set(key, 100);
  });
}
