export default function getListStudentIds(studentsArray, city, newGrades) {
  if (studentsArray instanceof Array) {
    const studentsByLoc = studentsArray.filter((elem) => elem.location === city);
    studentsByLoc.map((x) => {
      const newGrade = newGrades.filter((student) => student.studentId === x.id)[0];
      const updatedStudent = x;
      if (newGrade instanceof Object) updatedStudent.grade = newGrade.grade;
      else updatedStudent.grade = 'N/A';
      return updatedStudent;
    });
    return studentsByLoc;
  }
  return [];
}
