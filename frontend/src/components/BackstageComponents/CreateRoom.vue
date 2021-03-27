<template>
  <jsk-form ref="form" :form-model="form" :form-label-width="80" class="create-room-form">
    <h3>创建答疑房间</h3>
    <jsk-form-item form-item-label="课程名称">
      <jsk-input v-model="form.lessonName"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="课程id">
      <jsk-input v-model="form.lessonId"></jsk-input>
    </jsk-form-item>
    <jsk-form-item form-item-label="课程公告">
      <jsk-input v-model="form.lessonNotice" type="textarea"></jsk-input>
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
  data: function () {
    return {
      form: {
        lessonName: '',
        lessonId: '',
        lessonNotice: ''
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
    onSubmit: function () {
      this.$axios.post('lesson/addLesson/', {
        lessonName: this.form.lessonName,
        lessonId: this.form.lessonId,
        lessonNotice: this.form.lessonNotice
      }).then((response) => {
        if (response.data.code === 'success') {
          alert('创建房间成功')
          this.$emit('refreshRoomList')
        } else if (response.data.code === 'exist') {
          alert('创建失败，该房间已存在')
        } else {
          alert('请确认课程代号和课程名称不为空')
        }
      })
    },
    clearInput: function () {
      this.form.lessonName = ''
      this.form.lessonId = ''
      this.form.lessonNotice = ''
    }
  }
};
</script>

<style scopped>
.create-room-form {
  border: 2px solid lightgray;
  border-radius: 5px;
  text-align: center;
  padding: 20px;
}
h3 {
  font-weight: bold;
}
</style>
