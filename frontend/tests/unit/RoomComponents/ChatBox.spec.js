import { mount } from '@vue/test-utils'
import ChatBox from '@/components/ChatBox'
describe('ChatBox', () => {
  it('has 3 divs', () => {
    const wrapper = mount(ChatBox)
    const divs = wrapper.findAll('div')
    expect(divs).toHaveLength(3)
  })
  it('has a form', () => {
    const wrapper = mount(ChatBox)
    expect(wrapper.find('el-form').exists()).toBe(true)
  })
  it('has an input', () => {
    const wrapper = mount(ChatBox)
    expect(wrapper.find('el-input').exists()).toBe(true)
  })
  it('has a button', () => {
    const wrapper = mount(ChatBox)
    expect(wrapper.find('el-button').exists()).toBe(true)
  })
  it('could write comment', () => {
    const wrapper = mount(ChatBox)
    wrapper.vm.comment = "hello"
    wrapper.find('.chat-box-submit').trigger('click')
    expect(wrapper.vm.comment).toBe("hello")
  })
})
