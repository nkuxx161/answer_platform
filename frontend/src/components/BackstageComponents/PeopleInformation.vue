<template>
  <div class="container">
    <div class="teacher-list">
      <h3 class="teacher-list-head">教师列表</h3>
      <div class="teacher-list-content">
        <ul class="teacher-list-ul">
          <li class="teacher-list-li-head">
            <span class="teacher-id-head">教工号</span>
            <span class="teacher-name-head">教师名</span>
          </li>
          <li v-for="(teacher, index) in teacherList" :key="index" class="teacher-list-li">
            <div class="teacher-infor">
              <span class="teacher-id">{{teacher.teacherId}}</span>
              <span class="teacher-name">{{teacher.teacherName}}</span>
              <el-button class="delete-teacher-button" type="primary" icon="el-icon-delete"
                @click="deleteTeacher(teacher.teacherId, teacher.lessonId)">
              </el-button>
            </div>
          </li>
        </ul>
       </div>
    </div>
    <div class="student-list">
      <h3 class="student-list-head">学生列表</h3>
      <div class="student-list-content">
        <ul class="student-list-ul">
          <li class="student-list-li-head">
            <span class="student-id-head">学号</span>
            <span class="student-name-head">学生名</span>
          </li>
          <li v-for="(student, index) in studentList" :key="index" class="student-list-li">
            <div class="student-infor">
              <span class="student-id">{{student.studentId}}</span>
              <span class="student-name">{{student.studentName}}</span>
              <el-button class="delete-student-button" type="primary" icon="el-icon-delete"
                @click="deleteStudent(student.studentId, student.lessonId)">
              </el-button>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InformationList",
  props: ['lessonId'],
  data() {
    return {
      teacherList: [],
      studentList: [],
      mark: 0
    }
  },
  methods: {
    getTeacherList: function () {
      this.$axios.post('teacherClass/getTeacher/', {
        lessonId: this.lessonId
      }).then((response) => {
        if (response.data.code === 'false') {
          this.teacherList = []
        } else {
          this.teacherList = response.data.teacherList
        }
      })
    },
    deleteTeacher: function (delTeacherId,delLessonId) {
      this.$axios.post('teacherClass/deleteTeacher/', {
        teacherId: delTeacherId,
        lessonId: delLessonId
      }).then((response) => {
        if (response.data.code === 'false') {
          alert('删除失败')
        } else {
          this.getTeacherList()
        }
      })
    },
    getStudentList: function () {
      this.$axios.post('studentClass/getStudent/', {
        lessonId: this.lessonId
      }).then((response) => {
        if (response.data.code === 'false') {
          this.studentList = []
        } else {
          this.studentList = response.data.studentList
        }
      })
    },
    deleteStudent: function (delStudentId,delLessonId) {
      this.$axios.post('studentClass/deleteStudent/', {
        studentId: delStudentId,
        lessonId: delLessonId
      }).then((response) => {
        if (response.data.code === 'false') {
          alert('删除失败')
        } else {
          this.getStudentList()
        }
      })
    }
  },
  mounted() {
    this.mark = setInterval(() => {
      this.getTeacherList()
      this.getStudentList()
    }, 500)
  },
  destroyed() {
    clearInterval(this.mark)
  }
}
</script>

<style scoped>
.container {
  display: flex;
}
.teacher-list {
  border: 2px solid lightgray;
  border-radius: 5px;
  width: 320px;
  height: 600px;
  margin: 10px;
}
.teacher-list-head {
  font-weight: bold;
}
.teacher-list-ul {
  margin: 0;
  height: 558px;
  overflow-y: scroll;
}
.teacher-list-li-head {
  list-style: none;
  line-height: 40px;
  height: 40px;
  margin: 5px 0;
  text-align: left;
  position: relative;
}
.teacher-list-li {
  list-style: none;
  line-height: 40px;
  height: 40px;
  margin: 5px 0;
  text-align: left;
  position: relative;
}
.teacher-list-li:hover {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.teacher-name {
  position: absolute;
  left: 100px;
}
.teacher-id-head {
  font-weight: bold;
}
.teacher-name-head {
  position: absolute;
  left: 100px;
  font-weight: bold;
}
.delete-teacher-button {
  float: right;
}
.student-list {
  border: 2px solid lightgray;
  border-radius: 5px;
  width: 320px;
  height: 600px;
  margin: 10px;
}
.student-list-head {
  font-weight: bold;
}
.student-list-ul {
  margin: 0;
  height: 558px;
  overflow-y: scroll;
}
.student-list-li-head {
  list-style: none;
  line-height: 40px;
  height: 40px;
  margin: 5px 0;
  text-align: left;
  position: relative;
}
.student-list-li {
  list-style: none;
  line-height: 40px;
  height: 40px;
  margin: 5px 0;
  text-align: left;
  position: relative;
}
.student-list-li:hover {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.student-name {
  position: absolute;
  left: 100px;
}
.student-id-head {
  font-weight: bold;
}
.student-name-head {
  position: absolute;
  left: 100px;
  font-weight: bold;
}
.delete-student-button {
  float: right;
}
</style>
