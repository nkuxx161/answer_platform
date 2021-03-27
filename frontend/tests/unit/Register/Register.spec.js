import {mount} from '@vue/test-utils'
import Register from '@/views/Register'

describe('Register.vue', () => {
  it('correct contents', () => {
    const wrapper = mount(Register)
    const h1 = wrapper.find('h1')
    expect(h1.text())
    .toBe('注册')
  })
  it('button exist', () => {
    const wrapper = mount(Register)
    expect(wrapper.contains('el-button')).toBe(true)
  })
  it('div exsit', () => {
    const wrapper = mount(Register)
    expect(wrapper.contains('div')).toBe(true)
  })
  it('input exsit', () => {
    const wrapper = mount(Register)
    expect(wrapper.contains('input')).toBe(true)
  })
  it('span exsit', () => {
    const wrapper = mount(Register)
    expect(wrapper.contains('span')).toBe(true)
  })
  it('choose student', () => {
    const wrapper = mount(Register)
    wrapper.vm.studentRegister()
    expect(wrapper.vm.identity).toBe('student')
  })
  it('choose teacher', () => {
    const wrapper = mount(Register)
    wrapper.vm.teacherRegister()
    expect(wrapper.vm.identity).toBe('teacher')
  })
  it('register student pass diff', () => {
    const wrapper = mount(Register)
    wrapper.find('.student input').trigger('click')
    wrapper.vm.name = "888@qq.com"
    wrapper.vm.password = "888"
    wrapper.vm.rePassword = "888"
    wrapper.vm.card = "888"
    wrapper.vm.relName = "888"
    wrapper.find('.register').trigger('click')
    expect(wrapper.vm.name).toBe('888@qq.com')
    expect(wrapper.vm.password).toBe('888')
    expect(wrapper.vm.rePassword).toBe('888')
    expect(wrapper.vm.card).toBe('888')
    expect(wrapper.vm.relName).toBe('888')
  })
  it('register teacher pass diff', () => {
    const wrapper = mount(Register)
    wrapper.find('.teacher input').trigger('click')
    wrapper.vm.name = "999@qq.com"
    wrapper.vm.password = "999"
    wrapper.vm.rePassword = "999"
    wrapper.vm.card = "999"
    wrapper.vm.relName = "999"
    wrapper.find('.register').trigger('click')
    expect(wrapper.vm.name).toBe('999@qq.com')
    expect(wrapper.vm.password).toBe('999')
    expect(wrapper.vm.rePassword).toBe('999')
    expect(wrapper.vm.card).toBe('999')
    expect(wrapper.vm.relName).toBe('999')
  })
})
