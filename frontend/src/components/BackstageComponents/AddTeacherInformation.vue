<template>
  <jsk-form ref="form" :form-model="form" :form-label-width="80" class="add-teacher-form">
    <h3>课程{{parentRoomId}}添加老师</h3>
    <jsk-form-item form-item-label="老师邮箱">
      <jsk-input v-model="form.teacherEmail"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="老师姓名">
      <jsk-input v-model="form.teacherName"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="老师工号">
      <jsk-input v-model="form.teacherId"></jsk-input>
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
  name: 'CreateRoom',
  props: ['parentRoomId'],
  data: function () {
    return {
      form: {
        teacherEmail: '',
        teacherName: '',
        teacherId: ''
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
      if (this.form.teacherEmail === '' || this.form.teacherName === '' || this.form.teacherId === '') {
        alert('添加失败，请输入完整信息')
      } else {
        this.$axios.post('teacherClass/addTeacher/', {
          lessonId: this.parentRoomId,
          teacherName: this.form.teacherName,
          teacherId: this.form.teacherId,
          teacherEmail: this.form.teacherEmail
        }).then((response) => {
          if (response.data.code === 'true') {
            alert('添加老师信息成功')
          } else if (response.data.code === 'error') {
            alert('请输入正确的邮箱')
          } else {
            alert('该老师已加入课程，请勿重复加入')
          }
        })
      }
    },
    clearInput: function () {
      this.form.teacherEmail = ''
      this.form.teacherName = ''
      this.form.teacherId = ''
    }

  }
};
</script>

<style scopped>
.add-teacher-form {
  border: 2px solid lightgray;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}
h3 {
  font-weight: bold;
}
</style>
