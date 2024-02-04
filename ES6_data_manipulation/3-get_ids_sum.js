export default function getStudentIdsSum(studentsArray) {
  return studentsArray.reduce((accumulator, value) => accumulator + value.id, 0);
}
