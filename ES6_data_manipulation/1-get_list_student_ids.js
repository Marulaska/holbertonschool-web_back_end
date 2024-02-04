export default function getListStudentIds(studentsArray) {
  if (studentsArray instanceof Array) return studentsArray.map((x) => x.id);
  return [];
}
