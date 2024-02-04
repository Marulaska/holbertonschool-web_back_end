export default function getStudentsByLocation(studentsArray, city) {
  return studentsArray.filter((elem) => elem.location === city);
}
