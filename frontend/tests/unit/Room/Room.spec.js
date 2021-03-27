import Roomvue from '@/views/Room.vue'
import { mount } from '@vue/test-utils'

describe('测试房间组件', () => {
  it('测试代码编辑器和白板的切换按钮', () => {
    const wrapper = mount(Roomvue,{})
    wrapper.vm.editorSwitch = '代码编辑器'
    wrapper.find('.RoomBody el-button').trigger('click')
    expect(wrapper.vm.editorSwitch).toBe('白板')
  })
})
