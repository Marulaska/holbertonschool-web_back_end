export default function cleanSet(set, startString) {
  let retString = '';
  if (startString == null || startString.length > 0) {
    set.forEach((value) => {
      // console.log(value.substring(0,startString.length))
      if (value.substring(0, startString.length) === startString) {
        retString += `${value.substring(startString.length)}-`;
      }
    });
  }
  return retString.substring(0, retString.length - 1);
}
