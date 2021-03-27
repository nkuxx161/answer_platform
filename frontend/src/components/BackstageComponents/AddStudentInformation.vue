<template>
  <jsk-form ref="form" :form-model="form" :form-label-width="80" class="add-student-form">
    <h3>课程{{parentRoomId}}添加学生</h3>
    <jsk-form-item form-item-label="学生邮箱">
      <jsk-input v-model="form.studentEmail"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="学生姓名">
      <jsk-input v-model="form.studentName"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="学生学号">
      <jsk-input v-model="form.studentId"></jsk-input>
    </jsk-form-item>
    <div>
      <jsk-button button-background-color="rgb(102,177,255)" button-type="success" @click="onSubmit">
        确认
      </jsk-button>
      <jsk-button button-background-color="rgb(102,177,255)" button-type="info" @click="clearInput">
        取消
      </jsk-button>
    </div>
  </jsk-form>
</template>

<script>
import {
  form,
  button,
  input,
  FormItem
} from 'jellies'

export default {
  name: 'Addstudent',
  props: ['parentRoomId'],
  data: function () {
    return {
      form: {
        studentEmail: '',
        studentName: '',
        studentId: ''
      }
    }
  },
  components: {
    JskForm: form,
    JskInput: input,
    JskButton: button,
    JskFormItem: FormItem
  },
  methods: {
    onSubmit() {
      if (this.form.studentEmail === '' || this.form.studentName === '' || this.form.studentId === '') {
        alert('添加失败，请输入完整信息')
      } else {
        this.$axios.post('studentClass/addStudent/', {
          lessonId: this.parentRoomId,
          studentEmail: this.form.studentEmail,
          studentId: this.form.studentId,
          studentName: this.form.studentName
        }).then((response) => {
          if (response.data.code === 'true') {
            alert('添加学生信息成功')
          } else if (response.data.code === 'error') {
            alert('请输入正确的邮箱')
          } else {
            alert('该学生已加入课程，请勿重复加入')
          }
        })
      }
    },
    clearInput: function () {
      this.form.studentEmail = ''
      this.form.studentName = ''
      this.form.studentId = ''
    }
  }
};
</script>

<style scopped>
.add-student-form {
  border: 2px solid lightgray;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}
h3 {
  font-weight: bold;
}
</style>
